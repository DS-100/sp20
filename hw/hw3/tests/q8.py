test = {   'name': 'q8',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> runtimeRatingsDf.shape == '
                                               '(25, 4)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'set(runtimeRatingsDf.columns) '
                                               "== set(['runtime_bin', "
                                               "'avg_rating', 'avg_num_votes', "
                                               "'total'])\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'runtimeRatingsDf["runtime_bin"].min() '
                                               '== 50.0\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'runtimeRatingsDf["runtime_bin"].max() '
                                               '== 470.0\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
