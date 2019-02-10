'''
Created on 03 feb 2019

@author: pasteris
'''


#-------------
listOfSymbolsToAdd=['3','4','5','6','7','8']

listOfWords0=[]
listOfWords1=['12','21']
listOfSymbolsToRepl=['1','2']

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

#---------------------------------------------
#---------------------------------------------
print('----------------------------')
listOfSymbols=   ['1','2','3','4','5','6','7','8']
listOfNewSymbols=['P','A','S','T','E','R','I','S']
listtOfAnagrams =[]

for el in listOfWords1:
    curWord=el
    print(curWord)
    for indSymb in range(len(listOfSymbols)):
        oldSymb= listOfSymbols[indSymb]
        newSymb= listOfNewSymbols[indSymb]
        
        #print(oldSymb, newSymb)
        curWord=curWord.replace(oldSymb, newSymb)
    
    listtOfAnagrams.append(curWord)

tot=len(listtOfAnagrams)
c=0
for an in listtOfAnagrams:
    c+=1
    print(c,'/',tot, '  ',an)
    if c % 100 ==0:
        input("Press Enter to continue ...")

     
 
