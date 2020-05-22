class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = [] #Empty list for groups
        self.users = []  #Empty List for Users

    def addGroup(self, group): #Function to append the group to the list
        self.groups.append(group)

    def add_user(self, user): #Function to append the user to the list
        self.users.append(user)

    def getGroup(self): #Function to return rhe list of groups
        return self.groups

    def getUser(self):  #Functin to return the list of user
        return self.users

    def getName(self):
       return self.name


def UserinGroup(user, group):

    #using the getName () and getUser() function to check whether the user is in group
    if user == group.getName() or user in group.getUser():
        return True
    #iterating through the group using getGroup() function and suing a recursive call to the function
    for group in group.getGroup():
        return UserinGroup(user, group)

    return False




parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.addGroup(sub_child)
parent.addGroup(child)

sub_child_user2 = "sub_child_user_2"
sub_child_2 = Group("subchild2")
sub_child_2.add_user(sub_child_user2)
parent.addGroup(sub_child_2)

print(UserinGroup(sub_child_user, parent))
print(UserinGroup(sub_child_user, child))
print(UserinGroup(sub_child_user2, parent))
print(UserinGroup("", parent))
print(UserinGroup("child", child))

