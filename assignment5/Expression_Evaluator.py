class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node
        self.size += 1

    def add_index(self, data, index):
        if index > self.size or index < 0:
            raise TypeError("")
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            p = self.head
            for i in range(0, index - 1):
                p = p.next
            u = p.next
            new_node.next = u
            p.next = new_node
        self.size += 1

    def list_print(self):
        p = self.head
        print("[", end=""),
        while p:
            if p.next:
                print(p.data, end=", ")
            else:
                print(p.data, end="")
            p = p.next
        print("]")

    def get_element(self, index):
        if self.not_in_bound(index):
            raise TypeError("")
        p = self.head
        for i in range(0, index):
            p = p.next
        return p.data

    def set_element(self, data, index):
        if self.not_in_bound(index):
            raise TypeError("")
        p = self.head
        for i in range(0, index):
            p = p.next
        p.data = data

    def not_in_bound(self, index) -> bool:
        return index >= self.size or index < 0

    def delete_element(self, index):
        if self.not_in_bound(index):
            raise TypeError("")

        if index == 0:
            p = self.head
            self.head = p.next
        else:
            cur = self.head
            prev = None
            for i in range(0, index):
                prev = cur
                cur = cur.next
            prev.next = cur.next
        self.size -= 1

    def clear(self):
        # while (self.size > 0):
        #   self.deleteElement(0)
        self.head = None
        self.size = 0

    def sublist(self, start_index, end_index):
        if self.not_in_bound(start_index) or \
                self.not_in_bound(end_index) or \
                end_index < start_index:
            raise TypeError("")
        p = self.head
        for i in range(0, start_index):
            p = p.next
        new_sublist = SingleLinkedList()
        for i in range(start_index, end_index + 1):
            new_sublist.add_last(p.data)
            p = p.next
        return new_sublist

    def is_empty(self):
        if self.size == 0 or self.head is None:
            return True
        return False

    def contains(self, data):
        p = self.head
        for i in range(self.size):
            if p.data == data:
                return True
            p = p.next
        return False

    def initialize(self, data):
        if data != "[]":
            data = data[1:-1]
            data = data.replace(" ", "").split(',')
            for i in range(len(data)):
                self.add_last(data[i])


class Stack(SingleLinkedList):
    def __init__(self):
        SingleLinkedList.__init__(self)
    def initialize(self, data):
        SingleLinkedList.initialize(self,data)
    def push(self, data):
        SingleLinkedList.add_index(self,data,0)
    def pop(self):
        data = SingleLinkedList.get_element(self,0)
        SingleLinkedList.delete_element(self,0)
        return data
    def peek(self):
        data = SingleLinkedList.get_element(self,0)
        return data
    def is_empty(self):
        return SingleLinkedList.is_empty(self)
    def stack_print(self):
        SingleLinkedList.list_print(self)
 
def is_operand(expr_char): 
    if expr_char == "a" or expr_char == "b" or expr_char == "c":
        return True
    else:
        return False

def is_operator(expr_char): 
    if expr_char == "+" or expr_char == "-" or expr_char == "*" or expr_char == "/" or expr_char == "^":
        return True
    else:
        return False
def notGreater(operator):
    try:
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        a = precedence[operator]
        b = precedence[mystack.peek()]
        return True if a <= b else False
    except KeyError:
        return False
def evaluatePostfix (exp):      
    # Iterate over the expression for conversion
    if (len(exp)==0):
        return 0
    else:
        eval_stack = Stack()
        for i in range(len(exp)):
            charecter = exp[i]
            # If the scanned character is an operand
            # (number here) push it to the stack
            if is_operand(charecter):
                eval_stack.push(get_val(charecter))
            # If the scanned character is an operator,
            # pop two elements from stack and apply it.
            else:
                if charecter == "^":
                    charecter = "**"
                val1 = eval_stack.pop()
                if charecter == "-":
                    try: 
                        val2 = eval_stack.pop()
                    except:
                        val2 = 0
                else:
                    val2 = eval_stack.pop()
                eval_stack.push(str(int(eval(str(val2) + charecter + str(val1)))))
        value = int(eval_stack.pop())
        if not(eval_stack.is_empty()):
            raise Exception
        return value
def get_val(character):
    if character == "a":
        return a
    elif character == "b":
        return b
    elif character == "c":
        return c
    else:
        return character

if __name__ == "__main__":
    try:
        mystack =   Stack()
        input_expr = input()

        if input_expr[0:2] == "--":
            input_expr = input_expr[2:]

        elif input_expr[0] == "+":
            input_expr = input_expr[1:]
        
        for i in range(len(input_expr)):
            if input_expr[i:i+2] == "--":
                if is_operand(input_expr[i-1]):
                    input_expr = input_expr[:i] + "+" + input_expr[i+2:]
                else:
                    input_expr = input_expr[:i] + "" + input_expr[i+2:]

        if is_operator(input_expr[len(input_expr)-1]):
            raise Exception
        # input_expr = input_expr.replace("--", "+")
        global a,b,c
        a = int(input("")[2:])
        b = int(input("")[2:])
        c = int(input("")[2:])

        output_expr=""
        for i in range (len(input_expr)):
            if is_operand(input_expr[i]):
                output_expr += input_expr[i]

            elif input_expr[i] == "(":
                mystack.push(input_expr[i])

            elif input_expr[i] == ")":
                while((not mystack.is_empty()) and mystack.peek() != '('):
                        temp = mystack.pop()
                        output_expr += temp
                if (not mystack.is_empty() and mystack.peek() != '('):
                    raise Exception
                else:
                    mystack.pop()

            elif is_operator(input_expr[i]):
                if input_expr[i] == "+" and  is_operator(input_expr[i-1]):
                    continue
                while(not mystack.is_empty() and notGreater(input_expr[i])):
                    output_expr += mystack.pop()
                mystack.push(input_expr[i])
    
            # pop all the operator from the stack
        while not mystack.is_empty():
            output_expr += mystack.pop()

        value = evaluatePostfix(output_expr)
        print (output_expr)
        print(evaluatePostfix(output_expr))
    except:
        print("Error")
