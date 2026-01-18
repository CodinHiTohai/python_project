question=[["who is the first prime minister of india","modi","jawaharlalnehru","manmohan singh",2],
         ["what is the nation seets of india","rasogullas","jalebi","gulabjamun",2],
         ["who play  crikect for indin and score 264 runs","kohli","rohit","dhoni",2],
   
         ["capital of india","punjab","delhi","bihar",2]]
prize=[10,100,1000,10000,100000]
i=0;
for question in question:
    
    print(f"{question[0]}")
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")

    a=int(input("enter the answer 1 for a 2 for b anc c for 3"))
    if(question[4]==a):
        print("correct answer")
    else:
        print(f"the correct answer was {question[4]}")
        print("better luck next time")
        break;
    
    print(f"you won {prize[i]}")
    i+=1;