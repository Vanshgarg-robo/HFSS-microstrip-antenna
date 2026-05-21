def create_s11_report(hfss):
    try:
        hfss.post.create_report(
            expressions="dB(S(LumpedPort1,LumpedPort1))",
            primary_sweep_variable="Freq",
            report_category="Modal Solution Data",
            plot_type="Rectangular Plot",
            plot_name="S11_Report"
        )
        print("S11 report created.")
    except Exception as e:
        print(f"S11 report failed: {e}")


def create_vswr_report(hfss):
    try:
        hfss.post.create_report(
            expressions="VSWR(LumpedPort1)",
            primary_sweep_variable="Freq",
            report_category="Modal Solution Data",
            plot_type="Rectangular Plot",
            plot_name="VSWR_Report"
        )
        print("VSWR report created.")
    except Exception as e:
        print(f"VSWR report failed: {e}")


def create_smith_chart(hfss):
    try:
        hfss.post.create_report(
            expressions="St(LumpedPort1,LumpedPort1)",
            primary_sweep_variable="Freq",
            report_category="Modal Solution Data",
            plot_type="Smith Chart",
            plot_name="Smith_Chart"
        )
        print("Smith chart created.")
    except Exception as e:
        print(f"Smith chart failed: {e}")


def create_impedance_report(hfss):
    try:
        # Use Z instead of Zin for modal solution
        hfss.post.create_report(
            expressions="Z(LumpedPort1,LumpedPort1)",  # Changed from Zin
            primary_sweep_variable="Freq",
            report_category="Modal Solution Data",
            plot_type="Rectangular Plot",
            plot_name="Impedance_Report"
        )
        print("Impedance report created.")
    except Exception as e:
        print(f"Impedance report failed: {e}")

def create_gain_report(hfss):
    try:
        hfss.post.create_report(
            expressions="RealizedGainTotal",
            primary_sweep_variable="Theta",
            secondary_sweep_variable="Phi",
            report_category="Far Fields",
            plot_type="Rectangular Plot",
            context="RadiationSetup1",
            plot_name="Gain_Report"
        )
        print("Gain report created.")
    except Exception as e:
        print(f"Gain report failed: {e}")


def create_radiation_pattern(hfss):
    try:
        hfss.post.create_report(
            expressions="RealizedGainTotal",
            primary_sweep_variable="Theta",
            secondary_sweep_variable="Phi",
            report_category="Far Fields",
            plot_type="3D Polar Plot",
            context="RadiationSetup1",
            plot_name="Radiation_Pattern"
        )
        print("Radiation pattern created.")
    except Exception as e:
        print(f"Radiation pattern failed: {e}")


def create_all_reports(hfss):
    create_s11_report(hfss)
    create_vswr_report(hfss)
    create_smith_chart(hfss)
    create_impedance_report(hfss)
    create_gain_report(hfss)
    create_radiation_pattern(hfss)