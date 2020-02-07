from tkinter import *


class Arrow:
    def __init__(self, canvas, fromm, to):
        canvas.create_line(fromm, to)


class Process:
    def __init__(self, canvas, value, gr):
        x = gr[0]
        y = gr[1]
        self.x1 = ((x+1)*25)+(x*140)
        self.y1 = ((y+1)*25)+(y*70)
        self.x2 = self.x1+140
        self.y2 = self.y1+70
       # self.arrow = Arrow()
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='blue')
        canvas.create_text(self.x1+70, self.y1+35, fill='white', text=value, anchor=CENTER)


class IO:
    def __init__(self, canvas, fromm, to):
        pass


class Decision:
    def __init__(self, canvas, fromm, to):
        pass


class Print:
    def __init__(self, canvas, value):
        pass


class DefineVariable:
    def __init__(self, canvas, name, value):
        pass


class IfStatement:
    def __init__(self, canvas, condition):
        pass


class Input:
    def __init__(self, canvas, question):
        pass


class Importt:
    def __init__(self, canvas, importt, gr):
        self.box = Process(canvas, importt, gr)


class ForLoopRange:
    def __init__(self, canvas, iterator, range):
        pass


class ForLoopIter:
    def __init__(self, canvas, iterator, iterable):
        pass


class WhileLoop:
    def __init__(self, canvas, condition):
        pass


class Function:
    def __init__(self, canvas, name):
        pass


class File:
    def __init__(self, canvas, name):
        pass


# sequence = {'import0': {'name': 'imp0'}, 'import1': {'name': 'imp1'}, 'import2': {'name': 'imp2'}, 'import3': {'name': 'imp3'}, 'import4': {'name': 'imp4'}, 'import5': {'name': 'imp5'}, 'import6': {'name': 'imp6'}, 'import7': {'name': 'imp7'}, 'import8': {'name': 'imp8'}, 'import9': {'name': 'imp9'}, 'import10': {'name': 'imp10'}, 'import11': {'name': 'imp11'}, 'import12': {'name': 'imp12'}, 'import13': {'name': 'imp13'}, 'import14': {'name': 'imp14'}, 'import15': {'name': 'imp15'}, 'import16': {'name': 'imp16'}, 'import17': {'name': 'imp17'}, 'import18': {'name': 'imp18'}, 'import19': {'name': 'imp19'}, 'import20': {'name': 'imp20'}, 'import21': {'name': 'imp21'}, 'import22': {'name': 'imp22'}, 'import23': {'name': 'imp23'}, 'import24': {'name': 'imp24'}, 'import25': {'name': 'imp25'}, 'import26': {'name': 'imp26'}, 'import27': {'name': 'imp27'}, 'import28': {
#     'name': 'imp28'}, 'import29': {'name': 'imp29'}, 'import30': {'name': 'imp30'}, 'import31': {'name': 'imp31'}, 'import32': {'name': 'imp32'}, 'import33': {'name': 'imp33'}, 'import34': {'name': 'imp34'}, 'import35': {'name': 'imp35'}, 'import36': {'name': 'imp36'}, 'import37': {'name': 'imp37'}, 'import38': {'name': 'imp38'}, 'import39': {'name': 'imp39'}, 'import40': {'name': 'imp40'}, 'import41': {'name': 'imp41'}, 'import42': {'name': 'imp42'}, 'import43': {'name': 'imp43'}, 'import44': {'name': 'imp44'}, 'import45': {'name': 'imp45'}, 'import46': {'name': 'imp46'}, 'import47': {'name': 'imp47'}, 'import48': {'name': 'imp48'}, 'import49': {'name': 'imp49'}, 'import50': {'name': 'imp50'}, 'import51': {'name': 'imp51'}, 'import52': {'name': 'imp52'}, 'import53': {'name': 'imp53'}, 'import54': {'name': 'imp54'}, 'import55': {'name': 'imp55'}}

def Generate(sequence):
    root = Tk()
    root.geometry('1180x785')

    c = Canvas(root)
    c.pack(fill='both', expand=True)

    yiter = 0
    xiter = 0
    for i in sequence['imports']:
        print(i)
        globals()[sequence['imports'][i]] = Importt(c, sequence['imports'][i], (xiter, yiter))

        yiter += 1
        if(yiter == 8):
            yiter = 0
            xiter += 1
    for i in sequence['imports']:
        print(i)
        globals()[sequence['imports'][i]] = Importt(c, sequence['imports'][i], (xiter, yiter))

        yiter += 1
        if(yiter == 8):
            yiter = 0
            xiter += 1

    root.mainloop()


def tutorial():
    pass


if __name__ == '__main__':
    tutorial()
