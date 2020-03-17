test = {   'name': 'q1b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'add_bias(X_features.copy()) == '
                                               'None\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> list(X.columns) == '
                                               "['ones', 'carat', 'depth', "
                                               "'table']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(np.array(X['ones']) "
                                               '== np.ones((len(X), '
                                               '1)).flatten())\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
