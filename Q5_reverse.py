def reverse(string):
    stack = list(string)
    reverse = ''
    while stack:
        reverse += stack.pop()
    return reverse

string = "hello"
print(reverse(string))