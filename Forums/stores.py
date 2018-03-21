class MemberStore:

    members = []
    last_id = 1

    def get_all(self):
        return self.members

    @staticmethod
    def add(member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self, iden):
        all_members = self.get_all()
        for member in all_members:
            if iden is member.id:
                return member

    def entity_exists(self, member):
        result = True
        if self.get_by_id(member.id) is None:
            result = False

        return result

    def delete(self, iden):
        all_members = self.get_all()
        for member in all_members:
            if iden is member.id:
                all_members.remove(member)

    def update(self, new_member):
        all_members = self.get_all()
        for member in all_members:
            if new_member.id is member.id:
                self.delete(member.id)
                MemberStore.members.append(new_member)
                MemberStore.members.sort(key=lambda members: members.id)

    def get_by_name(self, member_name):
        all_members = self.get_all()
        result = []
        for member in all_members:
            if member_name is member.name:
                result.append(str(member))
        return result


class PostStore :
    posts = []
    last_id = 1

    def get_all(self):
        return self.posts

    @staticmethod
    def add(post):
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1

    def get_by_id(self, iden):
        all_post = self.get_all()
        for post in all_post:
            if iden is post.id:
                return post

    def entity_exists(self, post):
        result = True
        if self.get_by_id(post.id) is None:
            result = False

        return result

    def delete(self,id):
        all_post = self.get_all()
        for post in all_post:
            if id is post.id:
                all_post.remove(post)

    def update(self, new_post):
        all_post = self.get_all()
        for post in all_post:
            if new_post.id is post.id:
                self.delete(post.id)
                PostStore.members.append(new_post)