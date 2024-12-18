mN = int(input())
P,C,Q = input().split()
P = int(P)
Q = int(Q)

if C == '+':
    if P+Q > mN:
        print("OVERFLOW")
    else:
        print("OK")
elif C == '*':
    if P*Q > mN:
        print("OVERFLOW")
    else:
        print("OK")