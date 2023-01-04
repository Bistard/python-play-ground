while True:
    base = 2
    column = 0
    OUTPUT = []
    INPUT = int(input('Please enter a DECIMAL:'))
    while True:
        binary = base**column
        if INPUT >= binary:
            column += 1
        else:
            column -= 1
            binary = base**column
            break
    while column >= 0:
        if INPUT >= binary:
            INPUT -= binary
            column -= 1
            binary = base**column
            OUTPUT.insert(len(OUTPUT),1)
        else:
            column -= 1
            binary = base**column
            OUTPUT.insert(len(OUTPUT),0)
    while len(OUTPUT) % 4 != 0:
        print(OUTPUT)
        OUTPUT.insert(0,0)
    print(OUTPUT)