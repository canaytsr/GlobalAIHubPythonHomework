import random
figure =["""
   +---+
   |   |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------"""]

user_name=input("Enter your name:")
print("Welcome "+user_name+" Let's start the game!")

name_list=["brad","gray","cate","viola","mary" ,"william","olivia"]
color_list=["orange","green","violet","black","yellow","yellow","brown"]

print("1-Name")
print("2-Color")
selection= int(input("Select Category:"))

if selection==1:
    select_word=random.choice(name_list)
   
elif selection==2:
    select_word=random.choice(color_list)
    
else:
    print("Please enter valid value:")

mylist=[]
t=0
j=0
while j in range(len(select_word)):
    mylist.insert(j,"_") 
    #mylist.insert(j+1," ")
    j+=1
    
while t in range(len(mylist)):
    print(mylist[t]," ",end="") 
    t=t+1
print("")
false=0
r=0
true=0
print(figure[0])
while false<6 and true<len(select_word):
    
    tahmin=input("Enter a letter:")
    if tahmin not in select_word:
        false+=1
        print("Wrong Guess",end="")
        r=r+1
        print(figure[r])
        
        print(' {} tane tahmin hakkiniz kaldi.'.format(6-false))
    else:
        true+=1
        for i in range(len(select_word)):
            
            if tahmin==select_word[i]:
                print("True Guess")
                mylist[i]=tahmin
        print(' '.join(mylist),end='\n')
        
        
   
print("")  
if true>=len(select_word):
    print("---YOU WİN-----")

elif false>=6:
    print("---GAME OVER-----")



