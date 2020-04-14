test = {   'name': 'q3d',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> np.isclose(s[0], '
                                               '0.02514825, 1e-3)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> train.shape == (53680, '
                                               '16)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> test.shape == (13421, 16)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> list(train['region'][:8]) "
                                               '== [1, 1, 0, 1, 2, 1, 1, 0]\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> list(test['region'][:8]) "
                                               '== [2, 1, 2, 0, 1, 0, 1, 2]\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "sum(train[train['region']==1]['duration']) "
                                               '== 11666210\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "sum(test[test['region']==1]['duration']) "
                                               '== 2897696\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
