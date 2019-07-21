import random
print("Welcome to code braker game!!!")
print("Guess what number I am thinking of, I will tell your guess is match or close or nope")
print("Let's play!!!")
#fuct to get the guess number from user

def get_guess():
    return list(input("what is your guess user?"))
#funct to generate computer code

def generate_code():
    digits= [str(num) for num in range (10)]
    #it will shuffle the digits from 0 to 9 and returns first 3 digits
    random.shuffle(digits)
    return digits[:3]
#clue generation
#1-checks for code and u_guess if it's same then code cracke 2-checks num and code's index are same if
#same then match or else clode 3- nothing matches in code then nope
def generate_clue(code,user_guess):
    if user_guess==code:
        return "CODE CRACKED !!! YOU ARE A GENIUS"
        
    clues=[]
    for indx,num in enumerate(user_guess):
        if num == code[indx]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    
    if clues == []:
        return ["Nope"]
    else:
        return clues

#main funct
secret_code=generate_code()
clue_guess = []

while clue_guess != "CODE CRACKED !!! YOU ARE A GENIUS":
     
     guess=get_guess()
     clue_guess=generate_clue(guess,secret_code)
     print("here is the result : ")
     for clue in clue_guess:
         print(clue)
         

#while loop runs till clue guess gets equal to the string code cracked you are GENIUS














    