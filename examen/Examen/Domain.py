'''
Created on 26 Jan 2016

@author: name
'''

class Word:
    
    def __init__(self,initLang,initWord,destLang,finalWord):
        
        
        self.initLang=initLang.upper()
        self.initWord=initWord.upper()
        self.destLang=destLang.upper()
        self.finalWord=finalWord.upper()
        
        if self.initWord==self.finalWord or self.initWord=="" or self.finalWord=="":
            raise ValueError
        
        if not (self.initLang=="RO" or self.initLang == "EN" or self.initLang == "FR") and not (self.destLang=="RO" or self.destLang == "EN" or self.destLang == "FR"):
            raise ValueError
        
        
        
    def getInitLang(self):
        return self.initLang
    def getInitWord(self):
        return self.initWord
    def getDestLang(self):
        return self.destLang
    def getFinalWord(self):
        return self.finalWord
    
    