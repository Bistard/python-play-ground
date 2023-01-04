import xlrd
import random

#
print('Welcome to the VOCAB-CHECKER')
print('If you wanna quit, please enter:\'QUIT\'')
print('---------------------------')
print('---------------------------')
print('---------------------------')
# Open excel
data = xlrd.open_workbook('HOD.xlsx')
# Get data
table = data.sheets()[0]
# Get rows and columns
rows = table.nrows
cols = table.ncols
# how many vocab you just did
count = 0
#
Round = int(input('How many Vocab you wanna do?:'))
correct = 0
wrong = 0
while count != Round:
    count += 1
    # all the x of vocabs
    all_vocabs = list(range(0, rows))
    # cell location of the answer
    true_vocab_y = 0
    true_vocab_x = random.randint(0, rows - 1)
    # randomly pick one
    random_vocab_pick = table.cell(true_vocab_x, true_vocab_y).value
    # 4 OPTIONS
    options = []
    # True
    true_explaination = table.cell(true_vocab_x, 2).value
    # False
    for false_explaination in range(0, 3):
        false_vocab_x = random.choice(all_vocabs)
        all_vocabs.remove(false_vocab_x)  # prevent repetition
        false_explaination = table.cell(false_vocab_x, 2).value
        options.append(false_explaination)
    options.append(true_explaination)
    # Random order
    ABCD = ['A', 'B', 'C', 'D']
    abcd = ['a', 'b', 'c', 'd']
    print('Q' + str(count) + ':')
    for order in range(0, 4):
        option = random.choice(options)
        options.remove(option)
        print(ABCD[order] + ':' + option + '\n')
        # Give the right answer a value
        if option == true_explaination:
            answer = order
    # Get UserInput
    UserInput = input(random_vocab_pick + ':')
    # Checking
    if UserInput == 'QUIT' or UserInput == 'quit':
        quit()
    elif UserInput == ABCD[answer] or UserInput == abcd[answer]:
        print('CORRECT!!!')
        correct += 1
    else:
        print('\n' + 'WRONG!!!')
        print(ABCD[answer] + ' is correct!!!')
        wrong += 1

    print('---------------------------')
print('Your correct percentage is:')
print(str(correct/int(correct+wrong)*100)+'%')
input()
