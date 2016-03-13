from filtre import deleteBillOfType
from adaugare import addMonthBill




an={0:'ianuarie',1:'februarie',2:'martie',3:'aprilie',
    4:'mai',5:'iunie',6:'iulie',7:'august',
    8:'septembrie',9:'octombrie',10:'noiembrie',11:'decembrie'}


''' the delete function goes to the index given by the apartamentNumber and
removes every bill for every month'''

def deleteAllBillsOnApartament(apartaments,days,apartamentNumber):

     
     for i in range(12):
        
             apartaments[apartamentNumber][i]={}
        

         
def testDeleteAllBillsOnApartament():
     apartaments=[[{} for x in range(0,12)] for x in range(10)]
     days=[[0 for x in range(0,12)] for x in range(10)]

     bills={'apa': 25 ,'canalizare':15, 'altele':75}
     addMonthBill(apartaments, days , bills, 0 ,0 , 15)
     
     

     deleteAllBillsOnApartament(apartaments, days, 0)

     
     assert(apartaments[0]==[{}]*12)
     
     
testDeleteAllBillsOnApartament()


def deleteBillOfType(apartaments,billType):
	for i in range (100):
		for j in range(12):
			if billType in apartaments[i][j]:
				
				
				del apartaments[i][j][billType]
				
def testDeleteBillOfType():
     apartaments=[[{} for x in range(0,12)] for x in range(100)]
     days=[[0 for x in range(0,12)] for x in range(100)]

     bills={'apa': 25 ,'canalizare':15, 'altele':75}
     addMonthBill(apartaments, days , bills, 0 ,0 , 15)
     expectedList={'canalizare':15, 'altele':75}
     

     deleteBillOfType(apartaments, 'apa')
     
     assert(expectedList==apartaments[0][0])
testDeleteBillOfType()
     
    
def deleteConsecutiveBills(apartaments,days, startApartament, endApartament):
    for i in range(startApartament, endApartament+1):
        deleteAllBillsOnApartament(apartaments, days,i)

def testDeleteConsecutiveBills():
     apartaments=[[{} for x in range(0,12)] for x in range(100)]
     days=[[0 for x in range(0,12)] for x in range(100)]
     start=0
     end=3
     bills={'apa': 105 ,'curent':15, 'altele':75}
     addMonthBill(apartaments, days , bills, 0 ,0 , 15)
     bills={'apa': 45 ,'canalizare':15, 'altele':75}
     addMonthBill(apartaments, days , bills, 0 ,1 , 15)
     bills={'apa': 25 ,'canalizare':15, 'altele':75}
     addMonthBill(apartaments, days , bills, 0 ,2 , 15)

     deleteConsecutiveBills(apartaments,days, start ,end)

     for i in range(start, end):
          for k in range(12):
               assert(apartaments[i][k]=={})
    
testDeleteConsecutiveBills()
