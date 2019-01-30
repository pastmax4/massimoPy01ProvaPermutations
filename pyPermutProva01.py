'''
Created on 30 gen 2019

@author: mpasteri

https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/

'''



def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    print('len di lst=',len(lst))
    for i in range(len(lst)):   
        print('##i=',i)           
        m = lst[i] 
        print('##m=  ',m)
        
        
        # Extract lst[i] or m from the list.  remLst is 
        # remaining list 
        remLst = lst[:i] + lst[i+1:] 
        print('remLlst  ', remLst)
        print('  ')
       
        # Generating all permutations where m is first 
        # element 
        for p in permutation(remLst): 
            print('ppppppp=',p)
            l.append([m] + p)
            
        print('---------------------')     
    return l 


listPippo=['a','b','c','d','e']

data = list('123') 
for p in permutation(data): 
    print(p) 








    

