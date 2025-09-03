import random

def get_ans(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return "Number"

def play():
    logic = 0
    score=0
    previous_num=0
    while True:
        num=random.randint(1, 30)
        logic =previous_num+ num
        print("Number on screen:", num)
        guess = input("Your guess (fizz|buzz|fizzbuzz|Number): ").strip()
        correct = get_ans(logic)
        if guess.lower() == correct.lower():
            print("Correct!")
            score += 1
            previous_num = num
        else:
            print("Answer was:", correct)
            print("Hidden number was:", logic)
            cont = input("Do you want to continue? (yes|no): ").strip().lower()
            if cont != "yes":
                print("Your final score is:", score)
                score = 0
                logic = 0
                previous_num = 0
                break
    print("Your final score is:", score)
play()