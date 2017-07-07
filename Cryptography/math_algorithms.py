"""
Copyright 2017 Nikolay Stanchev

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


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
