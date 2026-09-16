


def show_header():
    
    print("===== GENERAL KNOWLEDGE QUIZ =====\n")


def main():
    
    show_header()

    
    print("Question 1: What is the capital of France?")
    answer1 = input("Your answer: ")

    
    answer1 = answer1.strip().lower()

    if answer1 == "paris":
        score = score + 1
        print("Correct! +1 point\n")
    else:
        print("Wrong answer!\n")

   
    print("Question 2: How many days are in a week?")
    answer2 = input("Your answer: ")
    answer2 = answer2.strip().lower()

    if answer2 == "7":
        score = score + 1
        print("Correct! +1 point\n")
    else:
        print("Wrong answer!\n")

    
    print("Question 3: What is the color of the sky?")
    answer3 = input("Your answer: ")
    answer3 = answer3.strip().lower()

    if answer3 == "blue":
        score = score + 1
        print("Correct! +1 point\n")
    else:
        print("Wrong answer!\n")

    
    print("===== QUIZ RESULT =====")
    print(f"Your final score: {score}/3")


if __name__ == "__main__":
    main()