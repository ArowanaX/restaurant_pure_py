# from models import CustomerUser
import uuid
import sqlite3
from db import get_main_menu, get_drinks_menu, get_deserts_menu
from db import price_main, price_drinks, price_deserts
# from db import seek_main_menu
import settings


# ------------------------------ register -------------------------------------------------

def register(username, password):

# -------------------------- admin registeration ------------------------------------------

    user_model = input('noe ozviate khod ra vared konid(admin/user): ')
    if user_model == 'admin':
        ramz = input('ramze admin ra vared konid: ')
        if ramz == '1095':
            username_admin = input('name kar barie khod ra vared konid: ')
            password_admin = input('ramze morede nazar ra vared konid: ')
            
            con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
            cur = con.cursor()
    
            cur.execute("""SELECT username
                        FROM admins
                        WHERE username=?""",
                        [username_admin])

            result = cur.fetchone()



            if result:
                print('username tekrari ast')

            else:
                admin_id = (username_admin, password_admin)
                sql = ''' INSERT INTO admins(username,password)
                VALUES(?,?) '''
                cur = con.cursor()
                cur.execute(sql, admin_id)
                con.commit()
                print('admin jadid sakhte shod')
                return cur.lastrowid


# ------------------------------ user registration -----------------------------------

    elif user_model == 'user':
        username = input('name kar barie khod ra vared konid: ')
        password = input('ramze morede nazar ra vared konid: ')
        con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
        cur = con.cursor()

        cur.execute("""SELECT username
                        FROM users
                        WHERE username=?""",
                        [username])

        result = cur.fetchone()

        if result:
            print('username tekrari ast')

        else:
            user_id = (username, password)
            sql = ''' INSERT INTO users(username,password)
              VALUES(?,?) '''
            cur = con.cursor()
            cur.execute(sql, user_id)
            con.commit()
            print('khosh amadid az sefaresh haye khod lezat bebarid')
            return cur.lastrowid


# -------------------------- login ---------------------------------------

def login(username, password):

#-------------------------- user login ---------------------------------

    user_model = input("noe vorode khod ra entekhab konid(admin/user):")

    if user_model == 'user':
        username = input('username khod ra vared konid: ')
        password = input('passworde khod ra vared konid: ')
        user_id = username
        con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
        cur = con.cursor()

        cur.execute("""SELECT username,
                    password
                    FROM users
                    WHERE password=? AND username=?""",
                    [password, username])
        
        result = cur.fetchone()

        if result:
            order = []
            prices = []

# ------------------------ order food --------------------------------------

            main_menu = get_main_menu()
            print('sefaresh dahid')
            print(main_menu)
            pick = input('ghazaye khod ra entekhab konid: ')
            # print(main_menu.gheymat)
            while pick != 'n':
                order.append(pick)
                prices.append(price_main)
                pick = input('ghazaye khod ra entekhab konid: ')

#-------------------------- order drinks -----------------------------------
            
            drinks_menu = get_drinks_menu()
            pick_drink = input('noshidani chi mikhay? ')

            while pick_drink != 'n':
                order.append(pick_drink)
                prices.append(price_drinks)
                pick_drink = input('noshidani chi mikhay? ')

 # ----------------------- order deserts ------------------------------------               

            desert_menu = get_deserts_menu()
            pick_desert = input('deser chi mikhay? ')

            while pick_desert != 'n':
                order.append(pick_desert)
                prices.append(price_deserts)
                pick_desert = input('deser chi mikhay? ')

            print('-' * 10)
            print('sefaresh shoma barabar ast ba : ', order, 'va jam gheymat bar a bar ast ba : ', sum(prices))

# ----------------------------- Finalizing order --------------------------------------------

            sefaresh_nahayi = input('mikhay sefaresheto sabt koni?(y/n) ')
            if sefaresh_nahayi == 'y':
                con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
                cur = con.cursor()
                price_nahayi = sum(prices)
                sefaresh = (str(order), str(user_id), int(price_nahayi))
                sql = ''' INSERT INTO sefaresh(sefaresh,users_id,price)
                VALUES(?,?,?) '''
                cur = con.cursor()
                cur.execute(sql, sefaresh)
                con.commit()
                print('sefaresh shoma ba moafaghiat sabt shod :)')
                return cur.lastrowid
            elif sefaresh_nahayi == 'n':
                history = input('mikhay sefareshe ghablito bbini?(y/n) ')

# ----------------------- see history ------------------------------------

                if history ==  'y':
                    con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
                    cur = con.cursor()

                    cur.execute("""SELECT 
                                sefaresh,
                                price
                                FROM sefaresh
                                WHERE users_id=?""",
                                [str(user_id)])
                    
                    sefaresh_history = cur.fetchall()
                    print(sefaresh_history)
                elif history == 'n':
                    print('khosh amadid')
        else:
            print('username ya password eshtebah ast')

