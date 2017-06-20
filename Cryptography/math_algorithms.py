def gcd(a, b, solve_equation=False):
    assert type(a) is int and type(b) is int, "Arguments for greatest common divisor must be integers"

    remainder = None
    if a >= b:
        quotients = []
        while remainder != 0:
            remainder = a % b
            quotient = a // b
            a = b
            b = remainder
            quotients.append(quotient)

        if solve_equation:
            x = [0, 1]
            y = [1, 0]

            for i in range(2, len(quotients)+1):
                x.append(x[i-2] - x[i-1]*quotients[i-2])
                y.append(y[i - 2] - y[i - 1]*quotients[i - 2])

            return a, (x[len(x)-1], y[len(y) - 1])

        else:
            return a

    else:
        return gcd(b, a, solve_equation=solve_equation)


def find_multiplicative_inverse(a, n):
    assert type(a) is int and type(n) is int, "Argument for multiplicative inverse must be integer"

    a = a % n

    result = gcd(a, n, solve_equation=True)

    assert result[0] == 1, "The arguments must be relatively prime"

    return result[1][0]
