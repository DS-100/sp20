test = {   'name': 'q1ci',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'print(list(ins_named.columns))\n'
                                               "['iid', 'date', 'score', "
                                               "'type', 'bid', 'timestamp', "
                                               "'year', 'Missing Score', "
                                               "'name', 'address']\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> len(ins_named) == '
                                               'len(ins)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "np.all(ins_named['date'].sort_values().values "
                                               '== '
                                               "ins['date'].sort_values().values)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
