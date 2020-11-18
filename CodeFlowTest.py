from re import findall, sub

def preParse(lines):
  global indents
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
    found = {}
    found['fors'] = findall(r'for (\w+\s*,?\s*\w*) in (enumerate\((.+)\))?(?:range\((.+)\))?(.+)?:', line)
    found['whiles'] = findall(r'while\s+(.+):', line)
    found['ifs'] = findall(r'(if|elif|else)(?:\s*\(?(.+)\)?\s*:)', line)
    found['prints'] = findall(r'print\((.*)\)', line)
    found['functions'] = findall(r'def\s+(\w+)\((.*)\):', line)
    found['imports'] = findall(r'import (.+)', line)
    found['inputs'] = findall(r'input\((.*)\)', line)
    found['defVars'] = findall(r'(\w+)\s*=\s*([^=]+)', line)
    found['others'] = []
    if(sum([len(i) for i in found.values()]) == 0):
      found['others'] = [line]
    construct = [i for i in found.values() if i][0][0]
    if isinstance(construct, tuple): construct = {'info': list(construct)}
    else: construct = {'info': [construct]}
    if found['fors']: construct['info'] = [i for i in construct['info'] if i]
    for i in found:
      if found[i]:
        construct['type'] = i[:-1]

    for i in indents:
      if construct['type'] in ['for', 'while', 'if', 'function']:
        pass
      construct['open'] = no
      construct['indent'] = indents[no]

    print(construct)

def Flow():
  with open('CodeFlowImport.py', 'r') as f:
    cont = f.readlines()
    clean, indents = preParse(cont)
    parse(clean)

nodeVals = {'fors': 3, 'whiles': 1, 'ifs': 1, 'prints': 1, 'functions': 1, 'imports': 1, 'inputs': 2, 'defVars': 1, 'other': 1}

lineInfo = []

curBlock = 0

Flow()
    
