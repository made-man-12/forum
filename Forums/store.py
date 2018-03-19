class MemberStore:

    members = []
    last_id = 1

    def get_all(self):
        return MemberStore.members

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self,id):
        all_members = self.get_all()
        for member in all_members:
            if id is member.id:
                return member


    def entity_exists(self, member):
        result = True
        if self.get_by_id(member.id) == None:
            result = False

        return result



    def delete(self,id):
        all_members = self.get_all()
        for member in all_members:
            if id is member.id:
                all_members.remove(member)

class PostStore :
    posts = []
    last_id = 1

    def get_all(self):
        return PostStore.posts

    def add(self, post):
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1

    def get_by_id(self,id):
        all_post = self.get_all()
        for post in all_post:
            if id is post.id:
                return post


    def entity_exists(self, post):
        result = True
        if self.get_by_id(post.id) == None:
            result = False

        return result



    def delete(self,id):
        all_post = self.get_all()
        for post in all_post:
            if id is post.id:
                all_post.remove(post)
