test = {   'name': 'q5e',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(punct_re, str)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> re.search(punct_re, '
                                               "'this') is None\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> re.search(punct_re, 'this "
                                               "is ok') is None\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> re.search(punct_re, 'this "
                                               "is\\nok') is None\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> re.search(punct_re, 'this "
                                               "is not ok.') is not None\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> re.search(punct_re, '
                                               "'this#is#ok') is not None\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> re.search(punct_re, '
                                               "'this^is ok') is not None\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "trump['no_punc'].loc[800329364986626048] "
                                               "== 'i watched parts of  nbcsnl "
                                               'saturday night live last '
                                               'night  it is a totally one '
                                               'sided  biased show   nothing '
                                               'funny at all  equal time for '
                                               "us '\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "trump['no_punc'].loc[894620077634592769] "
                                               "== 'on  purpleheartday i thank "
                                               'all the brave men and women '
                                               'who have sacrificed in battle '
                                               'for this great nation   usa   '
                                               "https   t co qmfdlslp6p'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # If you fail these tests, '
                                               'you accidentally changed the '
                                               'text column;\n'
                                               '>>> '
                                               "trump['text'].loc[884740553040175104] "
                                               "== 'working hard to get the "
                                               'olympics for the united states '
                                               "(l.a.). stay tuned!'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
