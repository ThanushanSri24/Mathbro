#Import items
import random
from datetime import datetime
import sys

G=[]#Final out
rand = random.randrange(100,999)
Time = datetime.now()
time = Time.strftime("Time : %H:%M\n")
date = Time.strftime("\nDate : %y-%m-%d\n")
name = Time.strftime(f"%y%m%d_%H%M_{rand}.txt")
T= date + time
session_count=1
#Condition
def D():
    G.append(T)
    while True:
        C=0#Question Count
        for i in range(3):
            L=[0,1,2,3,4,5]
            random.shuffle(L)
            Q=L[0]+L[1]
            pq=str(L[0])+" + "+str(L[1])+" = "
            print(pq,end="")
            V=int(input())
            if Q==V:
                S="√  "+str(pq)+str(V)
                C+=1
            else:
                S="X  "+str(pq)+str(V)+"    The correct answer is "+str(Q)
            G.append(S)
        G.append(f'\nTotal questions : 3\nCorrect questions : {C}\nMarks : {((C/3)*100)}%\nMode = Demo')          
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again=='yes':
            continue
        elif play_again=="no":
            break                   
    return
def E():
    G.append(T)
    C=0
    while True:
        L=[0,1,2,3,4,5,6,7,8,9,10]
        O=["+","-"]
        for i in range(5):
            random.shuffle(L)
            random.shuffle(O)
            operator=O[0]
            if O[0]=="+":
                Q=L[0]+L[1]
                pq=str(L[0])+" + "+str(L[1])+" = "
                C+=1
            elif O[0]=="-":
                Q=L[0]-L[1]
                pq=str(L[0])+" - "+str(L[1])+" = "
                #Q
            print(pq,end="")
            V=int(input())
            if Q==V:
                S="√  "+str(pq)+str(V)
            else:
                S="X  "+str(pq)+str(V)+"    The correct answer is "+str(Q)
            G.append(S)
        G.append(f'\nTotal questions : 5\nCorrect questions : {C}\nMarks : {((C / 5) * 100)}%\nMode = Eassy')
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again=='yes':
            continue
        elif play_again=="no":
            break                   
    return 
def M():
    G.append(T)
    C=0
    while True:
        L=[0,1,2,3,4,5,6,7,8,9,10]
        O=["+","-"]
        for i in range(10):
            random.shuffle(L)
            random.shuffle(O)
            operator=O[0]
            if O[0]=="+":
                Q=L[0]+L[1]
                pq=str(L[0])+" + "+str(L[1])+" = "
                C+=1
            elif O[0]=="-":
                Q=L[0]-L[1]
                pq=str(L[0])+" - "+str(L[1])+" = "
                C+=1
                #Q
            print(pq,end="")
            V=int(input())
            if Q==V:
                S="√  "+str(pq)+str(V)
            else:
                S="X  "+str(pq)+str(V)+"    The correct answer is "+str(Q)
            G.append(S)
        G.append(f'\nTotal questions : 10\nCorrect questions : {C}\nMarks : {((C / 10) * 100)}%\nMode = Medium')
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again=='yes':
            continue
        elif play_again=="no":
            break                   
    return    
        
def H():
    G.append(T)
    C=0
    while True:
        L=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        O=["+","-","*"]
        for i in range(10):
            random.shuffle(L)
            random.shuffle(O)
            operator=O[0]
            if O[0]=="+":
                Q=L[0]+L[1]
                pq=str(L[0])+" + "+str(L[1])+" = "
                C+=1
            elif O[0]=="-":
                Q=L[0]-L[1]
                pq=str(L[0])+" - "+str(L[1])+" = "
                C+=1
            elif O[0]=="*":
                Q=L[0]*L[1]
                pq=str(L[0])+" x "+str(L[1])+" = "
                C+=1
                #Q
            print(pq,end="")
            V=int(input())
            if Q==V:
                S="√  "+str(pq)+str(V)
            else:
                S="X  "+str(pq)+str(V)+"    The correct answer is "+str(Q)
            G.append(S)
        G.append(f'\nTotal questions : 10\nCorrect questions : {C}\nMarks : {((C / 10) * 100)}%\nMode = Hard')
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again=='yes':
            continue
        elif play_again=="no":
            break                   
    return
#CMD 
if len(sys.argv)==1:
    X='D'
else:
    X=sys.argv[1].lower()
    

if X =='D':
    D()
elif X == '-e':
    E()
elif X=='-m':
    M()
elif X=='-h':
    H()
file=open(name, 'w', encoding='utf-8')
for i in G:
    file.write(str(i) + '\n')

    




