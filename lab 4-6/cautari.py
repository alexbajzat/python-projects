from adaugare import addMonthBill



an={0:'ianuarie',1:'februarie',2:'martie',3:'aprilie',
    4:'mai',5:'iunie',6:'iulie',7:'august',
    8:'septembrie',9:'octombrie',10:'noiembrie',11:'decembrie'}






    
    
    
'''The first function is done by verifing each aparaments monthly bill
and if one bill is greater than the sum passed by the user,
the apartaments number is copied in a list (apartamentList)'''
    
def getGreaterThan(apartaments, valueToBeTested, apartamentList):
    for i in range(0,10):
        for j in range (0,12):
            if len(apartaments[i][j])>0:
                lista=apartaments[i][j].values()
                for n in lista:
                    if n>valueToBeTested:
                        apartamentList.append(i+1)
                        break
    
                    

def testGetGreaterThan():
    '''test the getGreaterThan function by comparing the resulted list
    with a pre-defined one
    '''
    apartaments=[[{} for x in range(0,12)] for x in range(10)]
    days=[[0 for x in range(0,12)] for x in range(10)]

    bills={'apa':120, 'canalizare':21, 'altele':150}
    addMonthBill(apartaments, days,bills, 0, 0, 15)

    bills={'apa':10, 'canalizare':21, 'altele':50}
    addMonthBill(apartaments, days ,bills, 0 ,1 ,14 )

    bills={'apa':10, 'canalizare':216, 'altele':50}
    addMonthBill(apartaments, days,bills ,0 ,2 , 12)

    
    
    
    listaTest=[]
    corectList=[1,3]
    getGreaterThan(apartaments,100,listaTest)
    for i in range (0,len(listaTest)):
            assert(corectList[i]==listaTest[i])
            
testGetGreaterThan()

def printGreaterThan(apartaments, days,value):
    apartamentList=[]
    getGreaterThan(apartaments, value, apartamentList)
    
    print(apartamentList)
    

''' First iteration`s second requirement done by testing each apartaments bills on each month
for a given type of bill. The function creates a bidimensional list of bills
in which we have the list of monthly bills of a type for each apartament'''

def getTypeBills(apartaments, billType,billList):
    
    for i in range (10):
        appList=[]
        for j in range(0,12):
            #if(len(apartaments[i][j])>0):
                
                test=list(apartaments[i][j].keys())
                if billType in test:

                    fIndex=test.index(billType)
                    
                    
                    values=list(apartaments[i][j].values())
                    
                    appList.append(values[fIndex])
                else:
                    appList.append(0)
                
        if(len(appList)>0):
            billList.append(appList)
        else:
            billList.append(0)


def testGetTypeBills():

    ''' test the arrays obtained from the getTypeBills function ,
    and compare it with a pre-defined array with the exepected elements'''
    apartaments=[[{} for x in range(0,12)] for x in range(100)]
    days=[[0 for x in range(0,12)] for x in range(100)]
    
    bills={'apa':121,'canalizare':5, 'curent':101, 'pula':5}
    addMonthBill(apartaments, days,bills,0,0,4)
    bills={'apa':52,'canalizare':1, 'curent':87, 'pula':5}
    addMonthBill(apartaments, days , bills,1,0,4)
   
    billList=[]
    getTypeBills(apartaments,'apa',billList)
    correctList=[121, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    k=0
    
    for k in range(0,12):
        assert(billList[0][k]==correctList[k])

testGetTypeBills()

'''The printTypeBills uses the getTypeBills to print the bills of a
type for each apartament
'''

def printTypeBills(apartaments, billType):
    billList=[]
    getTypeBills(apartaments,billType,billList)

    for i in range (len(billList)-1):
        typed=0
        print('Cheltuieli aferente',billType,' pentru apartamentul',i+1)
        for k in range(0,12):
            
                if billList[i][k]!=0:
                    bani=0
                    if billList[i][k]==1:
                        bani='leu'
                    else:
                        bani='lei'
                    
                    print("    Pe luna",an[k]," suma: ",billList[i][k],bani)
                    typed=1
        if not typed:
                print(0,"lei")

''' for the first iteration`s last requirement  the function is checking if the bill on the current month was
payed before the day provided and if so , it checks if the amount payed on a bill is greater than the amount given in order
to print the bill, the sum of the bill, and the month in which was payed''' 

def printGreaterThanAndLaterThan(apartaments, days, amount, day):
    for i in range (10):
        ok=0
        for j in range (12):
            if days[i][j]<day and days[i][j]!=0:
                values=list(apartaments[i][j].values())
                keys=list(apartaments[i][j].keys())
                for n in values:
                    if n>amount:
                        if not ok:
                            print("Apartamentul",i+1,"are cheltuieli mai mari decat",amount,"lei, la:")
                            ok=1
                        index=values.index(n)
                        print(keys[index],n,"lei, luna ",an[j])
        if ok:
            print(" ")


    

    









    
    









