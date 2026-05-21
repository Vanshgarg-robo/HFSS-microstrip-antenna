# port.py

from config import *

def create_lumped_port(hfss):

    start = [port_x, 0, ground_z]
    end   = [port_x, 0, ground_z + port_height]

    hfss.lumped_port(
        assignment=port_sheet_name,
        integration_line=[start, end],
        name="LumpedPort1",
        impedance=50
    )