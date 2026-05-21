import sys
sys.path.append(r"C:\Users\vansh garg\Desktop\HFSS\microstrip_antenna")

from ansys.aedt.core import Hfss
from config import *

from ground import create_ground
from substrate import create_substrate
from patch import create_patch
from feed import create_feed
from cut import create_cut
from port_sheet import create_port_sheet
from port import create_lumped_port
from airbox import create_airbox
from boundary import assign_radiation_boundary
from setup_simulation import create_setup, create_frequency_sweep
from farfield import create_farfield_setup
from reports import create_all_reports
from fields import create_all_field_plots
import os

# Launch HFSS
hfss = Hfss()

# Set units
hfss.modeler.model_units = "mm"

print("Creating antenna geometry...")

# Create objects
ground = create_ground(hfss)
substrate = create_substrate(hfss)
patch = create_patch(hfss)
feed = create_feed(hfss)
cut = create_cut(hfss)

# Boolean operations
print("Subtracting cut from patch...")
hfss.modeler.subtract(blank_list=[patch_name], tool_list=[cut_name], keep_originals=False)

print("Uniting patch and feed...")
hfss.modeler.unite([patch_name, feed_name])

# Port sheet
print("Creating port sheet...")
create_port_sheet(hfss)

# Airbox
print("Creating airbox...")
create_airbox(hfss)

# Radiation boundary
print("Assigning radiation boundary...")
assign_radiation_boundary(hfss)

# Lumped port
print("Assigning lumped port...")
create_lumped_port(hfss)

# Analysis setup
print("Creating analysis setup...")
setup = create_setup(hfss)

# Frequency sweep
print("Creating frequency sweep...")
create_frequency_sweep(setup)

# Far-field setup
print("Creating far-field setup...")
create_farfield_setup(hfss)

# Save project
project_path = r"C:\Users\vansh garg\Desktop\HFSS\microstrip_antenna\antenna_project.aedt"
folder = os.path.dirname(project_path)

if not os.path.exists(folder):
    os.makedirs(folder)

print("Saving project...")
hfss.save_project(project_path)

# Run simulation
print("Running simulation...")
hfss.analyze()

# Create reports
print("Creating reports...")
create_all_reports(hfss)

# === BANDWIDTH CALCULATION ===
print("\nCalculating bandwidth...")
try:
    from bandwidth import calculate_bandwidth, print_bandwidth_report
    import numpy as np
    
    # Get solution data
    solution_data = hfss.post.get_solution_data(
        expressions="dB(S(LumpedPort1,LumpedPort1))",
        setup_sweep_name="Setup1 : Sweep1",
        domain="Sweep"
    )
    
    # Get data - returns 2D array: [frequency_row, s11_row]
    raw_data = np.array(solution_data.get_expression_data("dB(S(LumpedPort1,LumpedPort1))"))
    
    # Extract frequency and S11 from the 2D array
    freqs_ghz = raw_data[0, :]  # First row is frequency in GHz
    s11_db = raw_data[1, :]     # Second row is S11 in dB
    
    print(f"Frequency range: {freqs_ghz.min():.3f} - {freqs_ghz.max():.3f} GHz")
    print(f"S11 range: {s11_db.min():.2f} to {s11_db.max():.2f} dB")
    print(f"Data points: {len(freqs_ghz)}")
    
    # Calculate bandwidth
    bw_data = calculate_bandwidth(freqs_ghz, s11_db, threshold=-10.0)
    print_bandwidth_report(bw_data)
    
    # Store bandwidth to file
    if "error" not in bw_data:
        result_path = r"C:\Users\vansh garg\Desktop\HFSS\microstrip_antenna\bandwidth_result.txt"
        with open(result_path, "w") as f:
            f.write("="*50 + "\n")
            f.write("2.4 GHz MICROSTRIP ANTENNA - BANDWIDTH REPORT\n")
            f.write("="*50 + "\n")
            f.write(f"Resonance Frequency: {bw_data['f_resonance_ghz']} GHz\n")
            f.write(f"Minimum S11: {bw_data['s11_min_db']} dB\n")
            f.write(f"-10 dB Bandwidth: {bw_data['bandwidth_mhz']} MHz\n")
            f.write(f"Fractional Bandwidth: {bw_data['fractional_bw_percent']}%\n")
            f.write(f"Lower Cutoff: {bw_data['f_lower_ghz']} GHz\n")
            f.write(f"Upper Cutoff: {bw_data['f_upper_ghz']} GHz\n")
            f.write("="*50 + "\n")
        print(f"\n✅ Bandwidth saved to: {result_path}")
    
except Exception as e:
    print(f"Bandwidth calculation failed: {e}")
    import traceback
    traceback.print_exc()

# Create field plots
print("Creating field plots...")
create_all_field_plots(hfss)

print("Done. Antenna model + setup + sweep + reports + field plots created successfully.")