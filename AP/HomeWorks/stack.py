class Stack:
    def __init__(self, capacity):
        self.__list = [None] * capacity
        self.__index = 0
        self.__capacity = capacity

    def push(self, item):
        if self.__index == self.__capacity:
            raise Exception("Cannot add any itme to a full array")
        self.__list[self.__index] = item
        self.__index += 1

    def pop(self):
        index = self.__index
        if index == 0:
            raise Exception("Cannot pop any item of an empty array")
        last_item = self.__list[index - 1]
        self.__list[index - 1] = None
        self.__index -= 1
        return last_item

    def peek(self):
        return self.__list[self.__index - 1]

    def size(self):
        return self.__index

    def clear(self):
        self.__list = [None] * self.__capacity
        self.__index = 0

    def is_empty(self):
        return self.__index == 0


class WebBrowser:
    def __init__(self):
        self.__url = "/home"
        self.__history = Stack(20)

    def visit(self, url):
        self.__history.push(url)
        self.__url = url

    def back(self):
        try:
            last_url = self.__history.pop()
            self.__url = last_url
        except Exception:
            raise Exception("You are already in home page") from None

    def close(self):
        self.__history.clear()
        self.__url = "/home"
