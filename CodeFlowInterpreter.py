import re
import CodeFlowDraw

sequence = {}

def Eval(list):
    # FORMAT: {tempName: [[whitespace],[start, end],extra info], etc.}
    openConstructs = {}
    index = 0
    sequenced={}
    for i in list:
        if(i[0] == '#'):
            continue
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
                cont = list[openConstructs[x][1][0]+1:openConstructs[x][1][1]+1]
                openConstructs[x].insert(1, cont)
                if('function' in x):
                    sequenced['function'+str(index)] = openConstructs[x][1:]
                elif('forr' in x):
                    sequenced['forr'+str(index)] = openConstructs[x][1:]
                elif('fori' in x):
                    sequenced['foris'+str(index)] = openConstructs[x][1:]
                elif('while' in x):
                    sequenced['whiles'+str(index)] = openConstructs[x][1:]
                elif('if' in x):
                    sequenced['ifs'+str(index)] = openConstructs[x][1:]
                toPop.append(x)

        for q in toPop:
            openConstructs.pop(q, '')

        if(len(openConstructs) == 0):
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
                sequenced['prints'+str(index)] = printMatches
                occ = True

            if(len(defvarMatches) == 1):
                defvarMatches = defvarMatches[0]
                sequenced['defvars'+str(index)] = [defvarMatches[0],
                                                   defvarMatches[1]]
                occ = True

            if(len(inputMatches) == 1):
                inputMatches = inputMatches[0]
                occ = True
                sequenced['inputs'+str(index)] = inputMatches

            if(len(importMatches) == 1):
                importMatches = importMatches[0]
                sequenced['imports'+str(index)] = importMatches
                occ = True

            if(not occ):
                if(i != '\n'):
                    sequenced['other'+str(index)] = i

        index += 1

    return sequenced


def embedCheck(d):

    if('for' in str(d)):
        for i in d:
            if('for' in i):
                if(type(d[i][0]).__name__ == 'list'):
                    d[i][0] = Eval(d[i][0])
                    embedCheck(d[i][0])
                else:
                    return True
    if('function' in str(d)):
        for i in d:
            if('function' in i):
                if(type(d[i][0]).__name__ == 'list'):
                    d[i][0] = Eval(d[i][0])
                    embedCheck(d[i][0])
                else:
                    return True
    if('while' in str(d)):
        for i in d:
            if('while' in i):
                if(type(d[i][0]).__name__ == 'list'):
                    d[i][0] = Eval(d[i][0])
                    embedCheck(d[i][0])
                else:
                    return True
    if('if' in str(d)):
        for i in d:
            if('if' in i):
                if(type(d[i][0]).__name__ == 'list'):
                    d[i][0] = Eval(d[i][0])
                    embedCheck(d[i][0])
                else:
                    return True


def Flow(file):
    global sequence
    with open(file, 'r') as f:
        list = f.readlines()
    sequence = Eval(list)
    embedCheck(sequence)
    print(sequence)
    CodeFlowDraw.Generate(sequence)

            # CodeFlowDraw.Generate(e)

