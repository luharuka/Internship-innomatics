
# The Minion Game



def minion_game(string):
    # your code goes here
    string = string.strip()
    totalScore = len(string)*(len(string)+1)/2
    scoreKevin = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(string)):
        if string[i] in vowels:
            scoreKevin += len(string)-i
    if scoreKevin>(totalScore-scoreKevin):
        print('Kevin', int(scoreKevin))
    elif scoreKevin == (totalScore-scoreKevin):
        print('Draw')
    else:
        print('Stuart', int(totalScore-scoreKevin))
if __name__ == '__main__':
    s = input()
    minion_game(s)