class Queue:
    def __init__(self):
        self.list = []
        self.size = 0

    def add_front(self, data):
        self.list.insert(0, data)
        self.size += 1

    def list_print(self):
        print(self.list)

    def delete_element(self):
        self.list.pop()
        self.size -= 1


    def is_empty(self):
        if self.size == 0:
            return True
        return False


    def initialize(self, data):
        if data != "[]":
            data = data[1:-1]
            data = data.replace(" ", "").split(',')
            res = [eval(i) for i in data]
            self.list = res
            self.size = len(res)

if __name__ == "__main__":
    my_list = Queue()
    input_list = input()
    my_list.initialize(input_list)
    command = input()
    try:
        if command == "enqueue":
            data = int(input())
            if data:
                my_list.add_front(data)
                my_list.list_print()
            else:
                print("Error")
        elif command == "isEmpty":
            print(my_list.is_empty())
        elif command == "dequeue":
            my_list.delete_element()
            my_list.list_print()
        elif command == "size":
            print(my_list.size)
        else:
            print("Error")
    except:
        print("Error")