import random

def random_numbers():
    answer = ''
    for i in range(4):
        num = random.randrange(0, 9)
        answer += str(num)
        if (i != 3):
            answer += ':'
    return answer

def guessA(guess, answer):
    round = ''
    remaining = list(answer)
    for i in range(len(guess)):
        if guess[i] == ':':
            round += ':'
        else:
            if guess[i] == answer[i]:
                round += 'e'
                remaining.remove(guess[i])
            elif guess[i] in remaining:
                round += 'p'
                remaining.remove(guess[i])
            else:
                round += '0'
    return round