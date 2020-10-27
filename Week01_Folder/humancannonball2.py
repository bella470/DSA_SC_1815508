import math

N = int(input())
t = float()

for i in range(N):
    V, T, X, H1, H2 = map(float, input().split())
    T = T*3.14159/180
    t = X / (V*math.cos(T))
    y = (V*t*math.sin(T)) - (0.5*9.81*(pow(t, 2)))
    if H1 + 1 < y < H2 - 1:
        print("safe")
    else:
        print("not safe")
