A, B = map(int, input().split())

reverseA = int(str(A)[:: -1])
reverseB = int(str(B)[:: -1])

if reverseA > reverseB:
    print(reverseA)
elif reverseB > reverseA:
    print(reverseB)