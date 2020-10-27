p = str(input())
game = (1, 0, 0)

A = str()
B = str()
C = str()

for i in p:
    if i == 'A':
        game = (game[1], game[0], game[2])
    elif i == 'B':
        game = (game[0], game[2], game[1])
    else:
        game = (game[2], game[1], game[0])

if game == (1, 0, 0):
    print("1")
elif game == (0, 1, 0):
    print("2")
else:
    print("3")