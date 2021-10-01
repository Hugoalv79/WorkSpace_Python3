def checkPalindrome(inputString):
    test = inputString[::-1]
    if test == inputString:
        return True
    if test != inputString:
        return False
    
        
inputString = "abaa"

print(checkPalindrome(inputString))