'''
Created on 26 Jan 2016

@author: name
'''

from Domain import *
class DictRepository:
    
    def __init__(self):
        self.__dictionary=[]
        
        try:
            file=open("dictionar.txt","r")
            
            for line in file.readlines():
                if line!="":
                    attrs=line.split(',')
                    obj=Word(attrs[0],attrs[1],attrs[2],attrs[3])
                    self.__dictionary.append(obj)
        except IOError:
            print("File does not exist!")
            
    
    
    def writeToFile(self):
        
        try:
            file=open("dictionar.txt",'w')
            for i in self.__dictionary:
                string=""
                string+=i.getInitLang()+','
                string+=i.getInitWord()+','
                string+=i.getDestLang()+','
                string+=i.getFinalWord()+','+ '\n'
                file.write(string)
        except IOError:
            print("Error occured in file parsing! ")
                
            
    def getDictionary(self):
        return self.__dictionary        
    
    def addWord(self,word):
        self.__dictionary.append(word)
    
    
    