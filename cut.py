# cut.py

from config import *

def create_cut(hfss):
    return hfss.modeler.create_box(
        origin=[cut_x, cut_y, cut_z],
        sizes=[cut_length, cut_width, cut_height],
        name=cut_name,
        material="vacuum"
    )