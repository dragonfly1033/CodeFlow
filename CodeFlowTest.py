
dict = {'imports0': 'CodeFlowInterpreter', 'imports1': 'CodeFlowTest',
 'function7': [['def function3(a, b):\n', '    summ = a+b\n', '    print(summ)\n'], [4, 7], 'function3', 'a, b'],
  'defvars9': ['a', '3  '], 'defvars11': ['b', '9'], 'defvars13': ['list', '[]'],
   'forr17': [['for i in range(5):\n', '    pass\n'], [15, 17], 'i', '5'],
    'foris20': [['for i in list:\n', '    pass\n'], [18, 20], 'i', 'list'],
     'whiles23': [['while False:\n', '    pass\n'], [21, 23], 'False'],
      'ifs26': [['if(b == 4):\n', '    pass\n'], [24, 26], 'b == 4)'],
       'other28': 'function3(a, b)\n',
        'other31': '#CodeFlowInterpreter.Flow(__file__)\n',
         'other32': 'CodeFlowTest.Flow(__file__)\n',
          'inputs33': ''}

# dict = str(dict.values())

# print(dict)
my_list = list(dict.keys())
bad = ['function', 'def', 'forr', 'fori', 'while', 'if']
s = set(my_list)-{i for e in bad for i in my_list if e in i}
print(len(s))
