
data = ["Schools", "Houses", "Apartments", "racecar"]


def reverse(s):
    return s[::-1]


def is_palindrome(s):
    rev = reverse(s)
    return s == rev


def is_palindrome3(s):
    # Run loop from 0 to len/2
    for i in range(0, int(len(s)/2 + 1)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


print(is_palindrome3(data[3]))