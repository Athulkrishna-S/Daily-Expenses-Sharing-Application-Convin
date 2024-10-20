from app import db

def createUser(data):
    # Initialize the expenses field as an empty dictionary
    data['expenses'] = {}
    
    # Insert the modified data into the database
    db.users.insert_one(data)


# find user email beign the uid
def findUser(email):
    return db.users.find_one({"email": email},{"_id":0})