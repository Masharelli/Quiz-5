
from ex11 import generate_n_chars


def histogram(li):
    for n in li:
        print generate_n_chars(n, '*')


if __name__ == "__main__":
    histogram([4, 9, 7])