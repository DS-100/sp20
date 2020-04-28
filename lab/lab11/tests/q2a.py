test = {   'name': 'q2a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> iris_mean.size == 4\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.all(np.isclose(iris_mean, '
                                               'np.array([5.84333333, '
                                               '3.05733333, 3.758, '
                                               '1.19933333])))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.all(np.isclose(np.zeros(4), '
                                               'np.mean(features, axis=0))) # '
                                               'make sure data is centered at '
                                               '0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> -3.67 < '
                                               'np.sum(features[0]) < -3.64\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
