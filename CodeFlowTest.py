from re import findall as find

def parse(lines):
  unclosed = {}

  for no, rawLine in enumerate(lines):
    line = rawLine.strip()
    fors = find(r'for (\w+\s*,?\s*\w*) in (enumerate\((.+)\))?(?:range\((.+)\))?(.+)?:', line)
    whiles = find(r'while\s+(.+):', line)
    ifs = find(r'(if|elif|else)(?:\s*\(?(.+)\)?\s*:)', line)
    prints = find(r'print\((.*)\)', line)
    functions = find(r'def\s+(\w+)\((.*)\):', line)
    imports = find(r'import (.+)', line)
    inputs = find(r'input\((.*)\)', line)
    defVars = find(r'(\w+)\s*=\s*(.+)', line)
