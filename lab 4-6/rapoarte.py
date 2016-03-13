from adaugare import addMonthBill


an={0:'ianuarie',1:'februarie',2:'martie',3:'aprilie',
    4:'mai',5:'iunie',6:'iulie',7:'august',
    8:'septembrie',9:'octombrie',10:'noiembrie',11:'decembrie'}







def totalSumType(apartaments, bill):
    totalSum=0
    for i in range(10):
        for j in range (12):
            values=list(apartaments[i][j].values())
            keys=list(apartaments[i][j].keys())
            if bill in keys:
                index=keys.index(bill)
                totalSum+=values[index]
    return totalSum

def testTotalSumType():
    apartaments=[[{} for x in range(0,12)] for x in range(100)]
    days=[[0 for x in range(0,12)] for x in range(100)]

    bills={'apa':25, 'canalizare':25}
    addMonthBill(apartaments, days,bills,  0, 0, 12)
    bills={'apa':20, 'canalizare': 25}
    addMonthBill(apartaments, days,bills, 0, 1, 12)
    corectSum=45
    suma=totalSumType(apartaments,'apa')
    assert(suma==corectSum)
testTotalSumType()

def printTotalSumType(apartaments,bill):
    print("Costul total al blocului pentru ",bill,"este de ", totalSumType(apartaments,bill),"lei")






def totalBillOnApartament(apartaments, apartamentNumber, bill):
    billSum=0
    for i in range(12):
        values=list(apartaments[apartamentNumber][i].values())
        keys=list(apartaments[apartamentNumber][i].keys())
        if bill in keys:
            index=keys.index(bill)
            billSum+=values[index]
    return billSum

def testTotalBillOnApartament():
    
    apartaments=[[{} for x in range(0,12)] for x in range(100)]
    days=[[0 for x in range(0,12)] for x in range(100)]
    bills={'apa':50, 'canalizare':25}
    addMonthBill(apartaments, days, bills, 0 ,0 ,15)
    bills={'apa':150, 'canalizare':25}
    addMonthBill(apartaments, days, bills, 1 ,0 ,15)

    assert(totalBillOnApartament(apartaments, 0, 'apa')== 200)

testTotalBillOnApartament()

def sortApartamentsByBill(apartaments,bill):
    orderedList=[]
    indexList=[]
    for i in range (10):
        orderedList.append(totalBillOnApartament(apartaments,i,bill))
        indexList.append(i)
    
    for i in range(9):
       for j in range(i+1,10):
           if(orderedList[i]>orderedList[j]):
               aux=orderedList[i]
               orderedList[i]=orderedList[j]
               orderedList[j]=aux
               aux=indexList[i]
               indexList[i]=indexList[j]
               indexList[j]=aux
    return indexList
            
def printSortedApartaments(apartaments, bill, z_index):
    orderedList=sortApartamentsByBill(apartaments,bill)

    if(z_index):
     
        pass
    else:
        orderedList=list(reversed(orderedList))
        
    
    
    for i in range(1,len(orderedList)+1):
            print(i,". Apartamentul:",orderedList[i-1]+1,"cu chelutieli:",totalBillOnApartament(apartaments, orderedList[i-1],bill),"lei, la",bill)


def testSortApartamentsByBill():
    pass

def getTotalSumOnApartament(apartaments,apartamentNumber):
    sumTotal=0
    for i in range(12):
        values=list(apartaments[apartamentNumber][i].values())
        for n in values:
            sumTotal+=n
    return sumTotal

def printTotalSumOnApartament(apartaments, apartamentNumber):
    print("Suma totala pe cheltuieli pentru apartamentul",apartamentNumber+1,"este de: ",getTotalSumOnApartament(apartaments,apartamentNumber)," lei")





