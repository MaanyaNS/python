print("Welcome to my computer quiz!")

playing=input("DO you want to play?\n")

if playing.lower()!="yes":
    quit()
    
else:
    print("Lets play!")

score=0

answer=input("What does CPU stands for?\n")
if answer.lower()=="central processing unit":
    print("✅")
    score+=1
else:
    print("❌")

answer=input("What does RAM stands for?\n")
if answer.lower()=="random access memory":
     print("✅")
     score+=1
else:
    print("❌")

answer=input("What does ROM stands for?\n")
if answer.lower()=="read only memory":
     print("✅")
     score+=1
else:
    print("❌")

answer=input("What does GPU stands for?\n")
if answer.lower()=="graphics processing unit":
     print("✅")
     score+=1
else:
    print("❌")

print("You got "+ str(score) +" questions right")
print("Your score is "+ str((score/4)*100)+"%")

