# config.py

# =========================
# UNITS
# =========================
unit = "mm"

# =========================
# INPUTS
# =========================
x = [60,60,29.4,38,30,3]

ground_length = x[0]
ground_width = x[1]
patch_length = x[2]
patch_width = x[3]
feed_length = x[4]
feed_width = x[5]

# =========================
# MATERIALS
# =========================
ground_material = "copper"
patch_material = "copper"
feed_material = "copper"
substrate_material = "FR4_epoxy"
airbox_material = "air"

# =========================
# THICKNESSES
# =========================
copper_thickness = 0.035
substrate_thickness = 1.6

# =========================
# GROUND
# =========================
ground_name = "Ground"
#ground_length = 60                                                  ##
#ground_width = 60                                                   ##
ground_height = copper_thickness

ground_x = -(ground_length/2)                                      ##
ground_y = -(ground_width/2)                                       ##
ground_z = 0

# =========================
# SUBSTRATE
# =========================
substrate_name = "Substrate"
substrate_length = ground_length
substrate_width = ground_width
substrate_height = substrate_thickness

substrate_x = -(substrate_length/2)                                ##
substrate_y = -(substrate_width/2)                                 ##
substrate_z = ground_z + ground_height

# =========================
# PATCH
# =========================
patch_name = "Patch"
#patch_length = 29.4
#patch_width = 38
patch_height = copper_thickness

patch_x = -(patch_length/2)                                        ##
patch_y = -(patch_width/2)                                         ##
patch_z = substrate_z + substrate_height

# =========================
# FEED
# =========================
feed_name = "FeedLine"
feed_x = 0
feed_y = -1.5
feed_z = patch_z

#feed_length = 30                                                    ##
#feed_width = 3                                                      ##
feed_height = copper_thickness

# =========================
# CUT (Closed Slot)
# safer positive dimensions
# =========================
cut_name = "CutBox"
cut_x = 5.2                                                         ##
cut_y = -2.5                                                        ##
cut_z = patch_z                                                     ##

cut_length = 9.5                                                    ##
cut_width = 5                                                       ##
cut_height = copper_thickness

# =========================
# PORT SHEET
# =========================
port_sheet_name = "PortSheet"
port_x = substrate_length / 2
port_y = -feed_width / 2
port_z = ground_z

port_width = feed_width
port_height = substrate_height + (2 * copper_thickness)

# =========================
# AIR BOX
# =========================
airbox_name = "AirBox"
airbox_length = 80                                                  ##
airbox_width = 80                                                   ##
airbox_height = 40

airbox_x = -(airbox_length/2)
airbox_y = -(airbox_width/2)
airbox_z = -(airbox_height/2)

# =========================
# SIMULATION
# =========================
setup_name = "Setup1"
solution_frequency = "2.4GHz"
frequency_sweep_start = "1GHz"
frequency_sweep_stop = "3GHz"
frequency_sweep_points = 201
