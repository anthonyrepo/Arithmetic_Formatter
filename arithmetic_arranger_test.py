from arithmetic_arranger import arithmetic_arranger

def test_two_problems_arrangement1():
    result = arithmetic_arranger(['3801 - 2', '123 + 49'])
    assert result == '  3801      123\n-    2    +  49\n------    -----', 'Expected different output when calling "arithmetic_arranger()" with ["3801 - 2", "123 + 49"]'

def test_two_problems_arrangement2():
    result = arithmetic_arranger(['1 + 2', '1 - 9380'])
    assert result == '  1         1\n+ 2    - 9380\n---    ------', 'Expected different output when calling "arithmetic_arranger()" with ["1 + 2", "1 - 9380"]'

def test_four_problems_arrangement():
    result = arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'])
    msg = 'Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]'
    assert result == '    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----', msg

def test_five_problems_arrangement():
    result = arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'])
    msg = 'Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]'
    assert result == '  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------', msg

def test_too_many_problems():
    result = arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'])
    assert result == 'Error: Too many problems.', 'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."'

def test_incorrect_operator():
    msg = """Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."""
    result = arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49'])
    assert result == "Error: Operator must be '+' or '-'.", msg

def test_too_many_digits():
    msg = 'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits.'
    result = arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'])
    assert result == 'Error: Numbers cannot be more than four digits.', msg

def test_only_digits():
    result = arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'])
    msg = 'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."'
    assert result == 'Error: Numbers must only contain digits.', msg

def test_two_problems_with_solutions():
    result = arithmetic_arranger(['3 + 855', '988 + 40'], True)
    msg = 'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with ["3 + 855", "988 + 40"] and a second argument of `True`.'
    assert result == '    3      988\n+ 855    +  40\n-----    -----\n  858     1028', msg

def test_five_problems_with_solutions():
    result = arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)
    msg = 'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with five arithmetic problems and a second argument of `True`.'
    assert result == '   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028', msg