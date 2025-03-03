class Node:
    def __init__(self, ugliness, idx):
        self.ugliness = ugliness
        self.idx = idx
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, ugliness):
        self.head = Node(ugliness, 1)
        self.head.next = self.head
        self.head.prev = self.head
        self.node_dict = {1: self.head}
        self.count = 1
    
    def insert(self, position, idx, ugliness):
        prev_monster = self.node_dict[position]
        new_monster = Node(ugliness, idx)

        new_monster.next = prev_monster.next
        new_monster.prev = prev_monster

        prev_monster.next.prev = new_monster
        prev_monster.next = new_monster

        self.node_dict[new_monster.idx] = new_monster
        self.count += 1
        self.merge(new_monster)
    
    def merge(self, node: Node):
        while True:
            merged = False
            left = node.prev
            right = node.next
            if left != node and node.ugliness == left.ugliness:
                if node.idx > left.idx:
                    left.next = node.next
                    node.next.prev = left
                    left.ugliness *= 2
                    self.count -= 1
                    node = left 
                else:
                    node.prev = left.prev
                    left.prev.next = node
                    node.ugliness *= 2
                    self.count -= 1
                merged = True

            elif right != node and node.ugliness == right.ugliness:
                if node.idx > right.idx:
                    node.prev.next = right
                    right.prev = node.prev
                    right.ugliness *= 2
                    self.count -= 1
                    node = right  
                else:
                    right.next.prev = node
                    node.next = right.next
                    node.ugliness *= 2
                    self.count -= 1
                merged = True

            if not merged:
                break





def solve():
    n , k = map(int,input().split())

    LL = LinkedList(k)

    nums = list(map(int,input().split()))
    ugly = list(map(int,input().split()))

    ans = []
    for i in range(n):
        pos = nums[i]
        ugliness = ugly[i]
        idx = i + 2
        LL.insert(pos , idx , ugliness)
        ans.append(LL.count)
    
    print(*ans)

for _ in range(int(input())):
    solve()
