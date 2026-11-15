import aviary.api as av
from aviary.api import Aircraft, Dynamic, Mission, Settings

prob = av.run_aviary(
    aircraft_data='models/aircraft/minimum/minimum_single_aisle_FLOPS.csv',
    phase_info='models/missions/energy_state_default',
)