
data = ["Schools", "Houses", "Apartments", "racecar"]

def reverse(str):
    return str[::-1]

def isPalendrome(str):
    rev = reverse(str)
    return str == rev

def isPalendrome3(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2 + 1)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

print(isPalendrome3(data[3]))