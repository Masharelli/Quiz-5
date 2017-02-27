
def max_in_list(li):
    max = li[0]
    for n in li:
        if n > max:
            max = n
    return max


if __name__ == "__main__":
    print max_in_list([1, 2, 5, 3])