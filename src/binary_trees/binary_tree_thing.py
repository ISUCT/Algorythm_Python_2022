class Node:
    def __init__(self, data):
        self.__data: int = data
        self.__left: Node = None
        self.__right: Node = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value) -> None:
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value) -> None:
        self.__right = value

    @property
    def data(self) -> int:
        return self.__data

    def add(self, value: int) -> None:
        if self.data == value:
            return
        if value < self.data:
            if self.left:
                self.left.add(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)

    def find_with_single(self) -> None:
        if self.left:
            self.left.find_with_single()
        if self.left and not self.right:
            print(self.data)
        if self.right and not self.left:
            print(self.data)
        if self.right:
            self.right.find_with_single()

def create_tree(xs) -> Node:
    root = Node(xs[0])
    for i in range(1, len(xs) - 1):
        root.add(xs[i])
    return root