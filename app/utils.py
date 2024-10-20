import re




def validate_user_data(data):
    required_fields = {"email", "name", "mobile"}
    
    # Check if data contains exactly the required fields
    if set(data.keys()) != required_fields:
        return False
    
    # Check if all required fields are present and not empty
    if not all(data[field] for field in required_fields):
        return False
    
    # Check if email is of correct format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, data['email']):
        return False
    
    # Check if mobile is of 10 digits and does not start with zero
    mobile_regex = r'^[1-9][0-9]{9}$'
    if not re.match(mobile_regex, str(data['mobile'])):
        return False
    
    return True

def validatePercentageSplit(*argv):
        
    total_percentage = sum(argv)
    return total_percentage == 100

def validateSplit(amt,*argv):
    total=sum(argv)
    return total==amt


