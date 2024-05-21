def Lcs_Length(X, Y):
    m = len(X)
    n = len(Y)

    c = [[0] * (n + 1) for _ in range(m + 1)]
    b = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        c[i][0] = 0
    for j in range(n):
        c[0][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = '↖'
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = '↑'
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = '←'
    return c, b

def print_Lcs(b, X, i, j):
    a = 0
    if i == 0 or j == 0:
        return a
    if b[i][j] == '↖':
        a += 1
        return a + print_Lcs(b, X, i - 1, j - 1)
    elif b[i][j] == '↑':
        return print_Lcs(b, X, i - 1, j)
    else:
        return print_Lcs(b, X, i, j - 1)

    
while True:
    try:
        X = list(input())
        Y = list(input())
        c, b = Lcs_Length(X, Y)
        print(print_Lcs(b, X, len(X), len(Y)), end='\n')
    except EOFError:
        break

