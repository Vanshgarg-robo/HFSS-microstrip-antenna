# substrate.py

from config import *

def create_substrate(hfss):
    return hfss.modeler.create_box(
        origin=[substrate_x, substrate_y, substrate_z],
        sizes=[substrate_length, substrate_width, substrate_height],
        name=substrate_name,
        material=substrate_material
    )