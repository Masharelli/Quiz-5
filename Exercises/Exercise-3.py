def length(string):
    count = 0
    for i in string:
        count += 1
    return count


if __name__ == "__main__":
    print length("test string")