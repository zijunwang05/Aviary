import aviary.api as av

phase_info = {
    'pre_mission': {'include_takeoff': False, 'optimize_mass': True},
    'climb': {
        'subsystem_options': {'aerodynamics': {'method': 'computed'}},
        'user_options': {
            'num_segments': 5,
            'order': 3,
            'mach_optimize': False,
            'mach_initial': (0.2, 'unitless'),
            'mach_final': (0.8, 'unitless'),
            'mach_bounds': ((0.18, 0.82), 'unitless'),
            'mach_polynomial_order': 3,
            'altitude_optimize': False,
            'altitude_initial': (0.0, 'ft'),
            'altitude_final': (30000.0, 'ft'),
            'altitude_bounds': ((0.0, 34000.0), 'ft'),
            'altitude_polynomial_order': 3,
            'throttle_enforcement': 'path_constraint',
            'time_initial': (0.0, 'min'),
            'time_duration_bounds': ((15.0, 100.0), 'min'),
        },
    },
    'cruise': {
        'subsystem_options': {'aerodynamics': {'method': 'computed'}},
        'user_options': {
            'num_segments': 5,
            'order': 3,
            'mach_optimize': False,
            'mach_initial': (0.8, 'unitless'),
            'mach_final': (0.8, 'unitless'),
            'mach_bounds': ((0.78, 0.82), 'unitless'),
            'mach_polynomial_order': 3,
            'altitude_optimize': False,
            'altitude_initial': (30000.0, 'ft'),
            'altitude_final': (32000.0, 'ft'),
            'altitude_bounds': ((23000.0, 38000.0), 'ft'),
            'altitude_polynomial_order': 3,
            'throttle_enforcement': 'path_constraint',
            'time_initial_bounds': ((15.0, 120.0), 'min'),
            'time_duration_bounds': ((25.0, 120.0), 'min'),
        },
    },
    'descent': {
        'subsystem_options': {'aerodynamics': {'method': 'computed'}},
        'user_options': {
            'num_segments': 5,
            'order': 3,
            'mach_optimize': False,
            'mach_initial': (0.8, 'unitless'),
            'mach_final': (0.36, 'unitless'),
            'mach_bounds': ((0.34, 0.82), 'unitless'),
            'mach_polynomial_order': 3,
            'altitude_optimize': False,
            'altitude_initial': (32000.0, 'ft'),
            'altitude_final': (500.0, 'ft'),
            'altitude_bounds': ((0.0, 38000.0), 'ft'),
            'altitude_polynomial_order': 3,
            'throttle_enforcement': 'path_constraint',
            'time_initial_bounds': ((80.0, 150.0), 'min'),
            'time_duration_bounds': ((10.0, 100.0), 'min'),
        },
    },
    'post_mission': {
        'include_landing': False,
        'target_range': (700, 'nmi'),
    },
}

aircraft_data = 'models/aircraft/minimum_T45_FLOPS.csv'

prob = av.AviaryProblem(verbosity=0)

prob.load_inputs(aircraft_data, phase_info)
prob.check_and_preprocess_inputs()

prob.build_model()

prob.add_driver('IPOPT', max_iter=50)

prob.add_design_variables()
prob.add_objective()

prob.setup()

prob.run_aviary_problem()

print('Done')