import sqlite3



def connect_db():
  
    conn = sqlite3.connect('info.db')
    return conn


def add_account(first_name:str, last_name:str, phone_number:str, username:str, password:str, email:str, security_answer:str, city:str, birthdate:str):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS accounts(first_name TEXT NOT NULL,last_name TEXT NOT NULL, phone_number TEXT NOT NULL,\
            username TEXT NOT NULL UNIQUE PRIMARY KEY, password TEXT NOT NULL, email TEXT NOT NULL UNIQUE, security_answer TEXT NOT NULL, city TEXT NOT NULL,\
                birth_date DATE NOT NULL);")
        cursor.execute("INSERT INTO accounts(first_name, last_name, phone_number, username, password, email, security_answer, city, birth_date) \
            VALUES ( ?, ? ,? ,? ,? ,? ,? ,? ,?);", [first_name, last_name, phone_number, username, password, email, security_answer, city, birthdate])
        conn.commit()
        conn.close()
    except:
        return "email and username must be unique"
    else:
        return "sign up completed"
    
    
def search_user(email_or_username):

    conn = connect_db()
    cursor = conn.cursor()
    
    
    query = "SELECT first_name, last_name, phone_number, username, password, email, security_answer, city, birth_date FROM accounts WHERE username = ?"
    cursor.execute(query, (email_or_username,))
    result = cursor.fetchone()


    if not result:
        query = "SELECT first_name, last_name, phone_number, username, password, email, security_answer, city, birth_date FROM accounts WHERE email = ?"
        cursor.execute(query, (email_or_username,))
        result = cursor.fetchone()

    conn.close()

    if result:
        user_info = {
            'first_name': result[0],
            'last_name': result[1],
            'phone_number': result[2],
            'username': result[3],
            'password': result[4],
            'email': result[5],
            'security_answer': result[6],
            'city': result[7],
            'birth_date': result[8],
        }
        return user_info
    else:
        return "User not found"


def user_login(username: str, password: str):
    user_info = search_user(username)
    if user_info == "User not found":
        return "User not found"
    else:
        if user_info['password'] == password:
            return "You have successfully logged in"
        else:
            return "Incorrect password"
        
        
def user_forgot_pass(email_or_username: str, security_answer: str):
    user_info = search_user(email_or_username)
    if user_info == "User not found":
        return "User not found"
    else:
        if user_info['security_answer'] == security_answer:
            return user_info['password']
        else:
            return "Incorrect answer"
    
# add_account("soroush", "ghaemi", "09387149816", "soroush2077" ,"Qwer1234@", "soroush2077@gmail.com", "rex", "mashhad", "2003-12-06")   


def add_transaction(username, income_or_expense, amount, date, source, type, description = None):
  
    
    conn = connect_db()
    

    cursor = conn.cursor()


    cursor.execute("CREATE TABLE IF NOT EXISTS transactions (\
        income_or_expense TEXT NOT NULL,\
        username TEXT NOT NULL,\
        amount INTEGER NOT NULL,\
        date DATE NOT NULL,\
        source TEXT NOT NULL,\
        description TEXT,\
        type TEXT NOT NULL\
    );")


    insert_query = "INSERT INTO transactions (username, income_or_expense, amount, date, source, description, type)\
    VALUES (?, ?, ?, ?, ?, ?, ?);"
    cursor.execute(insert_query, (username, income_or_expense, amount, date, source, description, type))


    conn.commit()
    conn.close()



