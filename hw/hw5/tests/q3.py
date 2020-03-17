test = {   'name': 'q3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> training_data.shape[0] == '
                                               '1998 # Make sure that two '
                                               'observations were removed\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure that the max '
                                               'Gr_Liv_Area is now below '
                                               '5000;\n'
                                               '>>> '
                                               "max(training_data['Gr_Liv_Area']) "
                                               '< 5000\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure that the sum '
                                               "of Gr_Liv_Area values hasn't "
                                               'been altered somehow;\n'
                                               '>>> '
                                               "sum(training_data['Gr_Liv_Area']) "
                                               '== 2980752\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
