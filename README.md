# HFSS Microstrip Antenna Parametric Design Automation

## Overview

This is a **microstrip antenna parametric design automation project** built for **Ansys HFSS** using **PyAEDT**.

Instead of manually designing the antenna in the HFSS GUI, I have written a complete Python automation pipeline. The antenna geometry is fully controlled by **6 design parameters** stored in an array. By simply modifying these parameter values, you can generate antennas for **different operating frequencies** in under **1 minute**.

## How It Works

- The antenna design is **code-driven**, not CAD-driven.
- **6 geometric parameters** are stored in a configuration array in `config.py`:
  1. Ground Length
  2. Ground Width  
  3. Patch Length
  4. Patch Width
  5. Feed Length
  6. Feed Width
- Change the array values in `config.py` → Run `main.py` → A new antenna design is automatically generated and simulated in HFSS.
- Total execution time: **~0.5 to 1 minute** per design variant.

## Project Structure

hfss-microstrip-antenna/

├── main.py                 # Main entry point — run this file

├── config.py               # 6-parameter array and all design variables

├── ground.py               # Ground plane geometry

├── substrate.py            # FR4 substrate geometry

├── patch.py                # Radiating patch geometry

├── feed.py                 # Microstrip feed line geometry

├── cut.py                  # Slot/notch geometry (subtracted from patch)

├── port_sheet.py           # Port sheet rectangle

├── port.py                 # Lumped port assignment

├── airbox.py               # Air box for radiation boundary

├── boundary.py             # Radiation boundary assignment

├── setup_simulation.py     # HFSS analysis setup & frequency sweep

├── farfield.py             # Far-field radiation setup

├── reports.py              # S11, VSWR, Smith Chart, Impedance, Gain, Radiation Pattern

├── fields.py               # E-field, H-field, Current distribution plots

├── bandwidth.py            # Bandwidth calculation from S11 data

└── README.md               # Project documentation


## Parameters

The 6 design parameters stored in `config.py`:

| Parameter | Description | Unit |
|-----------|-------------|------|
| Ground Length | Ground plane length | mm |
| Ground Width | Ground plane width | mm |
| Patch Length | Radiating patch length | mm |
| Patch Width | Radiating patch width | mm |
| Feed Length | Microstrip feed line length | mm |
| Feed Width | Microstrip feed line width | mm |

Example configuration:
```python
# config.py
x = [60, 60, 29.4, 38, 30, 3]
#     |   |    |    |   |  |
#     |   |    |    |   |  └── Feed Width (mm)
#     |   |    |    |   └──── Feed Length (mm)
#     |   |    |    └──────── Patch Width (mm)
#     |   |    └───────────── Patch Length (mm)
#     |   └────────────────── Ground Width (mm)
#     └────────────────────── Ground Length (mm)
```


**Prerequisites:**

  -Ansys Electronics Desktop (HFSS) installed
  
  -Python 3.8 or higher
  
  -PyAEDT library installed

**Usage:**

  1.Set up your HFSS/PyAEDT environment.
  
  2.Update the parameter array x in config.py with your desired dimensions.
  
  3.Run the main script:
```python
python main.py
```

  4.The script will automatically:
  
    -Launch HFSS
    
    -Build the antenna geometry (ground, substrate, patch, feed, cut)
    
    -Assign materials and boundaries
    
    -Create port and simulation setup
    
    -Run the frequency sweep
    
    -Generate reports (S11, VSWR, Smith Chart, Gain, Radiation Pattern)
    
    -Create field plots (E-field, H-field, Current)
    
    -Calculate and save bandwidth results


**Results:**
  
  -Return Loss (S11) plot
  
  -Voltage Standing Wave Ratio (VSWR)
  
  -Smith Chart
  
  -Impedance plot
  
  -Gain plot
  
  -3D Radiation Pattern
  
  -E-field, H-field, Current distribution plots
  
  -Bandwidth report (saved as bandwidth_result.txt)


##**Author:**

Vansh Garg
