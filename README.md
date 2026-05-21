# HFSS Microstrip Antenna Parametric Design Automation

## Overview

This is a **microstrip antenna parametric design automation project** built for **Ansys HFSS** using **PyAEDT**.

Instead of manually designing the antenna in the HFSS GUI, I have written a complete Python automation pipeline. The antenna geometry is fully controlled by **6 design parameters** stored in an array. By simply modifying these parameter values, you can generate antennas for **different operating frequencies** in under **1 minute**.

## How It Works

- The antenna design is **code-driven**, not CAD-driven.
- **6 geometric parameters** (ground length, ground width, patch length, patch width, and 2 additional parameters) are stored in a parametric array.
- Change the array values → Run the script → A new antenna design is automatically generated and simulated in HFSS.
- Total execution time: **~0.5 to 1 minute** per design variant.

## Features

- Fully automated HFSS geometry creation via PyAEDT
- Parametric design using a 6-element configuration array
- Rapid prototyping: generate multiple frequency variants instantly
- Automated simulation setup and execution
- Results export (S-parameters, radiation patterns, etc.)

## Project Structure
