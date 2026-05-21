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
