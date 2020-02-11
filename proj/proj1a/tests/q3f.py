test = {   'name': 'q3f',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> 'postal5' in bus.columns\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> (bus['postal5'].str.len() "
                                               '!= 5).sum() == 221\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "bus['postal5'].isin(valid_zips).sum() "
                                               '== 6032\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "bus['postal5'].isna().sum() == "
                                               '221\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
