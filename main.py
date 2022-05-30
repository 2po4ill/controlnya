def recursiveadd(node, value):
    if node is None:
        node = (value, None, None)
        return node
    if node[0] < value:
        node = (node[0], node[1], recursiveadd(node[2], value))
        return node
    if node[0] > value:
        node = (node[0], recursiveadd(node[1], value), node[2])
        return node


def recursivesearch(node, value):
    if node is None:
        return False
    if node[0] < value:
        return recursivesearch(node[2], value)
    if node[0] > value:
        return recursivesearch(node[1], value)
    return True


def recursivecounter(node, value, cnt):
    if node[0] < value:
        cnt += 1
        return recursivecounter(node[2], value, cnt)
    if node[0] > value:
        cnt += 1
        return recursivecounter(node[1], value, cnt)
    cnt += 1
    return cnt


class SearchTree:
    def __init__(self):
        self.head = None
        self.left = None
        self.right = None

    def add(self, value):
        if self.head is None:
            self.head = [value, None, None]
            return
        if self.head[0] > value:
            self.head = (self.head[0], recursiveadd(self.head[1], value), self.head[2])
            return
        if self.head[0] < value:
            self.head = (self.head[0], self.head[1], recursiveadd(self.head[2], value))
            return

    def contains(self, value):
        return recursivesearch(self.head, value)

    def minim(self):
        temp = self.head
        while temp is not None:
            minim = temp[0]
            temp = temp[1]
        return minim

    def maxim(self):
        temp = self.head
        while temp is not None:
            maxim = temp[0]
            temp = temp[2]
        return maxim

    def tree_length(self):
        maxcnt = 0
        minim = self.minim()
        maxim = self.maxim()
        while minim != maxim:
            if recursivesearch(self.head, minim):
                maxcnt = max(recursivecounter(self.head, minim, 0), maxcnt)
                minim += 1
        return maxcnt

class VersionedTree:
    def __init__(self):
        self.version = SearchTree()
        self.treeversions = []

    def add(self, value):
         self.version.add(value)
         self.treeversions.append(self.version)

    def contains(self, version, value):
        return self.treeversions[version].contains(value)

    def length(self, version):
        return self.treeversions[version].tree_length()

if __name__ == "__main__":
    Tree = VersionedTree()
    Tree.add(2)
    Tree.add(1)
    Tree.add(3)
    Tree.add(4)
    print(Tree.length(3))


#для комита