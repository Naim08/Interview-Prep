import unittest

'''
Part 1: Write a function called "changesNeeded" that returns the changes
needed to transform obj1 to obj2
'''


# def changesNeeded(obj1, obj2):

#     diff = {}

#     for key, value in obj2.items():
#         if key in obj1:
#             if value != obj1[key]:
#                 diff[key] = value
#         else:
#             diff[key] = value

#     for key, value in obj1.items():
#         if key not in obj2:
#             diff[key] = None


#     return diff


class TestPart1(unittest.TestCase):
    def test_property_changed(self):
        obj1 = {
            'color': 'red',
            'number': 1,
            }
        obj2 = {
            'color': 'red',
            'number': 2,
            }
        expected = {
            'number': 2,
            }
        self.assertEqual(changesNeeded(obj1, obj2), expected)
    
    def test_property_added(self):
        obj1 = {
            'color': 'red',
            'number': 1
            }
        obj2 = {
            'color': 'red',
            'number': 2,
            'rainbows': True,
            }
        expected = {
            'number': 2,
            'rainbows': True,
            }
        self.assertEqual(changesNeeded(obj1, obj2), expected)
    
    def test_property_removed(self):
        obj1 = {
            'color': 'red',
            'number': 1
            }
        obj2 = {
            'color': 'red',
            }
        expected = {
            'number': None,
            }
        self.assertEqual(changesNeeded(obj1, obj2), expected)


'''
 Part 2: Modify the changesNeeded function to accept trees as arguments where
 child nodes are specified by the "children" key. Use the index of the child
 as the comparison key. i.e. always compare cur.children[0] to
 target.children[0], cur.children[1] to target.children[1], etc.
'''


class TestPart2(unittest.TestCase):
    def test_nested_children(self):
        obj1 = {
            'number': 1,
            'children': [
                {
                    'color': 'red',
                    'children': [
                        {'state': 'ca'},
                        ],
                    },
                {
                    'color': 'blue',
                    }
                ],
            }
        obj2 = {
            'number': 1,
            'color': 'blue',
            'rainbows': True,
            'children': [
                {
                    'color': 'red',
                    'children': [
                        {'state': 'ca'},
                        ],
                    },
                {
                    'color': 'blue',
                    'number': 1,
                    'children': [
                        {'state': 'tx'}
                        ],
                    }, {
                    'color': 'green'
                    }
                ],
            }
        expected = {
            'children': [
                {
                    'children': [
                        {}
                        ]
                    },
                {
                    'number': 1,
                    'children': [
                        {'state': "tx"},
                        ]
                    },
                {
                    'color': "green"
                    }
                ],
            'color': "blue",
            'rainbows': True
            }
        self.assertEqual(changesNeeded(obj1, obj2), expected)


def changesNeeded(obj1, obj2):
    diff = {}
    
    diff = helper(obj1, obj2, diff)
    
    return diff


'''
- {'children': [{'children': [{'state': 'ca'}], 'color': 'red'},
+ {'children': [{'children': [{}]},


-               {'children': [{'state': 'tx'}], 'color': 'blue', 'number': 1},
?                                              -----------------


+               {'children': [{'state': 'tx'}], 'number': 1},
                {'color': 'green'}],

'''

def helper(obj1, obj2, diff):
    
    for key, value in obj2.items():
        
        if key in obj1:
            if key == 'children' and len(obj2[key]) != 0:
                for index, child in enumerate(value):
                    if index >= len(obj1[key]):
                        #print(key, child)
                        diff.append(child)
                    else:
                        if type(diff) == list:
                            diff.append(helper(obj1[key][index], child, [{}]))
                        else:
                            diff[key] = helper(obj1[key][index], child, [{}])
            
            elif value != obj1[key]:
                diff[key] = value
        
        else:
            print(key, value)
            print('onj1', obj1)
            print('obj2', obj2)
            diff[key] = value
            #print(diff)
    
    for key, value in obj1.items():
        if key not in obj2:
            diff[key] = None
    
    return diff

unittest.main(exit = False)