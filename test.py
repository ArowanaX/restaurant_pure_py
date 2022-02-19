from controller import register,login


# admin_object = AdminUser("asghar", "1234")
# member_object = CustomerUser("akbar", "1234")

# BaseQuery.conn.commit()
# cursors = BaseQuery.conn.cursor()
# cursors.execute("""CREATE TABLE users (
#         username text,
#         password integer
#     )""")
# cursors.execute("SELECT * FROM users")
# print(cursors.fetchall())
# member_object.save()


# menu_object = FoodMenu("kabab", "123", "kababe")

# menu_object.save()

# def loadall(filename):
#     with open(filename, "rb") as f:
#         while True:
#             try:
#                 yield pickle.load(f)
#             except EOFError:
#                 break


# items = loadall(settings.MENU_DATA_PATH / "food.txt")


# for item in items:
#     print(item.food,item.detail, item.price)

# for elm in CustomerUser.query.loadall():
#     print(elm.username)

# print(CustomerUser.query.exist("username", "amir"))

# print(login('kasra', '123'))

print(login("kasra", "1234"))

# print(register('amir1', '123'))
# print(login("amir", "123"))