from tkinter import *


class Arrow:
    def __init__(self, canvas, gr, nextt):
        x1 = gr[0]
        y1 = gr[1]
        x2 = nextt[0]
        y2 = nextt[1]
        self.arrow = canvas.create_line(x1, y1, x2, y2, width=2, arrow=LAST)


class Process:
    def __init__(self, canvas, value, gr, nextt):
        self.x1, self.y1, self.x2, self.y2, self.n, self.s, self.w, self.e = gr_coord(gr)
        self.nx1, self.ny1, self.nx2, self.ny2, self.nn, self.ns, self.nw, self.ne = gr_coord(nextt)
        if(nextt[1] == 0):
            self.na = self.e
            self.nextt = self.nw
        else:
            self.na = self.s
            self.nextt = self.nn
        self.arrow = Arrow(canvas, self.na, self.nextt)
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='blue')
        canvas.create_text(self.x1+70, self.y1+35, fill='white', text=value, anchor=CENTER, width=120)


class IO:
    def __init__(self, canvas, value, io,  gr, nextt):
        self.x1, self.y1, self.x2, self.y2, self.n, self.s, self.w, self.e = gr_coord(gr)
        self.nx1, self.ny1, self.nx2, self.ny2, self.nn, self.ns, self.nw, self.ne = gr_coord(nextt)
        self.x1_mod = self.x1 + 10
        self.x2_mod = self.x2 - 10
        coords = [self.x1_mod, self.y1, self.x2, self.y1,
                  self.x2_mod, self.y2, self.x1, self.y2]
        if(nextt[1] == 0):
            self.na = self.e
            self.nextt = self.nw
        else:
            self.na = self.s
            self.nextt = self.nn
        self.arrow = Arrow(canvas, self.na, self.nextt)
        canvas.create_polygon(coords, fill='blue')
        canvas.create_text(self.x1+70, self.y1+35, fill='white', text=io+value, anchor=CENTER, width=120)


class Decision:
    def __init__(self, canvas, cond, gr, nextt):
        self.x1, self.y1, self.x2, self.y2, self.n, self.s, self.w, self.e = gr_coord(gr)
        self.nx1, self.ny1, self.nx2, self.ny2, self.nn, self.ns, self.nw, self.ne = gr_coord(nextt)
        self.x1_mod = self.x1 + 10
        self.x2_mod = self.x2 - 10
        coords = [self.n[0], self.n[1], self.e[0], self.e[1],
                  self.s[0], self.s[1], self.w[0], self.w[1], ]

        if(nextt[1] == 0):
            self.na = self.e
            self.nextt = self.nw
        else:
            self.na = self.s
            self.nextt = self.nn
        print(self.na, self.nextt)
        self.arrow = Arrow(canvas, self.na, self.nextt)
        canvas.create_polygon(coords, fill='blue')
        canvas.create_text(self.x1+70, self.y1+35, fill='white', text=cond, anchor=CENTER, width=120)


class Print:
    def __init__(self, canvas, value, gr, nextt):
        self.box = IO(canvas, value, 'OUTPUT ', gr, nextt)


class DefineVariable:
    def __init__(self, canvas, name, value, gr, nextt):
        self.box = Process(canvas, '{} = {}'.format(name, value), gr, nextt)


class IfStatement:
    def __init__(self, canvas, condition, gr, nextt):
        pass


class Input:
    def __init__(self, canvas, question, gr, nextt):
        self.box = IO(canvas, question, 'INPUT ', gr, nextt)


class Importt:
    def __init__(self, canvas, importt, gr, nextt):
        self.box = Process(canvas, importt, gr, nextt)


class ForLoopRange:
    def __init__(self, canvas, iterator, rangee, gr, nextt):
        self.box = Decision(canvas, '{} <= {}'.format(iterator, int(rangee)-1), gr, nextt)


