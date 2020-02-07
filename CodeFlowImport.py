import CodeFlowInterpreter
import CodeFlowTest


def function3(a, b):
    summ = a+b
    print(summ)


a = 3  # int(input('Enter number: '))

b = 9

list = []

for i in range(5):
    pass

for i in list:
    pass

while False:
    pass

if(b == 4):
    pass


function3(a, b)


CodeFlowInterpreter.Flow(__file__)
input()
# CodeFlowTest.run(__file__)
