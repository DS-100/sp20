test = {   'name': 'q2a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(missing_counts, '
                                               'pd.Series)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> missing_counts.size == 84 '
                                               '# Should have 84 total '
                                               'features (82 features + '
                                               'TotalBathrooms + '
                                               'in_rich_neighborhood)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'set(missing_counts.index.values) '
                                               '== '
                                               'set(training_data.columns.values)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "missing_counts.loc['Fireplace_Qu'] "
                                               '== 975 # Make sure you are '
                                               'calculating the counts '
                                               'correctly\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> missing_counts.iloc[0] == '
                                               '1991 # Make sure you are '
                                               'sorting correctly\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
