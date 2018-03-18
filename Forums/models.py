
class   Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Name: %s Age: %d" %(self.name, self.age)

class Post():
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return "Title: %s Content: %s" %(self.title, self.content)
