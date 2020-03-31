test = {   'name': 'q1b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'len(find_rich_neighborhoods(training_data, '
                                               '5, np.median)) == 5\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'isinstance(rich_neighborhoods, '
                                               'list)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'all([isinstance(neighborhood, '
                                               'str) for neighborhood in '
                                               'rich_neighborhoods])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> set(rich_neighborhoods) == '
                                               "set(['StoneBr', 'NridgHt', "
                                               "'NoRidge']) # Check to see if "
                                               'correct neighborhoods '
                                               'identified\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'set(find_rich_neighborhoods(training_data, '
                                               "2, np.min)) == set(['GrnHill', "
                                               "'NoRidge'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
