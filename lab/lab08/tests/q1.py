test = {   'name': 'q1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> list(X_normalized.shape) '
                                               '== [506, 52]\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.all([np.isclose(np.sum(X_normalized.iloc[:, '
                                               'i].values * '
                                               'X.iloc[:,i].std()), 0, atol = '
                                               'pow(10, -5)) for i in '
                                               'range(X_normalized.shape[1])])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.all([np.isclose(np.std(X_normalized.iloc[:, '
                                               'i].values), 1, atol = pow(10, '
                                               '-3)) for i in '
                                               'range(X_normalized.shape[1]) '
                                               'if i != 42])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
