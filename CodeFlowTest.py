from re import findall, sub

def preParse(lines):
  clean = []
  indents = []

  for no, rawLine in list(enumerate(lines))[1:-1]:
    if rawLine.strip() == '':
      indents.append('')
    else:
      line = sub(r"\\n|\"|'", '', repr(rawLine))
      clean.append(sub('^[ ]*', '', line))
      line = line.replace(' ',r'\s')
      leadSpace = findall(r'^[\\s]*[\\t]*', line)
      indents.append(leadSpace[0])
  
  return clean, indents
      

def parse(lines):
  unclosed = {}

  for no, rawLine in enumerate(lines):
    line = rawLine.strip()
    fors = findall(r'for (\w+\s*,?\s*\w*) in (enumerate\((.+)\))?(?:range\((.+)\))?(.+)?:', line)
    whiles = findall(r'while\s+(.+):', line)
    ifs = findall(r'(if|elif|else)(?:\s*\(?(.+)\)?\s*:)', line)
    prints = findall(r'print\((.*)\)', line)
    functions = findall(r'def\s+(\w+)\((.*)\):', line)
    imports = findall(r'import (.+)', line)
    inputs = findall(r'input\((.*)\)', line)
    defVars = findall(r'(\w+)\s*=\s*([^=]+)', line)
    #print(f'fors: {fors}')
    #print(f'whiles: {whiles}')
    #print(f'ifs: {ifs}')
    #print(f'prints: {prints}')
    #print(f'functions: {functions}')
    #print(f'imports: {imports}')
    #print(f'inputs: {inputs}')
    #print(f'defVars: {defVars}')
    #print()
    if(fors):
      pass
    elif(whiles):
      pass
    elif(ifs):
      pass
    elif(prints):
      pass
    elif(functions):
      pass
    elif(imports):
      pass
    elif(inputs):
      pass
    elif(defVars):
      pass
    else:
      other = [line]

def Flow():
  with open('CodeFlowImport.py', 'r') as f:
    cont = f.readlines()
    clean, indents = preParse(cont)
    parse(clean)

nodeVals = {'fors': 3, 'whiles': 1, 'ifs': 1, 'prints': 1, 'functions': 1, 'imports': 1, 'inputs': 2, 'defVars': 1, 'other': 1}

lineInfo = []

Flow()
    
