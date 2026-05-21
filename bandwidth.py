# bandwidth.py
import numpy as np

def calculate_bandwidth(freqs_ghz, s11_db, threshold=-10.0):
    """
    Calculate bandwidth from S11 data.
    
    Parameters:
        freqs_ghz: array of frequencies in GHz
        s11_db: array of S11 values in dB
        threshold: S11 threshold (default -10 dB)
    
    Returns:
        dict with bandwidth metrics
    """
    # Validate input arrays have same length
    if len(freqs_ghz) != len(s11_db):
        return {"error": f"Array size mismatch: freqs={len(freqs_ghz)}, s11={len(s11_db)}"}
    
    # Find where S11 is below threshold (good matching)
    mask = s11_db <= threshold
    
    if not np.any(mask):
        return {"error": f"No points meet {threshold} dB criteria"}
    
    # Find continuous regions
    indices = np.where(mask)[0]
    
    # Find the largest continuous band (for single-band antennas)
    gaps = np.diff(indices)
    if len(gaps) > 0 and np.any(gaps > 5):  # Gap > 5 points suggests multi-band
        # Handle multi-band case - find largest segment
        split_points = np.where(gaps > 5)[0] + 1
        segments = np.split(indices, split_points)
        largest_segment = max(segments, key=len)
    else:
        largest_segment = indices
    
    # Safety check for indices
    if largest_segment[0] >= len(freqs_ghz) or largest_segment[-1] >= len(freqs_ghz):
        return {"error": f"Index out of bounds: segment={largest_segment}, array size={len(freqs_ghz)}"}
    
    f_lower = freqs_ghz[largest_segment[0]]
    f_upper = freqs_ghz[largest_segment[-1]]
    f_center = (f_lower + f_upper) / 2
    bw_absolute = f_upper - f_lower
    bw_fractional = (bw_absolute / f_center) * 100 if f_center != 0 else 0
    
    # Find minimum S11 (resonance) with bounds checking
    min_idx = np.argmin(s11_db)
    
    # Safety check
    if min_idx >= len(freqs_ghz):
        return {"error": f"Resonance index {min_idx} out of bounds for array size {len(freqs_ghz)}"}
    
    f_resonance = freqs_ghz[min_idx]
    s11_min = s11_db[min_idx]
    
    return {
        "threshold_db": threshold,
        "f_lower_ghz": round(f_lower, 3),
        "f_upper_ghz": round(f_upper, 3),
        "f_center_ghz": round(f_center, 3),
        "f_resonance_ghz": round(f_resonance, 3),
        "bandwidth_mhz": round(bw_absolute * 1000, 2),
        "fractional_bw_percent": round(bw_fractional, 2),
        "s11_min_db": round(s11_min, 2)
    }


def print_bandwidth_report(data):
    """Pretty print bandwidth results"""
    if "error" in data:
        print(f"\n❌ {data['error']}")
        return
    
    print("\n" + "="*50)
    print("📊 BANDWIDTH ANALYSIS REPORT")
    print("="*50)
    print(f"Threshold:              {data['threshold_db']} dB")
    print(f"Resonance Frequency:    {data['f_resonance_ghz']} GHz")
    print(f"Minimum S11:            {data['s11_min_db']} dB")
    print("-"*50)
    print(f"Lower Cutoff (f₁):      {data['f_lower_ghz']} GHz")
    print(f"Upper Cutoff (f₂):      {data['f_upper_ghz']} GHz")
    print(f"Center Frequency (f₀):  {data['f_center_ghz']} GHz")
    print("-"*50)
    print(f"Absolute Bandwidth:     {data['bandwidth_mhz']} MHz")
    print(f"Fractional Bandwidth:   {data['fractional_bw_percent']}%")
    print("="*50)