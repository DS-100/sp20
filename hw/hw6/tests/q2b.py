test = {   'name': 'q2b',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "sum(training_data['Fireplace_Qu'] "
                                               "== 'No Fireplace') == 975 # "
                                               "Make sure you've replaced all "
                                               "the missing values with 'No "
                                               "Fireplace'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sum(training_data.loc[:, '
                                               "'Fireplace_Qu'].isnull() == 0) "
                                               '== 1998 # Make sure you '
                                               "haven't introduced anything "
                                               'strange\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sum(training_data.loc[:, '
                                               "'Fireplace_Qu'] == "
                                               "'Excellent') == 30\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
