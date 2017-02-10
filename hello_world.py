print 'hello,\'world!'
print 'this is a''test code''\''
i=5
i+=1
print i

number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer:'))
    if guess == number:
        print 'congratulations, you guessed it.'
        running = False
    elif guess < number:
        print 'no, it\'s a little higher than that'
    else:
        print 'no, it\' a little lower than that'

for i in range(1, 5):
    print i
else :
    print 'for loop is over'

while True:
    str = raw_input('Enter something:')
    if str == 'quit':
        break
    elif len(str) < 3:
        continue
    print 'Length of string is', len(str)

def sayhello(x, y):
    print 'hello! ', x, ' ',y

sayhello(3, 5)

print 'Done'