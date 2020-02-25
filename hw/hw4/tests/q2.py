test = {   'name': 'q2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> sources = '
                                               "trump['source'].value_counts();\n"
                                               ">>> sources['Twitter for "
                                               "iPhone'] == 7758\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sources = '
                                               "trump['source'].value_counts();\n"
                                               ">>> sources['Twitter for "
                                               "Android'] == 1982\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "np.all(~trump['source'].str.contains('<'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(~(trump['source'] "
                                               "== ''))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
