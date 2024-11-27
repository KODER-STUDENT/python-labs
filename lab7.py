def evaluate_expression(expression):
    def precedence(op):
        """Пріоритет операцій"""
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def apply_operation(operands, operators):
        """Виконання операції"""
        b = operands.pop()
        a = operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(a + b)
        elif op == '-':
            operands.append(a - b)
        elif op == '*':
            operands.append(a * b)
        elif op == '/':
            operands.append(a / b)

    def is_digit_or_dot(ch):
        """Перевірка чи символ - цифра або крапка"""
        return ch.isdigit() or ch == '.'

    operands = []
    operators = []
    i = 0

    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue

        if expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                apply_operation(operands, operators)
            operators.pop()  # Видаляємо '('
        elif expression[i].isdigit() or expression[i] == '.':
            value = 0
            decimal_place = -1
            while i < len(expression) and is_digit_or_dot(expression[i]):
                if expression[i] == '.':
                    decimal_place = 0
                else:
                    value = value * 10 + int(expression[i])
                    if decimal_place >= 0:
                        decimal_place += 1
                i += 1
            i -= 1
            if decimal_place > 0:
                value = value / (10 ** decimal_place)
            operands.append(value)
        elif expression[i] in '+-*/':
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(expression[i])):
                apply_operation(operands, operators)
            operators.append(expression[i])
        i += 1

    while operators:
        apply_operation(operands, operators)

    return operands[-1]

expression = "3 + 5 * (2 - 8)"
result = evaluate_expression(expression)
print(f"Результат виразу '{expression}' дорівнює {result}")
