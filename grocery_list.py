class Stack():
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        self.item.pop()

    def peek(self):
        return self.item[-1]

    def get_grocery_list(self):
        return self.item


s = Stack()
s.push("eggs")
s.push("bacon")
s.push("bread")
print(s.get_grocery_list())
