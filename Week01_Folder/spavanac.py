H, M = map(int, input().split())

if H == 0:
    H = 24

if M < 45:
    H = H-1
    M = M+60

M = M-45
print(H, M)
