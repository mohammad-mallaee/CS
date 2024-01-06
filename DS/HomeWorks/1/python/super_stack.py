class SuperStack:
    def __init__(self) -> None:
        self.main_stack = list()
        self.aux_stack = list()
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def add_to_aux(self, x: int):
        if self.is_empty():
            self.aux_stack.append(x)
        elif self.aux_stack[self.top] <= x:
            last_aux_stack = self.aux_stack[self.top]
            self.aux_stack.append(last_aux_stack)
        else:
            self.aux_stack.append(x)

    def find_min(self):
        if self.is_empty():
            return None
        else:
            return self.aux_stack[self.top]

    def push(self, x: int):
        self.main_stack.append(x)
        self.add_to_aux(x)
        self.top += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            last_main_stack = self.main_stack[self.top]
            self.main_stack.pop(self.top)
            self.aux_stack.pop(self.top)
            self.top -= 1
            return last_main_stack
