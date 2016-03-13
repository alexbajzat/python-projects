'''
Created on 26 Jan 2016

@author: name
'''
from Domain import *

class Controller:
    def __init__(self,repository):
        
        ''' constructorul isi creeaza un atribut privat , repository'''
        
        self.__repository=repository
        
    def newWord(self, initLang,initWord, destLang,finalWord):
            '''metoda primeste 4 parametrii reprezentand atributele obiectului de tip Cuvant,
                    il creeaza si il adauga in dictionar
                    initLang, initWord, destLang, finalWord - de tip string '''
    
            self.word=Word(initLang,initWord,destLang,finalWord)
            dictionary=self.__repository.getDictionary()
            
            for i in dictionary:
                if i.getInitLang()==self.word.getInitLang() and i.getInitWord()==self.word.getInitWord() and i.getDestLang()==self.word.getDestLang() and i.getFinalWord()==self.word.getFinalWord():
                        raise ValueError
      
            self.__repository.addWord(self.word)
        
    
    def getDictionary(self):
        
        '''metoda returneaza dictionarul din repository ''' 
        
        return self.__repository.getDictionary()
    
    def deleteWord(self,word):
        
        '''metoda aceasta cauta un cuvant dupa un parametru dat si il sterge din lista 
        word- string '''
        word=word.upper()
        dictionary=self.__repository.getDictionary()
        for i in dictionary:
            if i.getInitWord()==word or i.getFinalWord()==word:
                dictionary.remove(i)
                
    def translateFromFile(self,fileName,initLang, destLang):
        
        ''' metoda primeste 3 parametrii string ,si cauta un fisier dupa fileName si translateaza in limba destLang dorita'''
        try:
            translatedString=""
            file=open(fileName,'r')
            dictionary=self.__repository.getDictionary()
            
            
            for line in file.readlines():
                if line!="":
                    
                    line=line.split(" ")
                    
                    for word in line:
                        if word!="" and word!=" ":
                            
                            word=word.upper()
                            
                            
                            translated=False
                            
                            for i in dictionary:
                                if i.getInitWord()==word:
                                    if i.getInitLang()==initLang and i.getDestLang()==destLang:
                                        translatedString+=i.getFinalWord()+ " "
                                        translated=True
                                        
                                elif i.getFinalWord()==word:
                                    if i.getInitLang()==destLang and i.getDestLang()==initLang:
                                        translatedString+=i.getInitWord()+ " "
                                        translated=True
                        if not translated:
                            translatedString+="{"+word+"} "
                
            return translatedString
        except IOError:
            print("File not found! ")
            
    
    def saveList(self):
        
        ''' metoda salveaza in fisier lista curenta'''
        
        self.__repository.writeToFile()
        
