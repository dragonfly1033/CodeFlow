import CodeFlowInterpreter
import CodeFlowTest


a = 9

b = 8

print(a+b)

c = 'hey'

d = a+b

print(c, d)

g = input('whats your name: ')

while g == 'me':
    while g == 'you':
        print('no')

for i in range(3):
    pass

CodeFlowInterpreter.Flow(__file__)
# CodeFlowTest.Flow(__file__)
#input()
