with open('day_2_input.txt', 'r') as f:
    rounds = f.read().split('\n')
    f.close()

def Part1(rounds):
    possibleOutcomes = {'A X': 3 + 1, 'A Y': 6 + 2, 'A Z': 0 + 3, 
                'B X': 0 + 1, 'B Y': 3 + 2, 'B Z': 6 + 3, 
                'C X': 6 + 1, 'C Y': 0 + 2, 'C Z': 3 + 3}
    score = sum(possibleOutcomes[i] for i in rounds)
    return score

def Part2(rounds):
    possibleOutcomes = {'A X': 0 + 3, 'A Y': 3 + 1, 'A Z': 6 + 2, 
                'B X': 0 + 1, 'B Y': 3 + 2, 'B Z': 6 + 3, 
                'C X': 0 + 2, 'C Y': 3 + 3, 'C Z': 6 + 1}
    score = sum(possibleOutcomes[i] for i in rounds)
    return score

print("Total score for Part 1: %d" %Part1(rounds))
print("Total score for Part 1: %d" %Part2(rounds))
