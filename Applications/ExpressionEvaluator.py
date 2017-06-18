# Evaluating mathematical expressions using a stack, tokens must be separated by a space
from ADTs.AbstractDataStructures import Stack


# the priorities of the attributes
operators_priorities = {"+": 1, "-": 1, "*": 2, "/": 2, '(': 0, ')': 0}


# the adjust_stacks method which takes as arguments the operands' stack, the operators' stack and the current token,
# which is expected to be an operator
def adjust_stacks(operands, operators, current_token):
    # using the global variable operators_priorities
    global operators_priorities

    # while the operators' stack is empty and the priority of the current token is less than or equal to the priority
    # of the top operator in the stack, adjust the stack
    while (not operators.is_empty()) and operators_priorities[current_token] <= operators_priorities[operators.peek()]:
        # popping the last operator with the last two operands
        operator = operators.pop()
        b = operands.pop()
        a = operands.pop()

        # evaluating the value of the simple expression and pushing it back into the stack
        if operator == "*":
            operands.push(a*b)
        elif operator == "/":
            operands.push(a/b)
        elif operator == "+":
            operands.push(a+b)
        elif operator == "-":
            operands.push(a-b)
        # if the operator is not from the supported ones, raise an exception
        else:
            raise ValueError("The attribute you are specifying is not supported")


# the adjust_parenthesis method, which takes as arguments the operands' stack and the operators' stack
def adjust_parenthesis(operands, operators):
    # get the last operator
    operator = operators.pop()

    # while the last operator is not a '(', evaluate simple expressions
    while operator != "(":
        # get the last two operands
        b = operands.pop()
        a = operands.pop()

        # evaluating the value of the simple expression and pushing it back into the stack
        if operator == "*":
            operands.push(a * b)
        elif operator == "/":
            operands.push(a / b)
        elif operator == "+":
            operands.push(a + b)
        elif operator == "-":
            operands.push(a - b)
        # if the operator is not from the supported ones, raise an exception
        else:
            raise ValueError("The attribute you are specifying is not supported")

        # popping the last operator again
        operator = operators.pop()


# the check_parenthesis method, which checks whether the parenthesis in the expression are valid
def check_parenthesis(expression):
    # the stack for the parenthesis
    parenthesis = Stack()

    # pushing all the left parenthesis in a stack
    for token in tokenize(expression):
        if token == "(":
            parenthesis.push(token)

        # if there's a right parenthesis, check if the stack is empty, that is there is no left parenthesis left
        elif token == ")":
            if parenthesis.is_empty():
                return False
            else:
                parenthesis.pop()

    # at the end, if the stack is empty, return true, all the parenthesis are valid; otherwise, return false
    return parenthesis.is_empty()


# the evaluate_expression method, which takes as argument a mathematical expression as a string
# and evaluates the value of it, assertion error is thrown if a non string object is passed as an argument
def evaluate_expression(expression):

    assert type(expression) is str, "Expression must be a string object"

    # check for errors in parenthesis
    if not check_parenthesis(expression):
        raise ArithmeticError("Invalid parenthesis")

    # using the global variable operators_priorities
    global operators_priorities

    # tokenizing the expression and initializing the two stack for the operands and the operators
    tokens = tokenize(expression)
    operands = Stack(elements_type=float)
    operators = Stack(elements_type=str)

    # iterating through the the tokens of the expression
    for token in tokens:
        # pushing the token into the right stack
        try:
            # if the token is a number push into operands stack
            operands.push(float(token))
        # if the token is one of these '(', ')', '*', '/', '+' or '-'
        except ValueError:
            try:
                # if the operators' stack is empty, add the token there
                if operators.is_empty():
                    operators.push(token)

                # if the operator is a '(', add the token to the stack
                elif token == "(":
                    operators.push(token)

                # if the operator is a ')', call the adjust_parenthesis method
                elif token == ")":
                    adjust_parenthesis(operands, operators)

                # if the last operator's priority is less than or equal to the priority of the current operator,
                # add the current operator to the stack again
                elif operators_priorities[operators.peek()] <= operators_priorities[token]:
                    operators.push(token)

                # if the last operator's priority is greater than the priority of the current operator,
                # call the method adjust_stacks and push the operator into the operators' stack
                elif operators_priorities[operators.peek()] > operators_priorities[token]:
                    adjust_stacks(operands, operators, token)
                    operators.push(token)
            # if the token is not supported, raise a Value error
            except KeyError:
                raise ValueError("Non supported attribute in the expression")

    # when we went through all the tokens, check if there's only one value left in the operands' stack and 0 operators
    # in the operators' stack, only then we know we are finished
    if operands.size() != 1 and operators.size() != 0:
        # if the finishing property is not true, then we repeat the operation from the adjust_stacks method,
        # while we know that we are finished
        while operands.size() != 1 and operators.size() != 0:
            # popping the last operator with the last two operands
            operator = operators.pop()
            b = operands.pop()
            a = operands.pop()

            # evaluating the value of the simple expression and pushing it back in the stack
            if operator == "*":
                operands.push(a * b)
            elif operator == "/":
                operands.push(a / b)
            elif operator == "+":
                operands.push(a + b)
            elif operator == "-":
                operands.push(a - b)
            # if the operator is not from the supported ones, raise an exception
            else:
                raise ValueError("The attribute you are specifying is not supported")

        # when we are finished, the operands' stack contains only the result from the expression, so we pop it
        return operands.pop()

    # if we know we are finished, we directly pop the result, since the operands' stack contains only the
    # result from the expression
    else:
        return operands.pop()


# tokenizer, which splits the string expression by splitting operands from operators
def tokenize(expression):
    tokens = []
    import re
    global operators_priorities
    for operator in operators_priorities.keys():
        expression = expression.replace(operator, " " + operator + " ")
    for token in re.split(r'\s+', expression):
        if token != '':
            tokens.append(token)
    return tokens
