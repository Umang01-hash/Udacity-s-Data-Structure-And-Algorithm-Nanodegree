from collections import defaultdict


class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

class RouteTrie:
    def __init__(self, root_handler=None):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):
        pathParts = self.getPathParts(path)
        node = self.root
        for part in pathParts:
            if part != '':

                node = node.children[part]

        node.handler = handler

    def find(self, path):

        pathParts = self.getPathParts(path)
        node = self.root

        for part in pathParts:
            if part != '':
                node = node.children[part]

        return node.handler

    def getPathParts(self, path):
        return path.split('/')

class Router:
    def __init__(self, root_handler):
        self.route_trie = RouteTrie(root_handler)

    def addHandler(self, path, handler):
        self.route_trie.insert(path, handler)

    def lookup(self, path):
        return self.route_trie.find(path)



router = Router("root handler")
router.addHandler("/home", "home handler")  # add a route
router.addHandler("/home/about", "about handler")  # add a route
router.addHandler("/home/about/me/edit", "edit handler")  # add a route

print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'home handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler'
print(router.lookup("/home/about/me/edit"))  # should print 'edit handler'
