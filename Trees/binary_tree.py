## Node Class and Tree Construction

class Node:

    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

drinks=Node("drinks")
hot=Node("Hot")
cold=Node("Cold")
tea=Node("Tea")
coffee=Node("Coffee")
cola=Node("Cola")
fanta=Node("Fanta")

hot.left=tea
hot.right=coffee

cold.left=cola
cold.right=fanta

drinks.left=hot 
drinks.right=cold

print(drinks.left.left.val)
print(drinks.right.left.val)
