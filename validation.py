def valid_first_name(first_name: str) -> str:
    
    if len(first_name) != 0:
        for letter in first_name:
            if not ((65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122)):
                return "You must use only English letters in first name."
        return "OK"
    
    else:
        return "First name cannot be empty"
            
            
def valid_last_name(last_name: str) -> str:
    
    if len(last_name) != 0:
        for letter in last_name:
            if not ((65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122)):
                return "You must use only English letters in last name."
        return "OK"
    
    else:
        return "Last name cannot be empty"
            

def valid_phone_number(phone_number: str) -> str:
    
    if len(phone_number) == 11:
        if phone_number[0] == '0' and phone_number[1] == '9':
            for digit in phone_number:
                if not (48 <= ord(digit) <= 57):
                    return "You must use only numbers in phone number."
            return "OK"
        else:
            return "Phone number must start with 09"
    
    elif len(phone_number) == 0:
        return "Phone number cannot be empty and must have 11 digits"   
    
    else:
        return "Phone number must have 11 digits"


def valid_password(password: str) -> str:
    
    if len(password) >= 6:
        
        for char in password:
            if 97 <= ord(char) <= 122:
                break
        else:
            return "Password must have at least one lowercase letter"
        
        for char in password:
            if 65 <= ord(char) <= 90:
                break
        else:
            return "Password must have at least one captial letter"
        
        for char in password:
            if 33 <= ord(char) <= 47 or 58 <= ord(char) <= 64 or 91 <= ord(char) <= 96 or 123 <= ord(char) <= 126:
                break
        else:
            return "Password must have at least one symbol"
        
        for char in password:
            if 48 <= ord(char) <= 57:
                break
        else:
            return "Password must have at least one number"
        
        return "OK"
    
    elif len(password) == 0:
        return "Password cannot be empty"
    
    else:
        return "Password must be at least 6 characters long"


def valid_email(email: str) -> str:
    
    if "@gmail.com" in email or "@yahoo.com" in email:
        email_parts = email.split('@')
        
        if email_parts[1] == "gmail.com" or email_parts[1] == "yahoo.com":
            for char in email_parts[0]:
                if not ((ord(char) == 46) or (48 <= ord(char) <= 57) or (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122)):
                    return "Invalid email"
            return "OK"
        
        else:
            "Invalid email"
            
    else:
        return "Invalid email"
def valid_username(username:str) ->str:
    pass
def valid_security_answer(answer:str) -> str:
    pass
def valid_city(city:str) -> str:
    pass