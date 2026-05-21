# patch.py

from config import *

def create_patch(hfss):
    return hfss.modeler.create_box(
        origin=[patch_x, patch_y, patch_z],
        sizes=[patch_length, patch_width, patch_height],
        name=patch_name,
        material=patch_material
    )