import random

def random_numbers():
    digits = list('0123456789')
    random.shuffle(digits)
    chosen = digits[:4]
    return ':'.join(chosen)

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