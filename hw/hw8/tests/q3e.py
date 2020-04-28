test = {   'name': 'q3e',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> first_2_pcs.shape == (51, '
                                               '2)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all(first_2_pcs.columns == '
                                               "['pc1', 'pc2'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'all(np.isclose(first_2_pcs.loc[0], '
                                               '[-2.7338, 0.8789], '
                                               'atol=1e-4))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'all(np.isclose(first_2_pcs.loc[46], '
                                               '[-0.7269, -1.3023], '
                                               'atol=1e-4))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'all(np.isclose(first_2_pcs.loc[28], '
                                               '[0.6075, -1.4480], '
                                               'atol=1e-4))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
