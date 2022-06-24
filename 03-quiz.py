import json

points = 0


def show_question(question):
    global points

    print()
    print(question["question"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()

    answer = input("Whichever answer you choose? ")

    if answer == question["correct_answer"]:
        points += 1
        print("That's the correct answer, bravo! You already have", points, "points.")
    else:
        print("Unfortunately that's the wrong answer, the correct answer is " + question["correct_answer"] + ".")


with open("quiz.json", encoding="utf-8") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        show_question(questions[i])

print()
print("It's game over, the number of points scored is " + str(points) + ".")
