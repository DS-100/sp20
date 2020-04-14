test = {   'name': 'q4c',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'list(design_matrix(test).sum())[10:15]\n'
                                               '[290.0, 511.0, 699.0, 687.0, '
                                               '683.0]',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> 250 <= linear_rmse <= 260\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(linear_rmse, '
                                               '255.19147, 1e-4)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
