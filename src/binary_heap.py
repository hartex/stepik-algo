class MaxBinaryHeap:
    def __init__(self):
        self._array = []

    def sift_up(self, index):
        elem = self._array[index]
        parent_index = (index - 1) // 2
        parent_exist = (parent_index >= 0) and parent_index < len(self._array)
        if parent_exist:
            parent = self._array[parent_index]
            if parent < elem:
                self._array[parent_index] = elem
                self._array[index] = parent
                self.sift_up(parent_index)

    def sift_down(self, index):
        elem = self._array[index]
        child1_index = index * 2 + 1
        child2_index = index * 2 + 2
        child1_exist = child1_index < len(self._array)
        child2_exist = child2_index < len(self._array)

        if child1_exist and child2_exist:
            child1 = self._array[child1_index]
            child2 = self._array[child2_index]
            biggest = child1 if child1 >= child2 else child2
            biggest_index = child1_index if child1 == biggest else child2_index
            if elem < biggest:
                # swap elem with biggest
                self._array[index] = biggest
                self._array[biggest_index] = elem
                return self.sift_down(biggest_index)
        elif child1_exist:
            child1 = self._array[child1_index]
            if elem < child1:
                self._array[index] = child1
                self._array[child1_index] = elem

    def extract_max(self):
        if len(self._array) > 1:
            first = self._array.pop(0)
            last = self._array.pop()
            self._array.insert(0, last)
            self.sift_down(0)
            return first
        elif len(self._array) > 0:
            return self._array.pop()
        else:
            return None

    def insert(self, value):
        self._array.append(value)
        length = len(self._array)
        if length > 1:
            self.sift_up(length - 1)


def apply_operations(operations):
    queue = MaxBinaryHeap()
    for op in operations:
        if op == "ExtractMax":
            print(queue.extract_max())
        else:
            queue.insert(op[1])


def main():
    number_of_operations = int(input())
    operations = []
    for i in range(number_of_operations):
        operation = input()
        if operation != "ExtractMax":
            command, value = operation.split(" ")
            operation = (command, int(value))
        operations.append(operation)

    apply_operations(operations)


# Example
#
# 25
# Insert 20
# Insert 10
# ExtractMax
# Insert 31
# Insert 152
# Insert 52
# Insert 59
# Insert 33
# Insert 54
# Insert 121
# ExtractMax
# Insert 54
# Insert 61
# ExtractMax
# ExtractMax
# ExtractMax
# ExtractMax
# Insert 33
# Insert 34
# Insert 41
# Insert 0
# Insert 0
# ExtractMax
# ExtractMax
# ExtractMax
if __name__ == "__main__":
    main()
