# ground.py

from config import *

def create_ground(hfss):
    return hfss.modeler.create_box(
        origin=[ground_x, ground_y, ground_z],
        sizes=[ground_length, ground_width, ground_height],
        name=ground_name,
        material=ground_material
    )