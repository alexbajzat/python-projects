

from copy import deepcopy


def saveList (apartaments, days ,undoList):
    
            

            undoList.append(deepcopy(apartaments))
            undoList.append(deepcopy(days))
            
        
    
    
    
    
    

def undo(apartaments, days, undoList):
    
       
    days=deepcopy(undoList[len(undoList)-1])
    del undoList[len(undoList)-1]
    
    apartaments.clear()
    apartaments.extend(deepcopy(undoList[len(undoList)-1]))
    
    del undoList[len(undoList)-1]
    



