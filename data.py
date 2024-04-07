# dummy_schedule = {'1': {
#     'A': {'10': 'Empty', '11': 'Empty', '12': 'Empty', '13': 'Empty', '14': 'Empty', '15': 'Empty', '16': 'Empty',
#           '17': 'Empty'}}, '2': {
#     'A': {'10': 'Empty', '11': 'Empty', '12': 'Empty', '13': 'Empty', '14': 'Empty', '15': 'Empty', '16': 'Empty',
#           '17': 'Empty'}}, '3': {
#     'A': {'12': 'Empty', '13': 'Empty', '14': 'Empty', '15': 'Empty', '16': 'Empty', '17': 'Empty', '18': 'Empty',
#           '19': 'Empty'}}, '4': {
#     'A': {'12': 'Empty', '13': 'Empty', '14': 'Empty', '15': 'Empty', '16': 'Empty', '17': 'Empty', '18': 'Empty',
#           '19': 'Empty'}, 'B': {'16': 'Empty', '17': 'Empty', '18': 'Empty', '19': 'Empty'}}, '5': {
#     'A': {'12': 'Empty', '13': 'Empty', '14': 'Empty', '15': 'Empty', '16': 'Empty', '17': 'Empty', '18': 'Empty',
#           '19': 'Empty', '20': 'Empty', '21': 'Empty'},
#     'B': {'14': 'Empty', '15': 'Empty', '16': 'Empty', '17': 'Empty', '18': 'Empty', '19': 'Empty'}}, '6': {
#     'A': {'12': 'Empty', '13': 'Empty', '14': 'Empty', '15': 'Empty', '16': 'Empty', '17': 'Empty', '18': 'Empty',
#           '19': 'Empty', '20': 'Empty', '21': 'Empty'},
#     'B': {'12': 'Empty', '13': 'Empty', '14': 'Empty', '15': 'Empty', '16': 'Empty', '17': 'Empty', '18': 'Empty',
#           '19': 'Empty', '20': 'Empty', '21': 'Empty'},
#     'C': {'14': 'Empty', '15': 'Empty', '16': 'Empty', '17': 'Empty', '18': 'Empty', '19': 'Empty'}}, '7': {
#     'A': {'10': 'Empty', '11': 'Empty', '12': 'Empty', '13': 'Empty', '14': 'Empty', '15': 'Empty', '16': 'Empty',
#           '17': 'Empty'},
#     'B': {'10': 'Empty', '11': 'Empty', '12': 'Empty', '13': 'Empty', '14': 'Empty', '15': 'Empty', '16': 'Empty',
#           '17': 'Empty'}, 'C': {'12': 'Empty', '13': 'Empty', '14': 'Empty', '15': 'Empty'}}}

schedule = {
    "2024-04-01": {
        1: {
            10: "Empty",
            11: "Empty",
            12: "Empty",
            13: "Empty",
            14: "Empty",
            15: "Empty",
            16: "Empty",
            17: "Empty"
        }
    },
    "2024-04-02": {
        1: {
            10: "Empty",
            11: "Empty",
            12: "Empty",
            13: "Empty",
            14: "Empty",
            15: "Empty",
            16: "Empty",
            17: "Empty"
        }
    },
    "2024-04-03": {
        1: {
            10: "Empty",
            11: "Empty",
            12: "Empty",
            13: "Empty",
            14: "Empty",
            15: "Empty",
            16: "Empty",
            17: "Empty"
        }
    },
    "2024-04-04": {
        1: {
            10: "Empty",
            11: "Empty",
            12: "Empty",
            13: "Empty",
            14: "Empty",
            15: "Empty",
            16: "Empty",
            17: "Empty"
        },
        2: {
            10: "Empty",
            11: "Empty",
            12: "Empty",
            13: "Empty",
            14: "Empty",
            15: "Empty",
            16: "Empty",
            17: "Empty"
        }
    },
    "2024-04-05": {
        1: {
            10: "Empty",
            11: "Empty",
            12: "Empty",
            13: "Empty",
            14: "Empty",
            15: "Empty",
            16: "Empty",
            17: "Empty"
        },
        2: {
            12: "Empty",
            13: "Empty",
            14: "Empty",
            15: "Empty",
            16: "Empty",
            17: "Empty"
        },
        3: {
            12: "Empty",
            13: "Empty",
            14: "Empty",
            15: "Empty"
        }
    }
}

