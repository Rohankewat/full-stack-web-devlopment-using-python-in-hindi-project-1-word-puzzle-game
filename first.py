print("INSTRUCTIONS 1-> You can give answer by First letter capital or all letters capital or all letters small")
print("2 -> If you give correct answer you got +1 and for wrong -1")
print("3 -> You have to play 3 rounds on each round you will face 5 words")
l1 = ["RAEHTF","KABRE","RENEG","OAERELANP","OLELH","WEOELMC","ROYENW","AHNMEOSD","DOGO","RETBET","EICN","LOCO","EIDNFR","TAC","YAES","DARH"]
l2 = ["Father","FATHER","father","Break","BREAK","break","Aeroplane","AEROPLANE","aeroplane","Hello","HELLO","hello","Welcome","WELCOME","welcome","Newyork","NEWYORK","newyork","Handsome","HANDSOME","handsome","Good","GOOD","good","Better","BETTER","better","Nice","NICE","nice","Cool","COOL","cool","Friend","FRIEND","friend","Cat","CAT","cat","Easy","EASY","easy","Hard","HARD","hard","Green","GREEN","green"]
a,b,c = 0,0,0
print("ROUND 1")       
i = 0
while i<=4:
    print(l1[i])
    ans = input("Arrange the letters to form a valid word ")
    if ans in l2:
        print("Correct")
        a += 1
    else:
        print("Wrong")
        a -= 1
    i += 1
print("Round 1 score is",a)
print("ROUND 2")
i = 5
while i<= 9:
    print(l1[i])
    ans = input("Arrange the letters to form a valid word ")
    if ans in l2:
        print("Correct")
        b += 1
    else:
        print("Wrong")
        b -= 1
    i += 1
print("Round 2 score is",b)
print("ROUND 3")
i = 10
while i<= 14:
    print(l1[i])
    ans = input("Arrange the letters to form a valid word ")
    if ans in l2:
        print("Correct")
        c += 1
    else:
        print("Wrong")
        c -= 1
    i += 1
print("Round 3 score is",c)   