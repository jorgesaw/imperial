'''
Created on 27/09/2015

@author: jorgesaw
'''

lstNum = [1,4,5,8]

lstNumCompletos = []

numInicio = 1
numFinal = 9

for num in lstNum:
    
    for i in range(num - numInicio - 1):
        lstNumCompletos.append(0)
        
    lstNumCompletos.append(num)
    
    numInicio = num
    
for i in range(numFinal - numInicio):
        lstNumCompletos.append(0)
    
print(lstNumCompletos)