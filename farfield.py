def create_farfield_setup(hfss):
    try:
        hfss.insert_infinite_sphere(
            name="RadiationSetup1"
        )
        print("Far-field radiation setup created successfully.")
    except Exception as e:
        print(f"Far-field setup creation failed: {e}")