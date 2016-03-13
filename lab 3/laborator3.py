
def menuAndInput():

     #display options and return an input
    
     print("Optiuni: ") 
     print("1- Introducere sir")
     print("2- Cerinta 1")
     print("3- Cerinta 2")
     print("0- Iesire")
    
     try:
          n=int(input("Optiunea Dumneavoastra: "))
          return n

     except ValueError:
          
          return -1

def getArray(user_list):

        #get user`s array
     try:
          n=int(input("Lungimea sirului: "))
     except ValueError:
          return 0
     
     while n<=0 or n>100:
          print("Lungimea listei nu este valida")
          print("Introduceti un numar mai mare decat 0 pentru a continua")
          print("Introduceti -1 pentru a renunta")
          n=int(input("Lungimea sirului: "))
          if n==-1:
               break
  
     if(n==-1):
          return 0
     for i in range(0,n):
          String="Elementul "+ str(i+1) + ": ";

          try:
               
               k=int(input(String))
          except ValueError:
               k=1001

          while k<-1000 or k>1000:
                    print("Valoare invalida!")
                    try:
               
                         k=int(input(String))
                    except ValueError:
                         k=1001
                    
               
          user_list.append(k)
  

     

     if n>0:
       return n
     else:
          return 0

def Cerinta1(user_list, n):
     
        #cea mai lunga secventa de 3 numere consecutive egale

          i=0
          k=0
          i_init=0
          final_array=[]
          
          while i+2<n:
               
               i_init=i
               p=0
               while i+2<n and (user_list[i]==user_list[i+1] or user_list[i]==user_list[i+2] or user_list[i+1]==user_list[i+2]):
                         
                         p+=1
                         i+=1
                         if i>=n:
                              break
                         
               while i>n:
                         i-=1
               if p>k:
                              final_array=[]
                              for q in range(i_init,i+2):
                                        final_array.append(user_list[q])
                              k=p
               
               i+=1
                         
               
          
                    
                    
          if final_array==[]:
                  print("NU exista o secventa cu cerinta data")
          else:
                  print(final_array)
     
         

def Cerinta2(user_list, n):

               if user_list==[]:
                    print("Nu ati inserat elemente in sir!")
                    return 0
               try:
                    poz=int(input("Pozitia de start a cautarii: "))-1
               except ValueError:
                    print("Invalid!")
                    Cerinta2(user_list,n)
               while(poz>=n):
                    print("Invalid")
                    print("Introduceti un numar din intervalul [", 1 , n-1, "] pentru a continua, sau -1 pentru a abandona")
                    poz=int(input("Pozitia de start a cautarii: "))
                    poz-=1
               if(poz==-1):
                    return 0

               j=poz
               maxim=0
               final_array=[]
               while j+2<n:
                    i_init=j
                    k=0
                    while(user_list[j+1]-user_list[j])*(user_list[j+2]-user_list[j+1])<0:
                              k+=1
                              j+=1
                              if j+2>=n:
                                   break

                    while j>=n:
                         j-=1
                    if k>maxim:
                         maxim=k
                         final_array=[]
                         for q in range (i_init,j+2):
                              final_array.append(user_list[q])
                              
                    j+=1
               if final_array!=[]:
                    print(final_array)
               else:
                    print(" Nu exista o secventa cu cerinta data")
                              
                   
               
                    
                    
        
def MainThread():
 optiune=-1
    #The starting point
 while optiune!=0: 
    optiune=menuAndInput()
    
     
    if(optiune==1):
         #apelare functie cu prima optiune

         user_list=[]
     
 
         n=getArray(user_list)
    
 
     
         print("Lista curenta : ",user_list)
         
    elif(optiune==2):
         #apelare functie cu optiunea a2a
          try:
                 Cerinta1(user_list, n)
          except UnboundLocalError:
               print(" Nu exista elemente in sir!")
       
    elif(optiune==3):
         #apelare functie cu optiunea a3a
          try:
              Cerinta2(user_list,n)
          except UnboundLocalError:
               print(" Nu exista elemente in sir!")
        
    else:

          if optiune==0:
             print("Actiune incheiata!")
             break
          else:  
             print("Invalid")
             continue

   
     

MainThread()

