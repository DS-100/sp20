test = {   'name': 'q1b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> all(np.isclose([sum(u[:, '
                                               'i] ** 2) for i in '
                                               'range(u.shape[1])], [1, 1, '
                                               '1]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all(np.isclose([sum(vt[i, '
                                               ':] ** 2) for i in '
                                               'range(vt.shape[1])], [1, 1, '
                                               '1]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> len(s) == 3\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> (np.isclose(u @ np.diag(s) '
                                               '@ vt, '
                                               'surfboard_centered)).all()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
