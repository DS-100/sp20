test = {   'name': 'q1a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> "|" not in regx1\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> re.search(regx1, '
                                               '"abc").group()\n'
                                               "'abc'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> re.search(regx1, '
                                               '"abcde").group()\n'
                                               "'abcde'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> re.search(regx1, '
                                               '"abcdefg").group()\n'
                                               "'abcdefg'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> re.search(regx1, "c abc") '
                                               'is None\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
