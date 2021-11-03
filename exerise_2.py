from main import Stack

if __name__ == "__main__":
    test_cases = ("(((([{}]))))", "[([])((([[[]]])))]{()}", "{{[()]}}", "}{}", "{{[(])]}}", "[[{())}]")
    stack = Stack()
    for s in test_cases:
        print(s, stack.check(s))