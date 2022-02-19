
from controller import register,login

print("""
            SALAM..... Be Restorane Saman Khosh Amadid
""")


question = input('aya ozv moshtari haye ma hastid?(y/n) :')
# try:
if question == 'n':
    print('pas ozv sho')
    register('username', 'password')

elif question == 'y':
    login('username', 'password')
        
            
# except:
#     print('tekrari e user')