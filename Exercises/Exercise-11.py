def generate_n_chars(n, c):
    result = ''
    for i in range(n):
        result += c
    return result


if __name__ == "__main__":
    print generate_n_chars(3, 'c')