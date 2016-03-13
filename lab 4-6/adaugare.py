
def addMonthBill(apartaments,days,bills, month, apartament_number,time):
    '''for each apartament (apartament_number) we add a bill list
    (bills) and a list for the billing days (days)'''
    
    apartaments[apartament_number][month]=bills
    days[apartament_number][month]=time

def testAddMonthBill():
    apartaments=[[{} for x in range(0,12)] for x in range(100)]
    days=[[0 for x in range(0,12)] for x in range(100)]
    
    expectedBills={'apa':52,'curent':124, 'canalizare': 205}
    expectedDays=5
    
    addMonthBill(apartaments,days,{'apa':52,'curent':124, 'canalizare': 205},1,0,5)
    assert(apartaments[0][1]==expectedBills)
    assert(days[0][1]==expectedDays)
    
testAddMonthBill()


    
