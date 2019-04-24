class MyHashSet(object):

    hashSet = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashSet = {}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashSet[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        try:
            #del self.hashSet[key]
            # self.hashSet.pop(key)
            self.hashSet[key] = False
        except:
            pass

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        try:
            return self.hashSet[key]
        except:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
