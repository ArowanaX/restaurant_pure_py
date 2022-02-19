# import pickle
# from uuid import uuid4
# import settings
# # from db import BaseQuery

# # class MetaBase(type):
# #     def __init__(self, *args, **kwargs):
# #         self.query = BaseQuery(self.conn)
# #         super().__init__(*args, **kwargs)


# # ----------------- users ----------------------------

# class BaseUser:
#     type = None
#     file_name = None
#     file_path = None

#     def __init__(self, username, password) -> None:
#         self.username = username 
#         self.password = self._set_password(password)
#         self.id = self._generate_id()
        

#     @staticmethod
#     def _generate_id():
#         return str(uuid4()) 
    
#     @staticmethod
#     def _set_password(passw):
#         return hash(passw)

# # ----------- admin ------------------------------

# class AdminUser(BaseUser):
#     def __init__(self, username, password) -> None:
#         super().__init__(username, password)
    
# # ----------- customer -----------------------------


# class CustomerUser(BaseUser):
#     type = "customer"
#     file_name = "customer.db"
#     file_path = settings.USER_DATA_PATH / file_name


# #--------------- menu ----------------------------

# # class MenuBase(object):
# #     file_name = None
# #     file_path = None

# #     def __init__(self, food, price, detail) -> None:
# #         self.food = food
# #         self.price = price
# #         self.detail = detail
# #         self.id = self._generate_id()

# #     @staticmethod
# #     def _generate_id():
# #         return str(uuid4())

# #     # @staticmethod
# #     # def _details(detail):
# #     #     return detail

# #     def save(self):
# #         try:
# #             with open(settings.MENU_DATA_PATH / self.file_name, "ab") as db_file:
# #                 pickle.dump(self, db_file)

# #         except Exception as e:
# #             print(e)

    


# # class FoodMenu(MenuBase):
# #     type = "food"
# #     file_name = "food.db"
# #     file_path = settings.MENU_DATA_PATH / file_name

# # class DrinkMenu(MenuBase):
# #     type = "drink"
# #     file_name = "drink.txt"
# #     file_path = settings.MENU_DATA_PATH / file_name

# # class DesertMenu(MenuBase):
# #     type = "desert"
# #     file_name = "desert.txt"
# #     file_path = settings.MENU_DATA_PATH / file_name

    