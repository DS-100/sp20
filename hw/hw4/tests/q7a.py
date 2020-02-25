test = {   'name': 'q7a',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> bool(re.search(rt_re, 'hi "
                                               "rt hello'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> bool(re.search(rt_re, '
                                               "'rt'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bool(re.search(rt_re, 'rt "
                                               "hello'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> bool(re.search(rt_re, '
                                               "'hello rt'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> bool(re.search(rt_re, '
                                               "'rthello')) == False\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> bool(re.search(rt_re, '
                                               "'hellort')) == False\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> bool(re.search(rt_re, '
                                               "':rt'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> bool(re.search(rt_re, '
                                               "'rt:'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'bool(re.search(hash_link_re, '
                                               "'#hello'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'bool(re.search(hash_link_re, '
                                               "'hello#')) == False\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'bool(re.search(hash_link_re, '
                                               "'#')) == False\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'bool(re.search(hash_link_re, '
                                               "'#!')) == False\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'bool(re.search(hash_link_re, '
                                               "'#HELLO'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'bool(re.search(hash_link_re, '
                                               "'http'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'bool(re.search(hash_link_re, '
                                               "'')) == False\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'bool(re.search(hash_link_re, '
                                               "'httphttp'))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