# ----------------------- admin login ------------------------------------------------
    
    elif user_model == 'admin':
        username = input('username khod ra vared konid: ')
        password = input('passworde khod ra vared konid: ')

        con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
        cur = con.cursor()

        cur.execute("""SELECT username,
                    password
                    FROM admins
                    WHERE password=? AND username=?""",
                    [password, username])
        
        result = cur.fetchone()
# ----------------------------------------------- Instructions ------------------------------------------------------
        while True:
            if result:
                print('vared shodid')
                tanzimat = input('mikhay be tanzimat dastressi peyda koni?(y/n) ')
                if tanzimat == 'y':
                    print('dastor ol amal be sorate zir mibashad')
                    print('*' * 6)
                    print('ba vared kardane har kodom az in horof varede tanzimat mishavid')
                    print('*' * 6)
                    print('ba vared kardan (u) varede tanzimat ghesmt karbar ha mishavid')
                    print('-' * 10)
                    print('ba vared kardan (h) varede tanzimat ghesmt history sefaresh ha mishavid')
                    print('-' * 10)
                    print('ba vared kardan (m) varede tanzimat ghesmt menue main mishavid')
                    print('-' * 10)
                    print('ba vared kardan (md) varede tanzimat ghesmt menue desert mishavid')
                    print('-' * 10)
                    print('ba vared kardan (mdr) varede tanzimat ghesmt menue drinks mishavid')
                    print('*' * 10)
                    print('*' * 8)
                    admin_choice = input('varede kodom tanzimat mikhahid shavid(u, h, m, md, mdr)?: ')

    # -------------------------------------------------- update users ------------------------------------------------------

                    if admin_choice == 'u':
                        con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
                        cur = con.cursor()

                        cur.execute("""SELECT * FROM users""")
                        result = cur.fetchall()
                        for elm in result:
                            print(elm)

    # --------------------------------------------- delete user -----------------------------------------------------

                        user_delete = input('mikhay useri ro hazf koni?(y/n) ')
                        if user_delete == 'y':
                            user_d = input('esme useri k mikhay delete koni ro bego: ')
                            con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
                            cur = con.cursor()
                            sql = 'DELETE FROM users WHERE username=?'
                            sql1 = 'DELETE FROM sefaresh WHERE users_id=?'
                            cur = con.cursor()
                            cur.execute(sql, (user_d,))
                            cur.execute(sql1, (user_d,))                        
                            con.commit()
                            print('usere morede nazar ba moafaghiat hazf shod')
                        elif user_delete == 'n':
                            print('- ' * 10)
                            print('kar ba tanzimat user tamom shod')

# --------------------------------------------- history acc ----------------------------------------------

                    elif admin_choice == 'h':
                        con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
                        cur = con.cursor()

                        cur.execute("""SELECT * FROM sefaresh""")
                        result = cur.fetchall()
                        for elm in result:
                            print(elm)

# --------------------------------------- main menu acc -------------------------------------------------

                    elif admin_choice == 'm':
                        con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
                        cur = con.cursor()

                        cur.execute("""SELECT * FROM main_menu""")
                        result = cur.fetchall()
                        for elm in result:
                            print(elm)
                        choice = input('u = update, d = delete, i = insert: ')
                        if choice == 'd':
                            food_d = input('esme ghazaei k mikhay delete koni ro bego: ')
                            con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
                            cur = con.cursor()
                            sql = 'DELETE FROM main_menu WHERE name=?'
                            cur.execute(sql, (food_d,))
                            print('ghazaye morede nazar ba moafaghiat hazf shod')
                            con.commit()

# ------------------------------------ insert values into main menu -------------------------------------

                        elif choice == 'i':
                            food_name = input('esme ghazaei k mikhay ezafe koni ro bego: ')
                            food_details = input('etelaate ghazaei k mikhay ezafe koni ro bego: ')
                            food_price = input('gheymate ghazaei k mikhay ezafe koni ro bego: ')
                            sql = ''' INSERT INTO main_menu(name,detail,price)
                            VALUES(?,?,?) '''
                            food_insert = (food_name, food_details, food_price)
                            cur = con.cursor()
                            cur.execute(sql, food_insert)
                            con.commit()
                            print('ghaza ezafe shod :)')
                            cur.lastrowid

# ---------------------------------- update values from main menu ----------------------------------

                        elif choice == 'u':
                            food_id = input('id o ghazayi k mikhay update koni ro bgo: ')
                            food_name = input('esme ghazaei k mikhay update koni ro bego: ')
                            food_details = input('etelaate ghazaei k mikhay update koni ro bego: ')
                            food_price = input('gheymate ghazaei k mikhay update koni ro bego: ')
                            sql = ''' UPDATE main_menu
                                SET name = ? ,
                                    detail = ? ,
                                    price = ?
                                WHERE id = ?'''
                            
                            columnValues = (food_name, food_details, food_price, food_id)
                            cur.execute(sql, columnValues)
                            print('taghirat emal shod')
                            con.commit()

