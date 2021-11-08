
#class for exerice 1
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == 0
    #will check if the list id emplty, if it emplty it will say "True"
    # and if its not emplty it will say "False"

    def push(self, item):
        self.items.append(item)
        #this one push new item into the list as the last item

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None
    # will pop the last item in the list out of the list

    def peek(self):
        return self.items[len(self.items)-1]
    ## return you the last item from the list

    def size(self):
        return len(self.items)
    ## will tell the the number of items in the list



def check(list):
    stack = Stack()
    parentheses = {"{": "}", "(": ")", "[": "]"}

    for item in list:
        if item in "{[(":
            stack.push(item)
        elif stack.items and item == parentheses[stack.items[-1]]:
            stack.pop()
        else:
            return False
    return stack.size() == 0
### this function will check parentheses and see if they are balanced or not



## to check how exerise 1 turns out
if __name__ == "__main__":
    stack = Stack()
    print(stack.isEmpty())
    stack.push('1')
    stack.push('3')
    stack.push('8')
    stack.push('6')
    stack.pop()
    print('-------------')
    print(check("(((([{}]))))"))
    print('-------------')
    print(stack.size())
    print(stack.peek())
    print(stack.isEmpty())
    print(stack.items)


