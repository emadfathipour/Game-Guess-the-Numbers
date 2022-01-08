

answer = input("player 1: please insert the number (1 - 100):")
answer = int(answer)

is_correct = False
try_count = 0
while try_count <10 and is_correct == False:
    guess = int(input("player 2 : please guess a number!"))
    if guess == answer:
        print("player 2: you won!")
        is_correct = True
    elif guess > answer:
        print("your guess is bigger than the answer.")
        try_count += 1
    else:
        print("your guess is smaller than the answer.")
        try_count += 1

if is_correct == False:
    print("player 2: you lost!")