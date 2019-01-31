'''
Created on 31 gen 2019

@author: pasteris
'''

N=3
jTot=1
for i in range(N,-1,-1):
    print('---',i)
    jTot=jTot*i
    Fj=0
    for j in range(0,jTot,1):
        if (j%i==0):
            Fj=0
        else:
            Fj=Fj+1
        
            
        print('Father:', N-i,Fj ,'Key:',N-i+1,j)
    
    