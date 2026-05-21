from config import *

def create_e_field_plot(hfss):
    try:
        hfss.post.create_fieldplot_surface(
            assignment=[patch_name],
            quantity="Mag_E",
            plot_name="E_Field_Plot"
        )
        print("E-field plot created.")
    except Exception as e:
        print(f"E-field plot failed: {e}")


def create_h_field_plot(hfss):
    try:
        hfss.post.create_fieldplot_surface(
            assignment=[patch_name],
            quantity="Mag_H",
            plot_name="H_Field_Plot"
        )
        print("H-field plot created.")
    except Exception as e:
        print(f"H-field plot failed: {e}")


def create_current_plot(hfss):
    try:
        hfss.post.create_fieldplot_surface(
            assignment=[patch_name],
            quantity="Jsurf",
            plot_name="Current_Distribution"
        )
        print("Current distribution plot created.")
    except Exception as e:
        print(f"Current plot failed: {e}")


def create_all_field_plots(hfss):
    create_e_field_plot(hfss)
    create_h_field_plot(hfss)
    create_current_plot(hfss)