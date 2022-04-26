import string
import random

def password(length):
    letters = string.ascii_letters + string.digits + string.punctuation 
    result_str = "".join(random.choice(letters) for i in range(length))
    print("Your password is", result_str)
    

password(10)
