print("Welcome to my quiz game!")

play = input("Do you want to play?\nIt is a fun science game. " )
score = 0

if play.lower() == "yes":
    print("Okay! Let's get ready to rumble")
else:
    print("Sorry to see you go.")
    quit()

question_1 = int(input("How many elements are on the periodic table. "))

if question_1 == 118:
    print("correct")
    score += 1
else:
    print("incorrect")

question_2 = input("What is the 17th element. ")

if question_2.lower() == "chlorine" or "Cl":
    print("correct")
    score += 1
else:
    print("incorrect")
 
question_3 = input("What is the chemical symbol for gold. ")

if question_3 == "Au":
    print("correct")
    score += 1
else:
    print("incorrect")
 
question_4 = input("What is the metal with the highest melting point. ")

if question_4.lower() == "tungsten":
    print("correct")
    score += 1
else:
    print("incorrect")
    
question_5 = input("What is the chemical formula for sodium chloride. ")

if question_5 == "NaCl":
    print("correct")
    score += 1
else:
    print("incorrect")

if score > 3:
    print(f"Congratulations, you've passed.\nYou had {(score/5 )*100}%, well done!")
else:
    print(f"You've got to try harder.\nYou had {(score/5 )*100}%, better luck next time")
 
     

