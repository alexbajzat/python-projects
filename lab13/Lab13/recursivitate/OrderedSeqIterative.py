'''
Created on 04 Jan 2016

@author: name
'''


def isSorted(list):
   
    
    for i in range(0, len(list)-1):
        
            if list[i]>=list[i+1]:
                return False
        
    return True

def printList(list):
    print("(", end="")
    fTime=True
    for i in list:
        if not fTime:
            print(',',end=" ")
        fTime=False
        print(i,end="") 
    
    
    print(")", end=" ")


                
                
            
            
            
  
 
list=[1,2,1,3,7,5,6]


firstTime=True


while list!=[]:
    newList=[]
    
    for i in list:
        newList.append(i)
        
        if isSorted(newList):
            printList(newList)
            print(" ")
            
        else:
            newList.pop()
    list.remove(list[0])
    
