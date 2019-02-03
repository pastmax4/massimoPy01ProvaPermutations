'''
Created on 03 feb 2019

@author: pasteris
'''

listOfSymbolsToAdd=['C','D','E']

#-------------
listOfWords0=[]
listOfWords1=['AB','BA']
listOfSymbolsToRepl=['A','B']

def ConstructWord02(newS):
    #Copy 
    listOfWords0.clear()
    for ind in range(len(listOfWords1)):
        listOfWords0.append(listOfWords1[ind])
    listOfWords1.clear()
 
    #Add new Symbol
    for ind in range(len(listOfWords0)):
        myWord0=listOfWords0[ind]
        listOfWords1.append(newS+myWord0)
    
    #Substitude of Symbol
    for indR in range(len(listOfSymbolsToRepl)):
        for ind in range(len(listOfWords0)):
            myWord0=listOfWords0[ind]
            myWord1=myWord0.replace(listOfSymbolsToRepl[indR], newS)
            listOfWords1.append(listOfSymbolsToRepl[indR]+myWord1)

    if len(listOfSymbolsToAdd)==0:
        return 
    else:  
        myNextSymbol=listOfSymbolsToAdd[0]
        listOfSymbolsToAdd.pop(0)
        listOfSymbolsToRepl.append(newS)
        ConstructWord02( myNextSymbol )
        
    

print('------')
mySymbol=listOfSymbolsToAdd[0]
listOfSymbolsToAdd.pop(0)
ConstructWord02(mySymbol)

indC=0
for el in listOfWords1:
    indC=indC+1
    print(indC,el)






