'''
Created on 01 Jan 2016

@author: name
'''

def isSorted(list):
   
    
    for i in range(0, len(list)-1):
        if list[i+1]!=None and list[i]!=None:
            if list[i]>=list[i+1]:
                return False
        
    return True

def printList(list):
    print("[",end=" ")
    for i in list:
        if i!=None:
            print(i,end=" ") 
    print("]")
    
    
def solution(origList,list):
    
    for i in range(0,len(list)-1):
        if list[i]!=None and list[i+1]!=None:
            if origList.index(list[i]) > origList.index(list[i+1]) :
                return False
    return True

def subSeq(index,origList,list):
    #list=[None]*len(list)
    if index<len(origList):
        for j in range(index, len(origList)):
            list[index]=origList[j]
            #print(list)
            
            if isSorted(list):
                if solution(origList,list):
                    
                    printList(list)
                
                subSeq(index+1,origList,list)
            
            list[index]=None
            
  
 
list=[1,2,3,7,5,6]

#for i in range(0,len(list)):
auxList=[None]*len(list)
subSeq(0,list,auxList)