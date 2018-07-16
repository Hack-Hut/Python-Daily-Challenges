def main():
    for x in range(1, 100):
        question = "challenge-" + str(x) + "/temp.txt"
        with open(question, 'r') as f:
            lines = f.readlines()
        question_a = ""
        for y in range(0, len(lines)):
            current = lines[y]
            if current == "Hints:\n":
                print(question_a)
                print("Hint Found")
                temp = "challenge-" + str(x) + "/Question.txt"
                wr = open(temp, 'w')
                wr.write(question_a)
                wr.close()
                question_a = ""
                break
            else:
                question_a += current

main()


# temp = "challenge-" + str(question_number) + "/Question.txt"
#             file = open(temp, 'w' )
#             file.write(questions[x])
#             file.close()