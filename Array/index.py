# QUESTIONS FROM CRACKING THE CODING INTERVIEW CHAPTER ONE PAGE 90

def is_unique(string):
    res = set(string)
    if len(res) == len(string):
        return True
    return False
# a = 'ABCDEFGG'
# print(is_unique(a))

def is_permutation(str1,str2):
    if len(str1) != len(str2):
        return False
    arr = [0]*255
    for char in str1:
        arr[ord(char)]+=1
    for char in str2:
        arr[ord(char)]-=1
    for num in arr:
        if num != 0:
            return False
    return True

# one = 'acdb'
# two = 'cbad'
# print (is_permutation(one,two))

def URLify(str1):
    return str1.strip().replace(' ','%20')
    
# arr = 'Mr John Smith  '
# print(URLify(arr))






# CHAPTER ONE PAGE 91
def palindrome_permutation(str1):
    result = str1.lower().replace(' ','')
    H = dict()
    for char in result:
        if char in H:
            H[char]+=1
        else:
            H[char]=1
    if len(result) %2 == 0:
        for value in H.values():
            if value %2 != 0:
                return False
        return True
    else:
        count = 0
        for value in H.values():
            if value %2 != 0:
                if count >0:
                    return False
                count +=1 
        return True



print(palindrome_permutation('Tact Coa')) # tacocat is a palindrome 





