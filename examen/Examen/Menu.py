'''
Created on 26 Jan 2016

@author: name
'''


class Menu:
    
    def __init__(self,controller):
        self.toShow=""
        
        self.toShow+="1.Adaugare cuvant \n"
        self.toShow+="2. Afisare dictionar \n"
        self.toShow+="3.Stergere cuvant \n"
        self.toShow+="4.Translatare text din fisier \n"
        self.toShow+="0. Exit \n "
        
        self.__controller=controller 
        
    def printMainMenu(self):
        
        ''' printeaza meniu''' 
        
        print(self.toShow)
        
    def getOption(self):
        
        ''' initializeaza o variabila int cu optiunea introdusa''' 
        
        try:
            self.option=int(input("Optiunea dumneavoastra: "))
            
        except ValueError:
            print("Optiune invalida! ")
        return self.option
    
    def autoPlay(self):
        
        ''' metoda aceasta pune afisarea in loop pana la introducerea valorii 0 ''' 
        
        self.option=-1
        while True:
            self.printMainMenu()
            self.option=self.getOption()
            
            if self.option==1:
                
                initLang=input("Limba cuvantului initial: ")
                initWord=input("Cuvantul initial: ")
                destLang=input("Limva cuvantului destinatie: ")
                finalWord=input("Cuvantul: ")
                
                try:
                    self.__controller.newWord(initLang,initWord,destLang,finalWord)
                    
                except ValueError:
                    print("Informatiile introduse nu sunt corecte! ")
                
            
            elif self.option==2:
                
                dictionary=self.__controller.getDictionary()
                
                for i in dictionary:
                    print(i.getInitLang()+', '+i.getInitWord()+', '+i.getDestLang()+ ', '+ i.getFinalWord())
                print(' \n ')
            elif self.option==3:
                word=input("Cuvantul de sters: ")
                self.__controller.deleteWord(word)
                
            elif self.option==4:
                fileName=input("Numele fisierului: ")
                initLang=input("Limba textului (ro, en ,fr): ")
                destLang=input("Limba pentru traducere (ro, en ,fr):  ")
                initLang=initLang.upper()
                destLang=destLang.upper()
                string=self.__controller.translateFromFile(fileName,initLang,destLang)
                print(string+ '\n ')
            elif self.optiune==0:
                break
            else: 
                print(" Optiune invalida! ")
                
            self.__controller.saveList()