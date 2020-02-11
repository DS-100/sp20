test = {   'name': 'q1b',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "head_bz2('data/bus.csv.bz2')[0] "
                                               '== \\\n'
                                               '...     b\'"business id '
                                               'column","name","address","city","state","postal_code","latitude","longitude","phone_number"\\n\'\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "head_bz2('data/bus.csv.bz2', "
                                               '7)[-1] == \\\n'
                                               '...     b\'"100036","Hula '
                                               'Truck (#2)","2 Marina '
                                               'Blvd","San '
                                               'Francisco","CA","94123","-9999","-9999","-9999"\\n\'\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
