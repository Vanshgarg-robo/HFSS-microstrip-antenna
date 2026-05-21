# boundary.py

from config import *

def assign_radiation_boundary(hfss):

    airbox = hfss.modeler.get_object_from_name(airbox_name)

    hfss.assign_radiation_boundary_to_faces(
        airbox.faces,
        name="RadiationBoundary"
    )