def arithmetic_arranger(expressions, answer=False):
    if len(expressions) > 5:
        return 'Error: Too many problems.'
        
    components = []
    
    for expression in expressions:
        components.append(expression.split())
        
    for expression in components:
        if expression[1] != '+' and expression[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if expression[0].isdigit() == False or expression[2].isdigit() == False:
            return "Error: Numbers must only contain digits."
        if len(expression[0]) > 4 or len(expression[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            
    for expression in components:
        longest_length = 0
        if len(expression[0]) > longest_length:
            longest_length = len(expression[0])
        if len(expression[2]) > longest_length:
            longest_length = len(expression[2])
        expression.append(longest_length)
        
    first_line = ''
    second_line = ''
    third_line = ''
    for expression in components:
        first_line = first_line + expression[0].rjust(expression[3] + 2) + '    '
        second_line = second_line + expression[1] + ' ' + expression[2].rjust(expression[3]) + '    '
        third_line = third_line + ''.rjust(expression[3] + 2, '-') + '    '
        
    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    third_line = third_line.rstrip()
    
    if answer == True:
        for expression in components:
            if expression[1] == '+':
                expression.append(int(expression[0]) + int(expression[2]))
            elif expression[1] == '-':
                expression.append(int(expression[0]) - int(expression[2]))

        fourth_line = ''
        for expression in components:
            fourth_line = fourth_line + str(expression[4]).rjust(expression[3] + 2) + '    '
        fourth_line = fourth_line.rstrip()
            
        return first_line + '\n' + second_line + '\n' + third_line + '\n' + fourth_line
        
    return first_line + '\n' + second_line + '\n' + third_line

print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
print(repr(arithmetic_arranger(['3 + 855', '988 + 40'], True)))