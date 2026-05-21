# feed.py

from config import *

def create_feed(hfss):
    return hfss.modeler.create_box(
        origin=[feed_x, feed_y, feed_z],
        sizes=[feed_length, feed_width, feed_height],
        name=feed_name,
        material=feed_material
    )