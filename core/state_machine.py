class StateMachine:
    def __init__(self): self.state_stack = []
    def push(self, state): self.state_stack.append(state)
    def pop(self):
        if self.state_stack: return self.state_stack.pop()
    def peek(self): return self.state_stack[-1] if self.state_stack else None