# --------------------------------------- desert menu acc -------------------------------------------

                    elif admin_choice == 'md':
                        con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
                        cur = con.cursor()

                        cur.execute("""SELECT * FROM deserts_menu""")
                        result = cur.fetchall()
                        for elm in result:
                            print(elm)

# ------------------------------------ update values in desert menu -------------------------------------

                        choice = input('u = update, d = delete, i = insert: ')
                        if choice == 'd':
                            food_d = input('esme ghazaei k mikhay delete koni ro bego: ')
                            con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
                            cur = con.cursor()
                            sql = 'DELETE FROM deserts_menu WHERE name=?'
                            cur.execute(sql, (food_d,))
                            print('ghazaye morede nazar ba moafaghiat hazf shod')
                            con.commit()

# -------------------------------------- insert values into desert menu ----------------------------------

                        elif choice == 'i':
                            food_name = input('esme ghazaei k mikhay ezafe koni ro bego: ')
                            food_details = input('etelaate ghazaei k mikhay ezafe koni ro bego: ')
                            food_price = input('gheymate ghazaei k mikhay ezafe koni ro bego: ')
                            sql = ''' INSERT INTO deserts_menu(name,detail,price)
                            VALUES(?,?,?) '''
                            food_insert = (food_name, food_details, food_price)
                            cur = con.cursor()
                            cur.execute(sql, food_insert)
                            con.commit()
                            print('ghaza ezafe shod :)')
                            cur.lastrowid

# ------------------------------------ update values in desert menu -------------------------------------

                        elif choice == 'u':
                            food_id = input('id o ghazayi k mikhay update koni ro bgo: ')
                            food_name = input('esme ghazaei k mikhay update koni ro bego: ')
                            food_details = input('etelaate ghazaei k mikhay update koni ro bego: ')
                            food_price = input('gheymate ghazaei k mikhay update koni ro bego: ')
                            sql = ''' UPDATE deserts_menu
                                SET name = ? ,
                                    detail = ? ,
                                    price = ?
                                WHERE id = ?'''
                            
                            columnValues = (food_name, food_details, food_price, food_id)
                            cur.execute(sql, columnValues)
                            print('taghirat emal shod')
                            con.commit()

# ----------------------------------- drink_menu acc ---------------------------------------------

                    elif admin_choice == 'mdr':
                        con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
                        cur = con.cursor()

                        cur.execute("""SELECT * FROM drinks_menu""")
                        result = cur.fetchall()
                        for elm in result:
                            print(elm)

# ------------------------------- delete values from drink_menu ---------------------------------

                        choice = input('u = update, d = delete, i = insert: ')
                        if choice == 'd':
                            food_d = input('esme ghazaei k mikhay delete koni ro bego: ')
                            con = sqlite3.connect(f"{settings.RESTORAN_DATA_PATH}/restoran.db")
                            cur = con.cursor()
                            sql = 'DELETE FROM drinks_menu WHERE name=?'
                            cur.execute(sql, (food_d,))
                            print('ghazaye morede nazar ba moafaghiat hazf shod')
                            con.commit()

# --------------------------------- insert values to drink_menu ------------------------------------------

                        elif choice == 'i':
                            food_name = input('esme ghazaei k mikhay ezafe koni ro bego: ')
                            food_details = input('etelaate ghazaei k mikhay ezafe koni ro bego: ')
                            food_price = input('gheymate ghazaei k mikhay ezafe koni ro bego: ')
                            sql = ''' INSERT INTO drinks_menu(name,detail,price)
                            VALUES(?,?,?) '''
                            food_insert = (food_name, food_details, food_price)
                            cur = con.cursor()
                            cur.execute(sql, food_insert)
                            con.commit()
                            print('ghaza ezafe shod :)')
                            cur.lastrowid

# --------------------------------  update values from drink_menu -----------------------------------------

                        elif choice == 'u':
                            food_id = input('id o ghazayi k mikhay update koni ro bgo: ')
                            food_name = input('esme ghazaei k mikhay update koni ro bego: ')
                            food_details = input('etelaate ghazaei k mikhay update koni ro bego: ')
                            food_price = input('gheymate ghazaei k mikhay update koni ro bego: ')
                            sql = ''' UPDATE drinks_menu
                                SET name = ? ,
                                    detail = ? ,
                                    price = ?
                                WHERE id = ?'''
                            
                            columnValues = (food_name, food_details, food_price, food_id)
                            cur.execute(sql, columnValues)
                            print('taghirat emal shod')
                            con.commit()                            
            else:
                print('username ya password eshtebah ast')

            x=(input("aya mikhahid edame dahid?(y/n): "))
            if x=="y":
                continue
            elif x=="n":
                break