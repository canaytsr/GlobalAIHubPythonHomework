a = input("Enter 1st input: ")
b = input("Enter 2nd input")
c = input("Enter 3rd input: ")
d = input("Enter 4st input: ")
e = input("Enter 5st input: ")

mylist=[a,b,c,d,e]

for i in range(5):
    if mylist[i].isdigit():#integer
        mylist[i]=int(mylist[i])
        
    elif  mylist[i].replace(".","", 1).isdigit():#float
        mylist[i]=float(mylist[i])
            
    elif  mylist[i].count("-"):
        mylist[i]=mylist[i].replace("-","", 1)
       
        if mylist[i].isdigit():
            mylist[i]=int(mylist[i])
            mylist[i]=mylist[i]*-1
            
        else:
            mylist[i]=float(mylist[i])
            mylist[i]=mylist[i]*-1
    
    elif mylist[i]==str(mylist[i]):
        mylist[i]==mylist[i]
    else:
        mylist[i]=mylist[i]*(-1)
        
print(mylist)
print('\nFirst value:',mylist[0], type(mylist[0]))
print('Second value:{}  '.format(mylist[1]),type(mylist[1]))
print('Third value:{}  '.format(mylist[2]),type(mylist[2]))
print(f'Fourth value:{mylist[3]} ',type(mylist[3]))
print(f'Fifth value:{mylist[4]}  ',type(mylist[4]))
