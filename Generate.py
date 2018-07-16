# delimeters

question_del = "Question:"
line_del = "#----"
hint_del = "Hint:"
solution_del = "Solution:"


def main():
    question = ""
    questionNumber = 0

    with open('Python_challenges.txt', 'r') as fp:
        data = fp.readlines()
        temp = -1
        questions = []
        for x in range(0, len(data)):
            print(data[x])
            current = data[x]
            if line_del in current:
                temp = temp * -1
                if question != "":
                    questions.append(str(question))
                    question = ""
            if temp == 1:
                question = question + current
        for x in range(0, len(questions)):
            question_number = x + 1
            temp = "challenge-" + str(question_number) + "/Question.txt"
            file = open(temp, 'w' )
            file.write(questions[x])
            file.close()
            print("[+]\t\tQuestion_FOUND!\n" + questions[x])

main()
