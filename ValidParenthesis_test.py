import ValidParenthesis

def test_ValidParenthesis():
    assert ValidParenthesis.check_valid_parenthesis("()") == True
    assert ValidParenthesis.check_valid_parenthesis("()[]{}") == True
    assert ValidParenthesis.check_valid_parenthesis("(]") == False
    assert ValidParenthesis.check_valid_parenthesis("([)]") == False
    assert ValidParenthesis.check_valid_parenthesis("{[]}") == True
    assert ValidParenthesis.check_valid_parenthesis("") == True #empty string should return true
    assert ValidParenthesis.check_valid_parenthesis("((((((()))))))") == True
    assert ValidParenthesis.check_valid_parenthesis("((") == False
    assert ValidParenthesis.check_valid_parenthesis("())") == False
    assert ValidParenthesis.check_valid_parenthesis("(([]){})") == True
    assert ValidParenthesis.check_valid_parenthesis("({})[]{(){}}()") == True
    assert ValidParenthesis.check_valid_parenthesis("({})[]{(){}}(") == False