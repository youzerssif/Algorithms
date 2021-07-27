
import time
start_time = time.time()


def inverse_chaine3(s):
    return s[::-1]

print("La fonction 3 ",inverse_chaine3('bonjour third'))
print("--- %s seconds function 3 ---" % (time.time() - start_time))

def inverse_chaine2(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1

print("La fonction 2 ",inverse_chaine2('bonjour second'))
print("--- %s seconds function 2 ---" % (time.time() - start_time))




def inverse_chaine(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1
print("La fonction 1 ",inverse_chaine('bonjour first'))
print("--- %s seconds function 1 ---" % (time.time() - start_time))


