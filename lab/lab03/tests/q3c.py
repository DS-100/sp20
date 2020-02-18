test = {   'name': 'q3c',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> import matplotlib ;\n'
                                               '>>> '
                                               'np.alltrue(np.array([l.get_text() '
                                               'for l in '
                                               'ax_3c.xaxis.get_ticklabels()]) '
                                               '== days)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> import matplotlib ;\n'
                                               '>>> bars = [rect.get_height() '
                                               'for rect in '
                                               'ax_3c.get_children() \n'
                                               '...         if '
                                               'isinstance(rect, '
                                               'matplotlib.patches.Rectangle) '
                                               'and rect.get_x() != 0.0\n'
                                               '...        ];\n'
                                               '>>> '
                                               'np.allclose(np.array(bars)[-7:], '
                                               "calls['Day'].value_counts()[days].values)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
