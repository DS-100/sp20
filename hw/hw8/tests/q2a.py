test = {   'name': 'q2a',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> mid1_1st_2_pcs.shape == '
                                               '(992, 2)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all(mid1_1st_2_pcs.columns '
                                               "== ['pc1', 'pc2'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'all(np.isclose(mid1_1st_2_pcs.loc[0], '
                                               '[1.7103, -3.4888], '
                                               'atol=1e-4))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'all(np.isclose(mid1_1st_2_pcs.loc[987], '
                                               '[-3.8454, -1.9060], '
                                               'atol=1e-4))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
