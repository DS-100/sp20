test = {   'name': 'q3a',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(rated_geo, '
                                               'pd.DataFrame)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> set(rated_geo.columns) == '
                                               "set(['latitude', 'longitude', "
                                               "'score'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> (rated_geo.shape[0] > '
                                               '20000) and (rated_geo.shape[0] '
                                               '< 25000) == True\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
