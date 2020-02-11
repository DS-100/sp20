test = {   'name': 'q1a',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "sorted(list_files('data'))[0].name "
                                               "== 'bus.csv.bz2'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "get_file_size('data/bus.csv.bz2') "
                                               '== 113522\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "get_linecount_bz2('data/bus.csv.bz2') "
                                               '== 6254\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
