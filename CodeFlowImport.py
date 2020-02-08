import CodeFlowInterpreter
import CodeFlowTest


a = 9

b = 8

print(a+b)

c = 'hey'

d = a+b

print(c, d)


CodeFlowInterpreter.Flow(__file__)
# CodeFlowTest.Flow(__file__)
#input()
