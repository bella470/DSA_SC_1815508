m, d = map(str, input().split())

if (m == str('OCT') and d == str('31')) or (m == str('DEC') and d == str('25')):
    print("yup")
else:
    print("nope")
