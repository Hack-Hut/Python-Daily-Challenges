def main():
    for x in range(1, 100):
        question = "challenge-" + str(x) + "/Question.txt"
        with open(question, 'r') as f:
            lines = f.readlines()
        current = ""
        for y in range(0, len(lines)):
            current += "#\t" + lines[y]
        temp = "challenge-" + str(x) + "/Attempt.py"
        wr = open(temp, 'w')
        wr.write(current)
        wr.close()
        current = ""

main()