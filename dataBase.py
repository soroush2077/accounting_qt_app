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


def add_category(username: str, category):
    
    conn = connect_db()
    
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS categories(\
        username TEXT NOT NULL,\
        category TEXT NOT NULL);")

    query = "SELECT category FROM categories WHERE username = ?"
    cursor.execute(query, (username,))
    user_category = cursor.fetchall()
    

    for item in user_category:    
        if category in item[0]:
            return "Category already exists"
    
    else:
        insert_query = "INSERT INTO categories (username, category) VALUES (?, ?);"
        cursor.execute(insert_query, (username, category))
        conn.commit()
        conn.close()
        return "Category added succesfuly"
    
def get_categories(username: str):
    
    conn= connect_db()
    
    cursor = conn.cursor()
    
    query="SELECT category FROM categories WHERE username = ?"
    cursor.execute(query, (username,))
    categories = cursor.fetchall()
    conn.close()
    return categories



def search(username: str, search_text: str, filters: dict):
    conn = connect_db()
    cursor = conn.cursor()

    
    if 'search' in filters:

        search_term = '%' + search_text + '%'
        query = """
        SELECT * FROM transactions
        WHERE username = ?
        AND (
            description LIKE ? OR
            type LIKE ? OR
            source LIKE ? OR
            income_or_expense LIKE ? OR
            date LIKE ?
        )
        """
        params = [username]
        params.extend([search_term] * 5)


    if 'income_or_expense' in filters:
        query += " AND income_or_expense = ?"
        params.append(filters['income_or_expense'])

    if 'date' in filters:
        query += " AND date = ?"
        params.append(filters['date'])

    elif 'month' in filters:
        query += " AND strftime('%Y-%m', date) = ?"
        params.append(filters['month'])

    elif 'year' in filters:
        query += " AND strftime('%Y', date) = ?"
        params.append(filters['year'])
        
    if 'amount_range' in filters:
        query += " AND amount BETWEEN ? AND ?"
        params.extend(filters['amount_range'])

    if 'description' in filters:
        query += " AND description LIKE ?"
        params.append('%' + search_text + '%')

    if 'type' in filters:
        query += " AND type = ?"
        params.append('%' + search_text + '%')

    if 'source' in filters:
        query += " AND source = ?"
        params.append('%' + search_text + '%')


    if 'search' in filters and len(filters) == 1:

        search_term = '%' + search_text + '%'
        query = """
        SELECT * FROM transactions
        WHERE username = ?
        AND (
            description LIKE ? OR
            type LIKE ? OR
            source LIKE ? OR
            income_or_expense LIKE ? OR
            date LIKE ?
        )
        """
        params = [username]
        params.extend([search_term] * 5)
        
    

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()

    final_results = []
    for record in results:
        record_list = list(record)
        record_list.pop(1)
        final_results.append(record_list)

    return final_results


def report(username: str, filters: dict):


    conn = connect_db()
    
    cursor = conn.cursor()


    query = "SELECT * FROM transactions WHERE username = ?"
    params = [username]


    if 'income_or_expense' in filters:
        query += " AND income_or_expense = ?"
        params.append(filters['income_or_expense'])

    if 'date' in filters:
        query += " AND date = ?"
        params.append(filters['date'])

    elif 'month' in filters:
        query += " AND strftime('%Y-%m', date) = ?"
        params.append(filters['month'])

    elif 'year' in filters:
        query += " AND strftime('%Y', date) = ?"
        params.append(filters['year'])
        
    elif 'last_day' in filters:
        query += " AND date >= DATE('now', '-1 day')"
    
    elif 'last_three_days' in filters:
        query += " AND date >= DATE('now', '-3 days')"    
        
    elif 'date_range' in filters:
        query += "AND date BETWEEN ? AND ?"
        params.extend(filters['date_range'])


    if 'amount_range' in filters:
        query += " AND amount BETWEEN ? AND ?"
        params.extend(filters['amount_range'])

    if 'description' in filters:
        query += " AND description LIKE ?"
        params.append('%' + filters['description'] + '%')

    if 'type' in filters:
        query += " AND type = ?"
        params.append(filters['type'])

    if 'source' in filters:
        query += " AND source = ?"
        params.append(filters['source'])


    cursor.execute(query, params)
    results = cursor.fetchall()


    conn.close()
    
    final_results = []
    for tuple in results:
        tuple_list = list(tuple)
        tuple_list.pop(1)
        final_results.append(tuple_list)

    return final_results


def total(username: str, income_or_expense: str):
    
    conn = connect_db()
    
    cursor = conn.cursor()


    query = "SELECT amount FROM transactions WHERE username = ? AND income_or_expense = ?"
    params = [username, income_or_expense]
    cursor.execute(query, params)
    results = cursor.fetchall()
    
    total = 0
    for item in results:
        total += item[0]
        
    return total


def results_total(results: list):
    total = 0
    for item in results:
        total += item[1]  # amount
        
    return total



def edit_account(username, updates: dict):
    
    if not updates:
        return "You should at least change one item"
    
    conn = connect_db()
    cursor = conn.cursor()
    
    temp = [f"{key} = ?" for key in updates.keys()]
    set_query = ", ".join(temp)
    final_query = f" UPDATE accounts set {set_query} WHERE username = ?"
    values = list(updates.values()) + [username]
    
    cursor.execute(final_query, values)
    
    conn.commit()
    conn.close()
    
    return "Update succesful"



if __name__ == "__main__":
    # filters = {
    #     'date_range': ['2000-06-06', '2004-06-06']
    # }
    # print(report("alireza", filters))
    # print(total("alireza", "expense"))
    # report("alireza", {})
    pass
    