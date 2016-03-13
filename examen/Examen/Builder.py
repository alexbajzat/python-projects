'''
Created on 26 Jan 2016

@author: name
'''

if __name__ == '__main__':
    pass

from Repository.DictionaryRepository import DictRepository
from Controller import Controller
from Menu import Menu

class Builder:
    
    
    def __init__(self):
        
        ''' constructorul clasei builder initlaizeaza repository-ul si controller-ul'''
        
        self.__repository=DictRepository()
        self.__controller=Controller(self.__repository)
        
    def startApp(self):
        
        '''metoda startApp apeleaza meniul '''
        menu=Menu(self.__controller)
        menu.autoPlay()

builder=Builder()
builder.startApp()