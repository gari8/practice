def validate_format(chars: str) -> bool:
    stack = []
    for c in chars:
        if c == '(':
            stack.append(')')
        elif c == '{':
            stack.append('}')
        elif c == '[':
            stack.append(']')
        elif c == ')' or c == '}' or c == ']':
            if c in stack:
                if c != stack.pop():
                    return False
            else:
                return False
    if len(stack) == 0:
        return True

    return False


if __name__ == '__main__':
    json1 = '{"key1": "value1", "key2": [1, 2, 3], "key3": (1, 2, 3)}'
    json2 = '{"key1": ["value1", "key2": [1, 2, 3], "key3": (1, 2, 3)}'
    print(validate_format(json1))
    print(validate_format(json2))
