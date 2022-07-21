import random
from random import seed, randint
import pandas
import numpy


def g(wd, sd, change=False):
    assert wd < 3
    assert wd >= 0

    rd = next(i for i in range(3) if i != sd and i != wd)

    if change:
        sd = next(i for i in range(3) if i != sd and i != rd)

    return sd == wd


if __name__ == "__main__":
    pd = numpy.random.random_integers(0, 2, (1000 * 1000 * 1,))

    wd = [d for d in pd if g(1, d)]
    print("Winning percentage without changing choice: ", len(wd) / len(pd))

    wd = [d for d in pd if g(1, d, change=True)]
    print("Winning percentage while changing choice: ", len(wd) / len(pd))
