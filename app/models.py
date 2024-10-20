from app import db

def createUser(data):
    # Initialize the expenses field as an empty dictionary
    data['expenses'] = {}
    
    # Insert the modified data into the database
    db.users.insert_one(data)


# find user email beign the uid
def findUser(email):
    return db.users.find_one({"email": email},{"_id":0})


def findUsers(emails):

    users = db.users.find({"email": {"$in": emails}}, {"_id": 0, "email": 1})
    user_dict = {user['email']: user for user in users}
    return user_dict


def findAllUsers():
        users = db.users.find({}, {"_id": 0, "name": 1, "email": 1, "expenses": 1})
        user_list = list(users)
        return user_list

def addExpense(updates):

    '''
        updates = [
        {
            "filter": {"email": participant1},
            "purpose": purpose,
            "share": share
        },
        {
            "filter": {"email": participant2},
            "purpose": purpose,
            "share": share
        }

        ]      
    '''

    for update in updates:
        # Fetch the current expense for the purpose
        existing_record = db.users.find_one(update["filter"], {"_id": 0, "expenses": 1})
        
        # Get the current value if it exists, else default to 0
        existing_value = existing_record.get("expenses", {}).get(update["purpose"], 0)
        
        # Add the new share to the existing value
        new_share = existing_value + update["share"]
        
        # Perform the update
        db.users.update_one(update["filter"], {"$set": {f"expenses.{update['purpose']}": new_share}})
