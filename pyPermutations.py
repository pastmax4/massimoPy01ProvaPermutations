'''
Created on 11 feb 2019

@author: pasteris
'''

#-------------
# Example: listOfSymbolsToAdd=['3','4','5']

listOfSymbolsToAdd=[]
listOfWords0=[]
listOfWords1=['12','21']
listOfSymbolsToRepl=['1','2']



def ConstructWord02(newS):

    retList=[]
    #Copy in listOfWords0 from listOfWords1
    listOfWords0.clear()
    for ind in range(len(listOfWords1)):
        listOfWords0.append(listOfWords1[ind])
    listOfWords1.clear()
 
    #Add new input Symbol to old permutations
    #Example 3 ,1,2   3 ,2,1
    for ind in range(len(listOfWords0)):
        myWord0=listOfWords0[ind]
        listOfWords1.append(newS+myWord0)
    
    #substitute of Symbol: the new symbol is substituted
    #in all old permutations
    for indR in range(len(listOfSymbolsToRepl)):
        for ind in range(len(listOfWords0)):
            myWord0=listOfWords0[ind]
            myWord1=myWord0.replace(listOfSymbolsToRepl[indR], newS)
            listOfWords1.append(listOfSymbolsToRepl[indR]+myWord1)

    if len(listOfSymbolsToAdd)==0:
        #print('----40--> Fine recorsione')
        retList = listOfWords1[:]
        return retList
    else:  
        myNextSymbol=listOfSymbolsToAdd[0]
        #print('----44-->',myNextSymbol)
        listOfSymbolsToAdd.pop(0)
        listOfSymbolsToRepl.append(newS)
        
        ConstructWord02( myNextSymbol )


#----------------------------------------------
#----------------------------------------------
def constrPermutations(parInList):    
    # Call function for permutations
    
    global listOfWords0
    global listOfWords1
    #listOfSymbolsToAdd=[]
    listOfWords0.clear()
    listOfWords1.clear()
    listOfWords1=['12','21']

    #listOfSymbolsToRepl=['1','2']
    #print('---62-->',listOfWords0)
    #print('---63-->',listOfWords1)


    #--------    
    
    listOfSymbolsToAdd.clear()
    for el in parInList:
        listOfSymbolsToAdd.append(el)    
    
    mySymbol=listOfSymbolsToAdd[0]
    listOfSymbolsToAdd.pop(0)
    
    ConstructWord02(mySymbol)
    
    #for ell in listOfWords1:
    #    print(ell)
        
    return listOfWords1


#----------------------------------------------
#----------------------------------------------

def constrPermWords(inListWords, inListOfNewSymbols, inListOfOldSymbols):
    #esempio listOfNewSymbols=['P','A','S','T','E','R','I','S']
    listtOfAnagrams=[]
    for curWord in inListWords:
        for indSymb in range(len(inListOfNewSymbols)):
            oldSymb= inListOfOldSymbols[indSymb]
            newSymb= inListOfNewSymbols[indSymb]
            curWord=curWord.replace(oldSymb, newSymb)
            
        listtOfAnagrams.append(curWord)
    
    return listtOfAnagrams

#----------------------------------------------
#----------------------------------------------


def constrPermWords02(inListOfSymbols):
    # Replace numbers with letters
    
    # esempio inListOfSymbols=['M','A','S','S','I','M','O']
    listOfOldSymbols=[]
    listToUse=[]
    
    listOfNewSymbols=inListOfSymbols.copy()
    for ind in range(1,len(listOfNewSymbols)+1):
        listOfOldSymbols.append(str(ind))
        if ind>2:
            listToUse.append(str(ind))
        
    
    list01Per=constrPermutations(parInList=listToUse)
    
    listAnagr = constrPermWords(inListWords=list01Per, 
                                inListOfNewSymbols=listOfNewSymbols,
                                inListOfOldSymbols=listOfOldSymbols)
    
    

    return listAnagr
#----------------------------------------------
#----------------------------------------------



def clearFromListSomeWords(inListToClear,inListSymGroup):
    #listSymGroup=inListSymGroup
    listWordsGroup=constrPermWords02(inListOfSymbols=inListSymGroup)
    #print(listWordsGroup)
    
    for curWord in listWordsGroup:
        for curGroup in inListToClear:
            if curGroup in curWord:
                inListToClear.remove(curWord)
           
    return inListToClear

    
#----------------------------------------------
#----------------------------------------------
   
    
    
    
    
    
    


