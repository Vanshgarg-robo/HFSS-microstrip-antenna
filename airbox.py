# airbox.py

from config import *

def create_airbox(hfss):
    return hfss.modeler.create_box(
        origin=[airbox_x, airbox_y, airbox_z],
        sizes=[airbox_length, airbox_width, airbox_height],
        name=airbox_name,
        material=airbox_material
    )