"""Check the two orbit-type calculations in finite cyclic coordinates.

Interpret the first coordinate as 1/m of a turn along the upstairs circle.
The second is the index among the sphere point's different translates.
"""
from math import gcd


def sphere_index(polar, j, m):
    return 0 if polar else j % m


def replay():
    models = 0
    for m in range(2, 65):
        for polar in (False, True):
            # The diagonal images of a start state (0,0).
            deck = {(j % m, sphere_index(polar, j, m)) for j in range(m)}
            assert len(deck) == m
            # The lifted first-factor orbit runs at fixed sphere coordinate 0.
            first_return = next(j for j in range(1, m+1) if (j % m, 0) in deck)
            assert first_return == (1 if polar else m)
            order = m // gcd(first_return, m)
            assert order == (m if polar else 1)
            for n in range(2*m+1):
                endpoint = (n * first_return) % m
                assert (endpoint == 0) == (n % order == 0)
            models += 1
    print(f'PASS: {models} polar and nonpolar models for orders 2 through 64')
    print('PASS: primitive period, sheet displacement and first closed iterate')
    print('m=3 primitive polar endpoints: 1, 2, 0; nonpolar endpoints: 0, 0, 0')


if __name__ == '__main__':
    replay()
