

class ActivationRecord:
    def __init__(self, function_name, return_address):
        self.function_name = function_name
        self.return_address = return_address
        self.local_variables = {}

    def set_variable(self, var, value):
        self.local_variables[var] = value

    def get_variable(self, var):
        return self.local_variables.get(var, None)

    def __str__(self):
        return f"{self.function_name} | Locals: {self.local_variables}"


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ar):
        print(f"\nPUSH: {ar.function_name}")
        self.stack.append(ar)
        self.display()

    def pop(self):
        if self.stack:
            ar = self.stack.pop()
            print(f"\nPOP: {ar.function_name}")
            self.display()
            return ar

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def display(self):
        print("\n--- Stack State ---")
        for i, ar in enumerate(reversed(self.stack)):
            print(f"{i}: {ar}")
        print("-------------------")



stack = Stack()


main_ar = ActivationRecord("main", "start")
main_ar.set_variable("a", 10)
stack.push(main_ar)


foo_ar = ActivationRecord("foo", "main")
foo_ar.set_variable("x", 20)
stack.push(foo_ar)


bar_ar = ActivationRecord("bar", "foo")
bar_ar.set_variable("y", 30)
stack.push(bar_ar)


stack.pop()


stack.pop()


stack.pop()