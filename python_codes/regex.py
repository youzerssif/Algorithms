# def CodelandUsernameValidation(strParam):

#   # code goes here
#   import re
#   pattern = "^(?=[a-zA-Z0-9._]{4,25}$)[^_.].*[^_.]$"
#   result = re.match(pattern, str(strParam))
  
#   if result:
#     return True
#   else:
#     return False

# # keep this function call here 
# print(CodelandUsernameValidation(input()))

import re

pattern = '^a...s$'
test_string = "acc?7??sss?3rr1??????5"
not_qmark_digit = r'[^?\d]*'
# contiguous blocks of non-digit with exactly three question mark
three_qmark = '(?:' + not_qmark_digit + r'\?){3}' + not_qmark_digit
result = re.findall(three_qmark, test_string)

True if result else False
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")	