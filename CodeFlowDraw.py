from tkinter import *


class Arrow:
    def __init__(self, canvas, gr):
        x1 =  gr
        #self.arrow = canvas.create_line(x1, y1, x2, y2, width=2)


class Process:
    def __init__(self, canvas, value, gr):
        x = gr[0]
        y = gr[1]
        self.x1 = ((x+1)*gap)+(x*140)
        self.y1 = ((y+1)*gap)+(y*70)
        self.x2 = self.x1+140
        self.y2 = self.y1+70
        self.n = (self.x1 + 70, self.y1)
        self.w = (self.x1, self.y1 + 35)
        self.s = (self.x1 + 70, self.y2)
        self.e = (self.x2, self.y1 + 35)
       # self.arrow = Arrow()
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='blue')
        canvas.create_text(self.x1+70, self.y1+35, fill='white', text=value, anchor=CENTER, width=120)


class IO:
    def __init__(self, canvas, value, io,  gr):
        x = gr[0]
        y = gr[1]
        self.x1 = ((x+1)*gap)+(x*140)
        self.y1 = ((y+1)*gap)+(y*70)
        self.x2 = self.x1+140
        self.y2 = self.y1+70
        self.x1_mod = self.x1 + 10
        self.x2_mod = self.x2 - 10
        self.n = (self.x1 + 70, self.y1)
        self.w = (self.x1, self.y1 + 35)
        self.s = (self.x1 + 70, self.y2)
        self.e = (self.x2, self.y1 + 35)
        coords = [self.x1_mod, self.y1, self.x2, self.y1,
                 self.x2_mod, self.y2, self.x1, self.y2]
       # self.arrow = Arrow()
        canvas.create_polygon(coords, fill='blue')
        canvas.create_text(self.x1+70, self.y1+35, fill='white', text=io+value, anchor=CENTER, width=120)


class Decision:
    def __init__(self, canvas, cond, gr):
        x = gr[0]
        y = gr[1]
        self.x1 = ((x+1)*gap)+(x*140)
        self.y1 = ((y+1)*gap)+(y*70)
        self.x2 = self.x1+140
        self.y2 = self.y1+70
        self.x1_mod = self.x1 + 10
        self.x2_mod = self.x2 - 10
        self.n = (self.x1 + 70, self.y1)
        self.w = (self.x1, self.y1 + 35)
        self.s = (self.x1 + 70, self.y2)
        self.e = (self.x2, self.y1 + 35)
        coords = [self.n[0], self.n[1], self.e[0], self.e[1], 
                self.s[0], self.s[1], self.w[0], self.w[1], ]
       # self.arrow = Arrow()
        canvas.create_polygon(coords, fill='blue')
        canvas.create_text(self.x1+70, self.y1+35, fill='white', text=cond, anchor=CENTER, width=120)


class Print:
    def __init__(self, canvas, value, gr):
        self.box = IO(canvas, value, 'OUTPUT ', gr)


class DefineVariable:
    def __init__(self, canvas, name, value, gr):
        self.box = Process(canvas, '{} = {}'.format(name, value), gr)


class IfStatement:
    def __init__(self, canvas, condition, gr):
        pass


class Input:
    def __init__(self, canvas, question, gr):
        self.box = IO(canvas, question, 'INPUT ', gr)


class Importt:
    def __init__(self, canvas, importt, gr):
        self.box = Process(canvas, importt, gr)

class ForLoopRange:
    def __init__(self, canvas, iterator, rangee, gr):
        self.box = Decision(canvas, '{} <= {}'.format(iterator, int(rangee)+1), gr)


class ForLoopIter:
    def __init__(self, canvas, iterator, iterable, gr):
        self.box = Decision(canvas, 'End of {}?'.format(iterable), gr)


class WhileLoop:
    def __init__(self, canvas, condition, gr):
        self.box = Decision(canvas, condition, gr)


class Function:
    def __init__(self, canvas, name, gr):
        pass


class Other:
    def __init__(self, canvas, name, gr):
        self.box = Process(canvas, name, gr)


class File:
    def __init__(self, canvas, name, gr):
        pass


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
        globals()['box'+str(Iter)] = Importt(c, sequence[i], (Xiter, Yiter))
    elif('print' in i):
        globals()['box'+str(Iter)] = Print(c, sequence[i], (Xiter, Yiter))
    elif('other' in i):
        globals()['box'+str(Iter)] = Other(c, sequence[i], (Xiter, Yiter))
    elif('defvar' in i):
        if('input' in sequence[i][1]):
            globals()['box'+str(Iter)] = Input(c, sequence[i][0], (Xiter, Yiter))
            Yiter-=1
        else:
            globals()['box'+str(Iter)] = DefineVariable(c, sequence[i][0], sequence[i][1], (Xiter, Yiter))
    elif('while' in i):
        globals()['box'+str(Iter)] = WhileLoop(c, sequence[i][2], (Xiter, Yiter))
        Xiter, Yiter, Iter = increment(Xiter, Yiter, Iter)
        for ii in sequence[i][0]:
            Xiter, Yiter, Iter = Make(root, c, sequence[i][0], Xiter, Yiter, Iter, ii)
        Yiter-=1
        
    elif('forr' in i):
        globals()['box'+str(Iter)] = DefineVariable(c, sequence[i][2], '0', (Xiter, Yiter))
        Xiter, Yiter, Iter = increment(Xiter, Yiter, Iter)
        globals()['box'+str(Iter)] = ForLoopRange(c, sequence[i][2], sequence[i][3], (Xiter, Yiter))
        Xiter, Yiter, Iter = increment(Xiter, Yiter, Iter)
        for ii in sequence[i][0]:
            Xiter, Yiter, Iter = Make(root, c, sequence[i][0], Xiter, Yiter, Iter, ii)
        Yiter-=1
    elif('fori' in i):
        globals()['box'+str(Iter)] = DefineVariable(c, sequence[i][2],'Next Item in {}'.format(sequence[i][3]), (Xiter, Yiter))
        Xiter, Yiter, Iter = increment(Xiter, Yiter, Iter)
        globals()['box'+str(Iter)] = ForLoopIter(c, sequence[i][2], sequence[i][3], (Xiter, Yiter))
        Xiter, Yiter, Iter = increment(Xiter, Yiter, Iter)
        for ii in sequence[i][0]:
            Xiter, Yiter, Iter = Make(root, c, sequence[i][0], Xiter, Yiter, Iter, ii)
        Yiter-=1
        
        
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
