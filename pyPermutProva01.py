'''
Created on 30 gen 2019

@author: mpasteri

https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/

'''

Keys=[]
N=4
jTot=1
TreeInd = 0

PermutationCode = {}
for i in range(N,-1,-1):

    print('---',i)
    jTot=jTot*i
    
    Fj=-1
    for j in range(0,jTot,1):      
        
        if(j%i == 0):
            Fj=Fj+1
            print('')
            
        Keys=[N-i+1,j]     
        FatherKeys = [N-i,Fj]
             
        #print('Father:', N-i,Fj ,'Key:',N-i+1,j)
        
        print('Father:', FatherKeys ,'Key:', Keys)
        PermutationCode[str(FatherKeys[0])+ '|' + str(FatherKeys[1])+' '+str(Keys[0]) + '|' + str(Keys[1])]='Ciao'     


for el in PermutationCode:
    print(el,PermutationCode[el])
