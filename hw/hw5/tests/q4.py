test = {   'name': 'q4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> not '
                                               "training_data['TotalBathrooms'].isnull().any() "
                                               '# Check that missing values '
                                               'are dealt with\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "training_data['TotalBathrooms'].sum() "
                                               '== 4421.5 # Check that the '
                                               'values are as expected\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "training_data.loc[training_data['PID'] "
                                               '== 903230120, '
                                               "'TotalBathrooms'].iloc[0] == "
                                               '1.0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sum(training_data.loc[:, '
                                               "'TotalBathrooms'] < 2.5) == "
                                               '1124\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
