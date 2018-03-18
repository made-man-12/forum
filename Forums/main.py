from models import Member, Post
from store  import MemberStore, PostStore

m_1 = Member('member1', 50)
m_2 = Member('member2', 40)

p_1 = Post('post1', 'content1')
p_2 = Post('post2', 'content2')
p_3 = Post('post3', 'content3')

m_s = MemberStore()
p_s = PostStore()

m_s.add(m_1)
m_s.add(m_2)

p_s.add(p_1)
p_s.add(p_2)
p_s.add(p_3)


print m_s.get_all()
print p_s.get_all()




