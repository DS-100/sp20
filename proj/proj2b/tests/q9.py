test = {   'name': 'q9',
    'points': 15,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'isinstance(test_predictions, '
                                               'np.ndarray) # must be ndarray '
                                               'of predictions\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.array_equal(np.unique(test_predictions), '
                                               'np.array([0, 1])) # must be '
                                               'binary labels (0 or 1) and not '
                                               'probabilities\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> len(test_predictions) == '
                                               '1000 # must be the right '
                                               'number of predictions\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
