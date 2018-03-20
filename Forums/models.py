
class Member:
    def __init__(self, name, age):
        self.id = 0
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: %s Age: %d" %(self.name, self.age)

    def __ne__(self, other):
        return self.name != other.name and self.age != other.age and self.id != other.id

class Post:
    def __init__(self, title, content):
        self.id = 0
        self.title = title
        self.content = content

    def __str__(self):
        return "Title: %s Content: %s" %(self.title, self.content)
