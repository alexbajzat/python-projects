'''initializam 100 de apartamente si cheltuielile pe un an
initializam o matrice identica in care o vom retine zilele
in care au fost facute cheltuielile'''

apartaments=[[{} for x in range(0,12)] for x in range(100)]
days=[[0 for x in range(0,12)] for x in range(100)]
an={0:'ianuarie',1:'februarie',2:'martie',3:'aprilie',
    4:'mai',5:'iunie',6:'iulie',7:'august',
    8:'septembrie',9:'octombrie',10:'noiembrie',11:'decembrie'}






def deleteBillOfType(apartaments, billType):
	for i in range (10):
		for j in range(12):
			if billType in apartaments[i][j]:
				
				
				del apartaments[i][j][billType]
				
def deleteFewerThan(apartaments, billSum):
    for i in range(10):
        for j in range(12):
            keys=list(apartaments[i][j].keys())
            for k in keys:
                if apartaments[i][j][k]<billSum:
                    del apartaments[i][j][k]
                


    



