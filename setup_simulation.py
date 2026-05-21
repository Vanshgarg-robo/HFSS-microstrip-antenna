from config import *

def create_setup(hfss):
    setup = hfss.create_setup(name=setup_name)

    setup.props["Frequency"] = solution_frequency
    setup.props["MaximumPasses"] = 15
    setup.props["MinimumPasses"] = 2
    setup.props["MinimumConvergedPasses"] = 2
    setup.props["PercentRefinement"] = 30
    setup.props["DeltaS"] = 0.02

    setup.update()

    print(f"{setup_name} created at {solution_frequency}")
    return setup


def create_frequency_sweep(setup):
    sweep = setup.add_sweep(name="Sweep1")

    sweep.props["RangeType"] = "LinearCount"
    sweep.props["RangeStart"] = frequency_sweep_start
    sweep.props["RangeEnd"] = frequency_sweep_stop
    sweep.props["RangeCount"] = frequency_sweep_points
    sweep.props["Type"] = "Interpolating"

    sweep.update()

    print(f"Sweep1 created from {frequency_sweep_start} to {frequency_sweep_stop}")
    return sweep