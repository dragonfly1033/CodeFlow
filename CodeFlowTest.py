import re
import CodeFlowDraw

functions = {}
forrs = {}
foris = {}
whiles = {}
ifs = {}
prints = {}
defvars = {}
inputs = {}
imports = {}
other = {}


def Eval(list):
    # FORMAT: {tempName: [[whitespace],[start, end],extra info], etc.}
    openConstructs = {}
    index = 0
    for i in list:
        i.replace('elif', 'if')
        funcMatches = re.findall(r'^(\s*)def (\w+)\(([a-zA-z0-9,_ ]*)\):', i)
        forrMatches = re.findall(r'^(\s*)for (\w+) in range\((\d+)\):', i)
        foriMatches = re.findall(r'^(\s*)for (\w+) in (\w+):', i)
        whileMatches = re.findall(r'^(\s*)while (.+):', i)
        ifMatches = re.findall(r'(\s*)if\s?\(?(.+)\)?:', i)
        printMatches = re.findall(r"print\((.*)\)", i)
        defvarMatches = re.findall(
            r'(\w+)\s?=\s?([a-zA-z0-9 _\'\[\]\{\}:@\~<>?,\./!"%\^&\*\(\)\-\+]+)', i)
        inputMatches = re.findall(r'input\((.*)\)', i)
        importMatches = re.findall(r'import (\w+)', i)
        currIndent = re.findall(r'^(\s*)\w', i)

        if len(currIndent) != 0:
            currIndent = currIndent[0]
        else:
            currIndent.append('')
            currIndent = currIndent[0]

        toPop = []
        for x in openConstructs:
            if(len(currIndent) <= len(openConstructs[x][0][0])):
                openConstructs[x][1].append(index)
                if('function' in x):
                    functions[openConstructs[x][2]] = openConstructs[x][1:]
                elif('forr' in x):
                    forrs['forr'+str(index)] = openConstructs[x][1:]
                elif('fori' in x):
                    foris['foris'+str(index)] = openConstructs[x][1:]
                elif('while' in x):
                    whiles['whiles'+str(index)] = openConstructs[x][1:]
                elif('if' in x):
                    ifs['ifs'+str(index)] = openConstructs[x][1:]
                toPop.append(x)
        for q in toPop:
            openConstructs.pop(q, '')
        occ = False
        if(len(funcMatches) == 1):
            funcMatches = funcMatches[0]
            openConstructs['function{}'.format(index)] = [[funcMatches[0]], [
                index], funcMatches[1], funcMatches[2]]
            occ = True

        if(len(forrMatches) == 1):
            forrMatches = forrMatches[0]
            openConstructs['forr{}'.format(index)] = [[forrMatches[0]], [
                index], forrMatches[1], forrMatches[2]]
            occ = True

        if(len(foriMatches) == 1):
            foriMatches = foriMatches[0]
            openConstructs['fori{}'.format(index)] = [[foriMatches[0]], [
                index], foriMatches[1], foriMatches[2]]
            occ = True

        if(len(whileMatches) == 1):
            whileMatches = whileMatches[0]
            openConstructs['while{}'.format(index)] = [[whileMatches[0]], [
                index], whileMatches[1]]
            occ = True

        if(len(ifMatches) == 1):
            ifMatches = ifMatches[0]
            openConstructs['if{}'.format(index)] = [
                [ifMatches[0]], [index], ifMatches[1]]
            occ = True

        if(len(printMatches) == 1):
            printMatches = printMatches[0]
            prints['prints'+str(index)] = printMatches
            occ = True

        if(len(defvarMatches) == 1):
            defvarMatches = defvarMatches[0]
            defvars['defvars'+str(index)] = [defvarMatches[0],
                                             defvarMatches[1]]
            occ = True

        if(len(inputMatches) == 1):
            inputMatches = inputMatches[0]
            occ = True
            inputs['inputs'+str(index)] = inputMatches

        if(len(importMatches) == 1):
            importMatches = importMatches[0]
            imports['imports'+str(index)] = importMatches
            occ = True

        if(not occ):
            if(i != '\n'):
                other['other'+str(index)] = i

        index += 1

    print('openConstructs: ', openConstructs)
    print('functions: ', functions)
    print('forrs: ', forrs)
    print('foris: ', foris)
    print('whiles: ', whiles)
    print('ifs: ', ifs)
    print('prints: ', prints)
    print('defvars: ', defvars)
    print('inputs: ', inputs)
    print('imports: ', imports)
    print('other: ', other)

    formatted = {'functions': functions, 'forrs': forrs, 'foris': foris, 'whiles': whiles, 'ifs': ifs,
                 'prints': prints, 'defvars': defvars, 'inputs': inputs, 'imports': imports, 'other': other}

    print('\n'+str(formatted))

    return formatted


def Flow(file):
    with open(file, 'r') as f:
        list = f.readlines()
    e = Eval(list)
    CodeFlowDraw.Generate(e)
