'''
Created on 30 gen 2019

@author: mpasteri

https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/

'''
Keys=[]
N=3
listSymb=['A','B','c']
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
        PermutationCode['F'+str(FatherKeys[0])+ ',' + str(FatherKeys[1])+'K'+str(Keys[0]) + ',' + str(Keys[1])+'V']='Ciao'     

#-----------------------------------
#-----------------------------------

for key in PermutationCode:
    print(key)        

#-----------------------------------
ind=0
for key in PermutationCode:        
    if 'F0' in key:       
        PermutationCode[key]=listSymb[ind]
        ind=ind+1

#-----------------------------------
#-----------------------------------
for key01 in PermutationCode:       
    if 'K2' in key01:
        #print(key)
        startF = key01.find('F') 
        endF = key01.find('K')
        Fat=key01[startF+1:endF]    
        print('Fat',Fat)   
        for key02 in PermutationCode:    
            if 'K'+Fat in key02:
                print('---',key02)
                

 


#------------------------------------
for key in PermutationCode:
    print(key,PermutationCode[key])        

        


