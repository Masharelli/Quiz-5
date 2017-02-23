def is_palindrome(string):
    return string == string[::-1]


if __name__ == "__main__":
    print is_palindrome("aabbaa")
    print is_palindrome("abc")
    print is_palindrome("radar")