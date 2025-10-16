class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        if not self.queue1:
            self.queue1.append(x)
        else:
            for num in self.queue1[:]:
                self.queue2.append(num)
                self.queue1.remove(num)
            self.queue1.append(x)
            for num in self.queue2[:]:
                self.queue1.append(num)
                self.queue2.pop(0)

    def pop(self) -> int:
        if not self.queue1:
            return None
        x = self.queue1.pop(0)
        return x

    def top(self) -> int:
        if self.queue1:
            return self.queue1[0]
        else:
            return None

    def empty(self) -> bool:
        if not self.queue1:
            return True
        else:
            return False

    def seen(self):
        return self.queue1


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(7)
obj.push(8)
print(obj.seen())

