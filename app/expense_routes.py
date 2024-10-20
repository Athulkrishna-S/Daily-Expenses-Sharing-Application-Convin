from flask import Blueprint, request , jsonify
from app.models import addExpense, findUser, findUsers
#from app.utils import validate_user_data


expense_bp=Blueprint('expense',__name__)

@expense_bp.route('/add',methods=['POST'])
def addExpenseRoute():
    """
    Endpoint to add an expense.

    Expected JSON body:
    - payer: (str) Email of the user who paid the expense.
    - amount: (float) Total amount of the expense.
    - participants: (dict) A dictionary with participant emails as keys and their share as values.
      * For equal split: participants' values can be 0, which will be divided equally.
      * For exact split: participants' values should add up to the total amount.
      * For percentage split: participants' values should add up to 100 (percentage).
    - method: (str) The method to split the expense ("equal", "exact", "percentage").
    - purpose: (str) A brief description or purpose for the expense (e.g., "Dinner at restaurant").
    
    Returns:
    - JSON response with success or error message.
    """

    data = request.get_json()

    payer=data.get("payer")
    amount = data.get("amount")
    participants = data.get("participants")
    method = data.get("method")
    purpose = data.get("purpose")

    try:
        
        emails = [payer]+list(participants.keys())
        user_dict = findUsers(emails)

        for email in emails:
            if email not in user_dict:
                return jsonify({"message": f"User not found {email}", "statusCode": 404}), 404

        if method.lower() == "equal":
            equal_share = amount / len(emails)
            updates=[]
            for participant in emails:
                updates.append(
                    {
                        "filter": {"email": participant},
                        "purpose": purpose,
                        "share": equal_share
                    })
            addExpense(updates)
        
        return jsonify({"message": "Expense added successfully", "statusCode": 200}), 200

    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e), "statusCode": 500}), 500