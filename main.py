y = int(input(":")) 

def staricaseONE(n):
    for i in range(1, n + 1):
        print(" "*(n-i) + "#"*i)

staricaseONE(y)
print("-"*x)
staircase = lambda n: [print(" "*(n-i) + "#"*i) for i in range(1, n + 1)]
staircase(y)