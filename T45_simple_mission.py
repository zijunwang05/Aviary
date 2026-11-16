import aviary.api as av
from aviary.api import Aircraft

prob = av.run_aviary(
    aircraft_data='models/aircraft/minimum_T45_FLOPS.csv',
    phase_info='models/missions/T45_energy_state.py',
)