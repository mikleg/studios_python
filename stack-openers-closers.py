def validate(string):
    stack = Stack()
    for st in string:
        if st in "})]":
            if stack.size > 0:
                symbol = stack.pop()
            else:
                return False
            if symbol == "(" and st != ")" or symbol == "[" and st != "]" or symbol == "{" and st != "}":
                return False
        if st in "{([":
            stack.push(st)
    if stack.size == 0:
        return True
    else:
        return False  