class ForLoopIter:
    def __init__(self, canvas, iterator, iterable, gr, nextt):
        self.box = Decision(canvas, 'End of {}?'.format(iterable), gr, nextt)


class WhileLoop:
    def __init__(self, canvas, condition, gr, nextt):
        self.box = Decision(canvas, condition, gr, nextt)


class Function:
    def __init__(self, canvas, name, gr, nextt):
        pass


class Other:
    def __init__(self, canvas, name, gr, nextt):
        self.box = Process(canvas, name, gr, nextt)


class File:
    def __init__(self, canvas, name, gr, nextt):
        pass

def gr_coord(gr):
    x = gr[0]
    y = gr[1]
    x1 = ((x+1)*gap)+(x*140)
    y1 = ((y+1)*gap)+(y*70)
    x2 = x1+140
    y2 = y1+70
    n = (x1 + 70, y1)
    w = (x1, y1 + 35)
    s = (x1 + 70, y2)
    e = (x2, y1 + 35)

    return x1, y1, x2, y2, n, s, w, e

# sequence = {'import0': {'name': 'imp0'}, 'import1': {'name': 'imp1'}, 'import2': {'name': 'imp2'}, 'import3': {'name': 'imp3'}, 'import4': {'name': 'imp4'}, 'import5': {'name': 'imp5'}, 'import6': {'name': 'imp6'}, 'import7': {'name': 'imp7'}, 'import8': {'name': 'imp8'}, 'import9': {'name': 'imp9'}, 'import10': {'name': 'imp10'}, 'import11': {'name': 'imp11'}, 'import12': {'name': 'imp12'}, 'import13': {'name': 'imp13'}, 'import14': {'name': 'imp14'}, 'import15': {'name': 'imp15'}, 'import16': {'name': 'imp16'}, 'import17': {'name': 'imp17'}, 'import18': {'name': 'imp18'}, 'import19': {'name': 'imp19'}, 'import20': {'name': 'imp20'}, 'import21': {'name': 'imp21'}, 'import22': {'name': 'imp22'}, 'import23': {'name': 'imp23'}, 'import24': {'name': 'imp24'}, 'import25': {'name': 'imp25'}, 'import26': {'name': 'imp26'}, 'import27': {'name': 'imp27'}, 'import28': {
#     'name': 'imp28'}, 'import29': {'name': 'imp29'}, 'import30': {'name': 'imp30'}, 'import31': {'name': 'imp31'}, 'import32': {'name': 'imp32'}, 'import33': {'name': 'imp33'}, 'import34': {'name': 'imp34'}, 'import35': {'name': 'imp35'}, 'import36': {'name': 'imp36'}, 'import37': {'name': 'imp37'}, 'import38': {'name': 'imp38'}, 'import39': {'name': 'imp39'}, 'import40': {'name': 'imp40'}, 'import41': {'name': 'imp41'}, 'import42': {'name': 'imp42'}, 'import43': {'name': 'imp43'}, 'import44': {'name': 'imp44'}, 'import45': {'name': 'imp45'}, 'import46': {'name': 'imp46'}, 'import47': {'name': 'imp47'}, 'import48': {'name': 'imp48'}, 'import49': {'name': 'imp49'}, 'import50': {'name': 'imp50'}, 'import51': {'name': 'imp51'}, 'import52': {'name': 'imp52'}, 'import53': {'name': 'imp53'}, 'import54': {'name': 'imp54'}, 'import55': {'name': 'imp55'}}

