import models
import stores


def create_members():

    member1 = models.Member("Mohammed", 20)
    member2 = models.Member("Omar", 22)
    member3 = models.Member("Abdo", 25)
    member4 = models.Member("Mohammed", 21)
    print(member1)
    print(member2)
    print(member3)
    print(member4)
    print("=" * 30)

    return member1, member2, member3, member4


def store_should_add_models(members_instances, member_store):

    for member in members_instances:
        member_store.add(member)


def stores_should_be_similar():

    member_store1 = stores.MemberStore()
    member_store2 = stores.MemberStore()
    if member_store1.get_all() is member_store2.get_all():
        print("Same stores elements !")


def print_all_members(member_store):
    print("=" * 30)

    for member in member_store.get_all():
        print(member)

    print("=" * 30)


def get_by_id_should_retrieve_same_object(member_store, member2):
    member2_retrieved = member_store.get_by_id(member2.id)

    if member2 is member2_retrieved:
        print("member2 and member2_retrieved are matching !")


def update_should_modify_object(member_store, member3):
    member3_copy = models.Member(member3.name, member3.age)
    member3_copy.id = 3

    if member3_copy != member3:
        print("member3 and member3_copy are not the same !")

    print(member3_copy)
    member3_copy.name = "john"
    member_store.update(member3_copy)
    print(member_store.get_by_id(member3.id))


def catch_exception_when_deleting():
    try:
        member_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")

def find_member_by_name(mamber_name):
    find_member = member_store.get_by_name(mamber_name)
    if not find_member :
        print 'No member'
    else:
        print find_member

members_instances = create_members()
member1, member2, member3, member4 = members_instances

member_store = stores.MemberStore()

store_should_add_models(members_instances, member_store)

stores_should_be_similar()

print_all_members(member_store)

get_by_id_should_retrieve_same_object(member_store, member2)

update_should_modify_object(member_store, member3)

catch_exception_when_deleting()

print_all_members(member_store)

find_member_by_name('Mohammed')