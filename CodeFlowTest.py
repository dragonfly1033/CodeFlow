
dict = {'imports0': 'CodeFlowInterpreter', 'imports1': 'CodeFlowTest', 'defvars4': ['a', '9'], 'defvars6': ['b', '8'], 'prints8': 'a+b', 'defvars10': ['c', "'hey'"], 'defvars12': [
    'd', 'a+b'], 'prints14': 'c, d', 'defvars16': ['g', "input('whats your name: ')"], 'inputs16': "'whats your name: '", 'other19': 'CodeFlowInterpreter.Flow(__file__)\n'}


keys = list(dict.keys())

for i in dict:
    if('input' in dict[i][1]):
        print(keys[keys.index(i)+1])