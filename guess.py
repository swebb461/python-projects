
qs = ["What number am i thinking of?",]

num = ["28", "12", "14", "9"]

while True:
    answer = input("Guess a number or type v to quit")
    if answer == "v":
	    break
    if answer in num:
        print("You guessed correctly.")
    else:
        print("Wrong")

