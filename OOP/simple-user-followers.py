class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def __str__(self):
        return f"{self.name} has {self.followers} followers and is following {self.following}"

    def follow(self, user):
        self.following += 1
        user.followers += 1


user1 = User('01', 'RSP')
user2 = User('02', 'Praneeth')
user3 = User('03', 'Satya')
user4 = User('04', 'Reddi')

user1.follow(user2)
user4.follow(user1)
user2.follow(user3)
user3.follow(user1)
user2.follow(user1)

print(user1)
print(user2)
print(user3)
print(user4)

