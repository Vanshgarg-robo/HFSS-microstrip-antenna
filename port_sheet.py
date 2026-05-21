# port_sheet.py

from config import *

def create_port_sheet(hfss):
    return hfss.modeler.create_rectangle(
        orientation="YZ",
        origin=[port_x, port_y, port_z],
        sizes=[port_width, port_height],
        name=port_sheet_name,
        material="vacuum"
    )