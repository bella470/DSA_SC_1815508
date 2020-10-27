X, Y, N = map(int, input().split())

for i in range(N):
    if ((i + 1) % X == 0) and ((i + 1) % Y == 0):
        print("FizzBuzz")
    elif (i + 1) % X == 0:
        print("Fizz")
    elif (i + 1) % Y == 0:
        print("Buzz")
    else:
        print(i + 1)
