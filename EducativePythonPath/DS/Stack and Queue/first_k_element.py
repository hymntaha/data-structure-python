class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size

    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -= 1
        return self.stack_list.pop()

class MyQueue:
    def __init__(self):
        self.queue_list = []
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def size(self):
        return self.queue_size

    def enqueue(self, value):
        self.queue_size += 1
        self.queue_list.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        self.queue_size -= 1
        return front

def reverseK(queue, k):
    if queue.is_empty() or k > queue.size() or k<0:
        return None
    stack = MyStack()

    for i in range(k):
        stack.push(queue.dequeue())
    while stack.is_empty is False:
        queue.enqueue(stack.pop())
    size = queue.size()

    for i in range(size-k):
        queue.enqueue(queue.dequeue())
    return queue


class newQueue:
    def __init__(self):
        self.main_stack = MyStack()
        self.tmp_stack = MyStack()

    def enqueue(self,value):
        if self.main_stack.is_empty() and self.tmp_stack.is_empty():
            self.main_stack.push(value)
            print(str(value) + 'Init main enqueued')
        else:
            while not self.main_stack.is_empty():
                self.tmp_stack.push(self.main_stack.pop())

            self.main_stack.push(value)
            print(str(value) + "temp enqueued")
            while not self.tmp_stack.is_empty():
                self.main_stack.push(self.tmp_stack.pop())

    def dequeue(self):
        if self.main_stack.is_empty():
            return None
        value = self.main_stack.pop()
        print(str(value) + 'main dequeued')
        return value

def evaluate_post_fix(exp):
    stack = MyStack()
    for char in exp:
        if char.isdigit():
            stack.push(char)
        else:
            left = stack.pop()
            right = stack.pop()
            stack.push(str(eval(right+char+left)))

    return int(float(stack.pop()))

# print(evaluate_post_fix("921*-8-4+"))

def next_greater_element(lst):
    stack = MyStack()
    res = [-1]*len(lst)

    for i in range(len(lst) - 1, -1, -1):
        if not stack.is_empty():
            while not stack.is_empty() and stack.peek() <= lst[i]:
                stack.pop()
        if not stack.is_empty():
            res[i] = stack.peek()
        stack.push(lst[i])

    return res

print(next_greater_element([3,10,4,2,1,2,6,1,7,2,9]))
# if __name__ == "__main__":
#     queue = newQueue()
#     for i in range(5):
#         queue.enqueue(i+1)
#     print('-------------')
#     for i in range(5):
#         queue.dequeue()
#