employees = {
    'Alice': {
        'calendar': {
            "2024-04-02": {
                12: "Busy",
                13: "Busy",
                14: "Busy"
            },
            "2024-04-03": {
                9: "Busy",
                10: "Busy",
                11: "Busy",
                12: "Busy"
            },
            "2024-04-05": {
                16: "Busy",
                17: "Busy",
                18: "Busy"
            }
        },
        'min_shift_len': 3,
        'max_shift_len': 9
    },
    'Bob': {
        'calendar': {
            "2024-04-01": {
                10: "Busy",
                11: "Busy",
                12: "Busy"
            },
            "2024-04-02": {
                8: "Busy",
                9: "Busy",
                10: "Busy",
                17: "Busy",
                18: "Busy"
            },
            "2024-04-06": {
                14: "Busy",
                15: "Busy",
                16: "Busy"
            }
        },
        'min_shift_len': 2,
        'max_shift_len': 10
    },
    'Christine': {
        'calendar': {
            "2024-04-04": {
                10: "Busy",
                11: "Busy",
                12: "Busy",
                13: "Busy",
                14: "Busy",
                15: "Busy",
                16: "Busy",
                17: "Busy"
            },
            "2024-04-05": {
                8: "Busy",
                9: "Busy",
                10: "Busy",
                11: "Busy",
                12: "Busy",
                13: "Busy",
                14: "Busy",
                15: "Busy",
                16: "Busy",
            },
            "2024-04-06": {
                16: "Busy",
                17: "Busy",
                18: "Busy"
            }
        },
        'min_shift_len': 5,
        'max_shift_len': 9
    },
    'David': {
        'calendar': {
            "2024-04-02": {
                10: "Busy",
                11: "Busy",
                12: "Busy",
                13: "Busy",
                14: "Busy",
                15: "Busy",
                16: "Busy",
                17: "Busy"
            },
            "2024-04-03": {
                8: "Busy",
                9: "Busy",
                10: "Busy",
                11: "Busy",
                12: "Busy",
                13: "Busy",
                14: "Busy",
                15: "Busy",
                16: "Busy",
            },
            "2024-04-05": {
                10: "Busy",
                11: "Busy",
                12: "Busy",
                13: "Busy",
            }
        },
        'min_shift_len': 4,
        'max_shift_len': 9
    },
    'Eve': {
        'calendar': {
            "2024-04-02": {
                10: "Busy",
                11: "Busy",
                12: "Busy",
                13: "Busy"
            },
            "2024-04-03": {
                13: "Busy",
                14: "Busy",
                15: "Busy",
                16: "Busy",
            },
            "2024-04-05": {
                14: "Busy",
                15: "Busy",
                16: "Busy",
                17: "Busy",
            }
        },
        'min_shift_len': 4,
        'max_shift_len': 9
    }
}

adjusted_schedule = {
    "2024-04-01": {
        1: {
            "shift_len": 8,
            "unavailabilities": {
                2: [0, 1, 2]
            }
        }
    },
    "2024-04-02": {
        1: {
            "shift_len": 8,
            "unavailabilities": {
                1: [2, 3, 4],
                2: [0, 7],
                4: [0, 1, 2, 3, 4, 5, 6, 7],
                5: [0, 1, 2, 3]
            }
        }
    },
    "2024-04-03": {
        1: {
            "shift_len": 8,
            "unavailabilities": {
                1: [0, 1, 2],
                4: [0, 1, 2, 3, 4, 5, 6],
                5: [3, 4, 5, 6]
            }
        }
    },
    "2024-04-04": {
        1: {
            "shift_len": 8,
            "unavailabilities": {
                3: [0, 1, 2, 3, 4, 5, 6, 7]
            }
        },
        2: {
            "shift_len": 8,
            "unavailabilities": {
                3: [0, 1, 2, 3, 4, 5, 6, 7]
            }
        }
    },
    "2024-04-05": {
        1: {
            "shift_len": 8,
            "unavailabilities": {
                1: [6, 7],
                3: [0, 1, 2, 3, 4, 5, 6],
                4: [0, 1, 2, 3],
                5: [4, 5, 6, 7]
            }
        },
        2: {
            "shift_len": 6,
            "unavailabilities": {
                1: [4, 5],
                3: [0, 1, 2, 3, 4],
                4: [0, 1],
                5: [2, 3, 4, 5]
            }
        },
        3: {
            "shift_len": 4,
            "unavailabilities": {
                3: [0, 1, 2, 3],
                4: [0, 1],
                5: [2, 3]
            }
        }
    }
}
