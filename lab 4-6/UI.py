from adaugare import *
from cautari import *
from filtre import *
from rapoarte import *
from stergere import *
from undo import *

'''initializam 100 de apartamente si cheltuielile pe un an
initializam o matrice identica in care o vom retine zilele
in care au fost facute cheltuielile'''

apartaments=[[{} for x in range(0,12)] for x in range(10)]
days=[[0 for x in range(0,12)] for x in range(10)]
undoList=[]
validBills=('apa', 'curent', 'canalizare', 'altele')

an={0:'ianuarie',1:'februarie',2:'martie',3:'aprilie',
    4:'mai',5:'iunie',6:'iulie',7:'august',
    8:'septembrie',9:'octombrie',10:'noiembrie',11:'decembrie'}

addMonthBill(apartaments, days,{'apa':105, 'curent':205 , 'canalizare':50},  1, 0, 12)
addMonthBill(apartaments, days,{'altele':125, 'apa':205 },  4, 0, 12)
addMonthBill(apartaments, days,{'altele':400, 'curent':20 },  1, 3, 20)
addMonthBill(apartaments, days,{'apa':400, 'curent':20 ,'canalizare':125},  11, 5, 20)

while True:
    
  if True:
        print("Alegeti Optiunea:")
        
        print(" 1- Adaugă cheltuială pentru un apartament")
        print(" 2- Modifică cheltuială")
        print(" 3 - Șterge toate cheltuielile de la un apartament")
        print(" 4- Șterge cheltuielile de la apartamente consecutive ")
        print(" 5- Șterge cheltuielile de un anumit tip de la toate apartamentele")
        
        print("  6 - Tipărește toate apartamentele care au cheltuieli mai mari decăt o sumă dată")
        print("  7- Tipărește cheltuielile de un anumit tip de la toate apartamentele")
        print("  8- Tipărește toate cheltuielile efectuate înainte de o zi și mai mari decât o sumă" )
        print("  9 - Tipărește suma totală pentru un tip de cheltuială")
        print("  10- Tipărește toate apartamentele sortate după un tip de cheltuială")
        print("  11- Tipărește totalul de cheluieli pentru un apartament dat")
        print("  12 - Elimină toate cheltuielile de un anumit tip")
        print("  13- Elimină toate cheluielile mai mici decât o sumă dată")
        print("  14- Afiseaza intreaga lista")
        print("  15- Undo")
        print("  16- Exit")
  try:
        
        optiune=int(input("Optiunea dumneavoastra: " ))
        
        
        if(optiune==1):
            
            
            saveList(apartaments, days ,undoList)
            apartamentNumber=int(input("Numarul apartamentului:"))

            while apartamentNumber >10 or apartamentNumber<0:
                print('Apartamentul cu numarul', apartamentNumber,' nu exista. Alegeti un numar intre 1 si 10')
                apartamentNumber=int(input("Numarul apartamentului:"))
            
            values=list(an.values())
            month=input("Luna in care s-au realizat cheltuielile:")
            while month not in values:
                month=input("Luna in care s-au realizat cheltuielile(ianuarie, februarie etc... ):")
            
           
            month=values.index(month)
            
                
            bills={}
        
            
            print("Lista pentru tipurile valabile:" , validBills)
            while True:
                billType=input('Introduceti cheltuielile dorite din lista: ')

                if billType in validBills:
                    k=int(input("Suma Dorita"))
                    bills[billType]=k
                else:
                    print(" Invalid")
                    continue
                
                k=int(input(" Continuati? 1- da , 0- nu"))
                if k==0:
                    break
            
                         
                   
            day=int(input("ziua in care s-au realizat cheltuielile:"))

            addMonthBill(apartaments, days,bills,  month, apartamentNumber-1, day)
        elif optiune==2:
            saveList(apartaments, days ,undoList)
            
            apartamentNumber=int(input('Numarul apartamentului caruia doriti sa modificati datele: ' ))

            for i in range(0,12):
                if apartaments[apartamentNumber-1][i]!={}:
                    
                    print('Luna: ',an[i])
                    print(apartaments[apartamentNumber-1][i])
            
            while apartaments[apartamentNumber-1]==[{}]*12:
                print(' Apartamentul ' , apartamentNumber, ' nu are inregistrari! ' )
                apartamentNumber=int(input('Numarul apartamentului caruia doriti sa modificati datele: ' ))
           
            month=input(' Luna in care doriti sa aduceti o modificare/adaugare' )
            while month not in an.values():
                print(' invalid! ')
                month=input(' Luna in care doriti sa aduceti o modificare/adaugare' )

            
            billType=input('Tipul cheltuielii pe care doriti sa o modificati/adaugati' )
            while billType not in validBills:
                print(' invalid!' )
                billType=input('Tipul cheltuielii pe care doriti sa o modificati/adaugati' )
            summ=int(input(' Suma pe care doriti sa o adaugati' ))
            values=list(an.values())
            k=values.index(month)
            apartaments[apartamentNumber-1][k][billType]=summ
            
                
        elif optiune==3:
            saveList(apartaments, days ,undoList)
            apartamentNumber=int(input('Numarul apartamentului:'))
            deleteAllBillsOnApartament(apartaments, days, apartamentNumber-1)
        elif optiune==4:
            saveList(apartaments, days ,undoList)
            start=int(input('Stergeti de la apartamentul: '))
            end=int(input('pana la apartamentul: '))
            deleteConsecutiveBills(apartaments, days, start-1, end-1)
        elif optiune==5:
            saveList(apartaments, days ,undoList)
            billType=input('Tipul chelutielii')
            deleteBillOfType(apartaments, billType)
        elif optiune==6 :
                   value=int(input("Suma:"))
                   printGreaterThan(apartaments, days, value)
        elif optiune==7:
                    billType=input("Tipul cheltuielii:")
                    printTypeBills(apartaments,billType)
        elif optiune==8:
                    day=int(input("Ziua:"))
                    value=int(input("Suma:"))
                    printGreaterThanAndLaterThan(apartaments, days,value, day)
        elif optiune==9:
                    billType=input("tipul chelutielii: ")
                    printTotalSumType(apartaments,billType)
        elif optiune==10:
                    billType=input("tipul cheltuielii: ")
                    z_index=int(input("1- pentru sortat ascendent, 0 pentru sortat descendent"))
                    printSortedApartaments(apartaments, billType, z_index)
        elif optiune==11:
                    apartamentNumber=int(input('Numarul apartamentului: '))
                    apartamentNumber-=1
                    printTotalSumOnApartament(apartaments, apartamentNumber)

        elif optiune==12:
                    saveList(apartaments, days ,undoList)
                    saveList (apartaments, days ,undoList)
                    billType=input("Tipul Cheltuielii : ")
                    deleteBillOfType(apartaments,billType)
        elif optiune==13:
                    saveList(apartaments, days ,undoList)
                    suma=int(input("Suma: "))
                    deleteFewerThan(apartaments, suma)
        elif optiune==14:
                    for i in range(10):
                        ok=0
                        for j in range(12):
                            if apartaments[i][j]!={}:
                                if not ok:
                                    print("Apartamentul", i+1)
                                    ok=1
                                print("Luna",an[j])
                        
                                print(apartaments[i][j])
            
        elif optiune==15:
                    undo(apartaments, days , undoList)
        elif optiune==16:
                    print(' Finalizare cu succes! ')
                    break
        
               
  except ValueError:
        print('date invalide!')
  except IndexError:
        pass
  
            

