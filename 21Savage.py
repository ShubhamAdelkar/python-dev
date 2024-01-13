#WHILE LOOP

password = "21savage"
checkIn = False
passcode = ""
guessCount = 0
guessLimit = 3
outOfGuess = False

while passcode != password and not(outOfGuess):
    if guessCount < guessLimit:
      passcode = input("Please enter password: ")
      guessCount += 1
    else:
       outOfGuess = True

if outOfGuess == True:
   print("Out of Guess, You lose!")
else: 
   print("Correct, You Win!")
