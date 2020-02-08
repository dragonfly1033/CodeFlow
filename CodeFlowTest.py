from CodeFlowInterpreter import Eval

dict = {   'imports0': 'CodeFlowInterpreter',
    'imports1': 'CodeFlowTest',
    'function13': [[
    '    for i in range(5):\n',
    "        print('hey')\n",
    '        for ii in range(7):\n',
    '            pass\n', 
    '    if(a+b == 5):\n',
    "        print('hey')\n", 
    '    elif(a+b == 6):\n',
    "        print('no')\n", '\n'],
     [4, 13], 'funtionn', 'a, b'],
    'whiles17': [[' pass\n', '\n'], 
    [15, 17], 'False'], 
    'other19': 'CodeFlowInterpreter.Flow(__file__)\n', 
    'other20': '# CodeFlowTest.Flow(__file__)\n', 
    'inputs21': ''}
                                                                                



def c(d):

    if('for' in str(d)):
        for i in d:
            if('for' in i):
                if(type(d[i][0]).__name__ == 'list'):
                    d[i][0] = Eval(d[i][0])
                    c(d[i][0])
                else:
                    return True
    if('function' in str(d)):
        for i in d:
            if('function' in i):
                if(type(d[i][0]).__name__ == 'list'):
                    d[i][0] = Eval(d[i][0])
                    c(d[i][0])
                else:
                    return True
    if('while' in str(d)):
        for i in d:
            if('while' in i):
                if(type(d[i][0]).__name__ == 'list'):
                    d[i][0] = Eval(d[i][0])
                    c(d[i][0])
                else:
                    return True
    if('if' in str(d)):
        for i in d:
            if('if' in i):
                if(type(d[i][0]).__name__ == 'list'):
                    d[i][0] = Eval(d[i][0])
                    c(d[i][0])
                else:
                    return True




#{'prints0': "'hey'", 'forr3': [['        pass\n', '\n'], [1, 3], 'ii', '6']}

c(dict)

#{'forr1': [['    print("hey")', '    for ii in range(6):', '        pass'], [4,8], 'i', '5']}
#{'forr1': [{'print1': 'hey', 'forr2': [['        pass', '\n'], [1, 3], 'ii', '6']}, [4, 8], 'i', '5']}
#{'forr1': [{'print1': 'hey', 'forr2': [{'other1': '        pass'}, [1, 3], 'ii', '6']}, [4, 8], 'i', '5']}
