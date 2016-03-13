'''
Created on 26 Jan 2016

@author: name
'''
from Domain import Word
from Repository.DictionaryRepository import *
from Controller import *
import unittest

class TestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testDomain(self):
        initLang="Ro"
        destLang="eN"
        fWord="ceva"
        sWord="something"
        dictWord=Word(initLang,fWord,destLang,sWord)
        assert(dictWord.getInitLang()==initLang.upper())
        assert(dictWord.getDestLang()==destLang.upper())
        assert(dictWord.getInitWord()==fWord.upper())
        assert(dictWord.getFinalWord()==sWord.upper())
        
    def testNewAndAddWord(self):
        initLang="Ro"
        destLang="eN"
        fWord="ceva"
        sWord="something"
        repository=DictRepository()
        dictWord=Word(initLang,fWord,destLang,sWord)
        
        repository.addWord(dictWord)
        assert(len(repository.getDictionary())>0)
    
    def testDeleteWord(self):
        initLang="Ro"
        destLang="eN"
        fWord="ceva"
        sWord="something"
        dictWord=Word(initLang,fWord,destLang,sWord)
        
        repository=DictRepository()
        
        
        
        repository.addWord(dictWord)
        
        
        controller=Controller(repository)
        lastLength=len(controller.getDictionary())
        
        controller.deleteWord(dictWord.getFinalWord())
        
        assert(len(controller.getDictionary())==lastLength-1)
        
    def testTranslate(self):
        
        initLang="Ro"
        destLang="eN"
        fWord="ceva"
        sWord="something"
        repository=DictRepository()
        dictWord=Word(initLang,fWord,destLang,sWord)
        
        repository.addWord(dictWord)
        initLang="en"
        destLang="ro"
        fWord="horse"
        sWord="cal"
        
        
        dictWord=Word(initLang,fWord,destLang,sWord)
        
        
        repository.addWord(dictWord)
        controller=Controller(repository)
        
        initLang="Ro"
        destLang="eN"
        fileName="test.txt"
        assert("{HORSE} {SOMETHING} {ANA} "==controller.translateFromFile(fileName, initLang, destLang))
        
        
        
        
        
        
        
        
    
       
if __name__ == '__main__':
    unittest.main()