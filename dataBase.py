import sqlite3

def add_account(first_name:str,last_name:str,phone_number:str,username:str,password:str,email:str,security_answer:str,city:str,birthdate:str):
    db=sqlite3.connect("info.db")
    cursor=db.cursor()
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS accounts(first_name TEXT NOT NULL,last_name TEXT NOT NULL,phone_number TEXT NOT NULL,\
            username TEXT NOT NULL UNIQUE,password TEXT NOT NULL,email TEXT NOT NULL UNIQUE,security_answer TEXT NOT NULL,city TEXT NOT NULL,\
                birth_date TEXT NOT NULL);")
        cursor.execute("INSERT INTO accounts(first_name, last_name, phone_number, username, password, email, security_answer, city, birth_date) \
            VALUES ( ?, ? ,? ,? ,? ,? ,? ,? ,?);", [first_name, last_name, phone_number, username, password, email, security_answer, city, birthdate])
        db.commit()
        db.close()
    except:
        return "email and username must be unique"
    else:
        return "sign up completed"

def user_login():
    pass
def user_forgot_pass():
    pass
    
# add_account("soroush", "ghaemi", "09387149816", "soroush2077" ,"Qwer1234@", "soroush2077@gmail.com", "rex", "mashhad", "2006/12/06")
    