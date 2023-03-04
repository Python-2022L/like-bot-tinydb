from db import LikeDB

db = LikeDB('db.json')

# print(db.add_student(2334))
# db.add_like(234)
# db.add_like(2334)
# db.add_dislike(234)

print(db.all_dislikes())