def Make(root, c, sequence, Xiter, Yiter, Iter, i):
    def increment(Xiter, Yiter, Iter):
        Yiter += 1
        Iter += 1
        if(Yiter == 7):
            Yiter = 0
            Xiter += 1
        return Xiter, Yiter, Iter

    if('import' in i):
        nx, ny, nn = increment(Xiter, Yiter, Iter)
        nextt = (nx, ny)
        globals()['box'+str(Iter)] = Importt(c, sequence[i], (Xiter, Yiter), nextt)
    elif('print' in i):
        nx, ny, nn = increment(Xiter, Yiter, Iter)
        nextt = (nx, ny)
        globals()['box'+str(Iter)] = Print(c, sequence[i], (Xiter, Yiter), nextt)
    elif('other' in i):
        nx, ny, nn = increment(Xiter, Yiter, Iter)
        nextt = (nx, ny)
        globals()['box'+str(Iter)] = Other(c, sequence[i], (Xiter, Yiter), nextt)
    elif('defvar' in i):
        nx, ny, nn = increment(Xiter, Yiter, Iter)
        nextt = (nx, ny)
        if('input' in sequence[i][1]):
            globals()['box'+str(Iter)] = Input(c, sequence[i][0], (Xiter, Yiter), nextt)
            Yiter -= 1
        else:
            globals()['box'+str(Iter)] = DefineVariable(c, sequence[i][0], sequence[i][1], (Xiter, Yiter), nextt)
    elif('while' in i):
        nx, ny, nn = increment(Xiter, Yiter, Iter)
        nextt = (nx, ny)
        globals()['box'+str(Iter)] = WhileLoop(c, sequence[i][2], (Xiter, Yiter), nextt)
        Xiter, Yiter, Iter = increment(Xiter, Yiter, Iter)
        for ii in sequence[i][0]:
            Xiter, Yiter, Iter = Make(root, c, sequence[i][0], Xiter, Yiter, Iter, ii)
        Yiter -= 1

    elif('forr' in i):
        nx, ny, nn = increment(Xiter, Yiter, Iter)
        nextt = (nx, ny)
        globals()['box'+str(Iter)] = DefineVariable(c, sequence[i][2], '0', (Xiter, Yiter), nextt)
        Xiter, Yiter, Iter = increment(Xiter, Yiter, Iter)
        globals()['box'+str(Iter)] = ForLoopRange(c, sequence[i][2], sequence[i][3], (Xiter, Yiter), nextt)
        Xiter, Yiter, Iter = increment(Xiter, Yiter, Iter)
        for ii in sequence[i][0]:
            Xiter, Yiter, Iter = Make(root, c, sequence[i][0], Xiter, Yiter, Iter, ii)
        globals()['box'+str(Iter)] = Process(c, '{} += 1'.format(sequence[i][2]), (Xiter, Yiter), nextt)
        Yiter -= 1
    elif('fori' in i):
        nx, ny, nn = increment(Xiter, Yiter, Iter)
        nextt = (nx, ny)
        globals()['box'+str(Iter)] = DefineVariable(c, sequence[i][2], 'Next Item in {}'.format(sequence[i][3]), (Xiter, Yiter), nextt)
        Xiter, Yiter, Iter = increment(Xiter, Yiter, Iter)
        globals()['box'+str(Iter)] = ForLoopIter(c, sequence[i][2], sequence[i][3], (Xiter, Yiter), nextt)
        Xiter, Yiter, Iter = increment(Xiter, Yiter, Iter)
        for ii in sequence[i][0]:
            Xiter, Yiter, Iter = Make(root, c, sequence[i][0], Xiter, Yiter, Iter, ii)
        globals()['box'+str(Iter)] = Process(c, '{} += 1'.format(sequence[i][2]), (Xiter, Yiter), nextt)
        Yiter -= 1

    Xiter, Yiter, Iter = increment(Xiter, Yiter, Iter)

    return Xiter, Yiter, Iter


def Generate(sequence):
    root = Tk()
    root.geometry('1180x810')

    c = Canvas(root)
    c.pack(fill='both', expand=True)

    Xiter = 0
    Yiter = 0
    Iter = 0
    for i in sequence:
        Xiter, Yiter, Iter = Make(root, c, sequence, Xiter, Yiter, Iter, i)

    root.mainloop()


def tutorial():
    pass


gap = 40

if __name__ == '__main__':
    tutorial()
