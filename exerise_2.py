from main import check
from main import Stack
### here we can check how parentheses work
if __name__ == "__main__":
    test_cases = ("(((([{}]))))", "[([])((([[[]]])))]{()}", "{{[()]}}", "}{}", "{{[(])]}}", "[[{())}]")
    for s in test_cases:
        print(s, check(s))
