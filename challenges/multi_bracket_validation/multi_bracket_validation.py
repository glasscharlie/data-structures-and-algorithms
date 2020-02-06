def validation(string):
    open = ''
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '{' or string[i] == '[':
            open += string[i]
        if string[i] == ')':
            if open[len(open)-1] == '(':
                open = open[:(len(open)-1)]
            else:
                return False
        if string[i] == '}':
            if open[len(open)-1] == '{':
                open = open[:(len(open)-1)]
            else:
                return False
        if string[i] == ']':
            if open[len(open)-1] == '[':
                open = open[:(len(open)-1)]
            else:
                return False

    if open == '':
        return True
    else:
        return False       