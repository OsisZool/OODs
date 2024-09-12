def valid_parentheses(str):
    if len(str) == 0 :
        return True
    if '(' in str and ')' in str:
        open_index = str.index('(')
        close_index = str.index(')')
        if open_index < close_index :
            return valid_parentheses(str[:open_index]+ str[open_index +1:close_index] + str[close_index+1:])
    return False

print(valid_parentheses("(()()(())())"))
print(valid_parentheses("((()()"))
print(valid_parentheses("())()()("))
print(valid_parentheses("(((()))((())))"))
print(valid_parentheses("()()(((())))"))
print(valid_parentheses("()"))