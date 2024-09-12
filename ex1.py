def isPalindrome(str) :
    n = len(str)
    if n == 0 or n == 1 :
        return True
    elif str[0] == str[-1]:
        return isPalindrome(str[1:-1])
    else:
        return False

print(isPalindrome("abcdcba"))
print(isPalindrome("atoyota"))
print(isPalindrome("kmitl"))
print(isPalindrome("manassanan"))
print(isPalindrome("programming"))
print(isPalindrome("fundamental"))