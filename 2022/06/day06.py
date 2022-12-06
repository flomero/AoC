day = "06"
source = "data"
file = "C:/Users/flofi/repos/CodeImAdvent/2022/" + day + "/" + source + ".txt"

with open(file) as file:
    input = file.read()

input = [i for i in input]

answer = 0

def double_letters(word):
    for i in word:
        count = word.count(i)
        if count > 1:
            return False
    return True

for i, char in enumerate(input):
    if i < (len(input) - 3):
        word = [char, input[i+1], input[i+2], input[i+3]]
        if (double_letters(word)):
            if answer == 0:
                print(word)
                answer = (i + 4)

print(answer)

answerTwo = 0

for i, char in enumerate(input):
    if i < (len(input) - 13):
        word = []
        for j in range(14):
            word.append(input[i+j])
        if (double_letters(word)):
            if answerTwo == 0:
                print(word)
                answerTwo = (i + 14)

print(answerTwo)