from flask import Blueprint, request , jsonify, send_file, render_template_string
from app.models import addExpense, findUsers, findAllUsers, findUser
from app.utils import validatePercentageSplit, validateSplit
from app.balanceSheet import generateBalanceSheet
import io


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
    
    Note: The payer's email must be included in the participants dictionary if they are to be included in the expense split.

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
        
        emails = list(participants.keys())
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

        elif method.lower() == "percentage":

            if not validatePercentageSplit(*participants.values()):
                return jsonify({"error": "Percentages must add up to 100", "statusCode": 400}), 400
        
            updates=[]
            for participant, percentage in participants.items():
                amt = (percentage / 100) * amount
                updates.append(
                    {
                        "filter": {"email": participant},
                        "purpose": purpose,
                        "share": amt
                    })
            addExpense(updates)
        
        elif method.lower() == "exact":

            if not validateSplit(amount,*participants.values()):
                return jsonify({"error": f"Split must add up to {amount}", "statusCode": 400}), 400
        
            updates=[]
            for participant, amt in participants.items():
                updates.append(
                    {
                        "filter": {"email": participant},
                        "purpose": purpose,
                        "share": amt
                    })
            addExpense(updates)
        else:
            return jsonify({"error": "Invalid Split Method", "statusCode": 400}), 400

        return jsonify({"message": "Expense added successfully", "statusCode": 200}), 200

    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e), "statusCode": 500}), 500
    
@expense_bp.route('/download/balanacesheet',methods=['GET'])
def downloadBalanceSheet():
    try:
        
        user_list = findAllUsers()

        pdf_file = generateBalanceSheet(user_list)

        return send_file(
            io.BytesIO(pdf_file),
            mimetype='application/pdf',
            as_attachment=True,
            download_name='balance_sheet.pdf'
        )
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e), "statusCode": 500}), 500
    

@expense_bp.route('/getData/<username>', methods=['POST'])
def getUserExpense(username):
    '''
    Expected JSON body:

    - email: (str) Email of the user
    '''

    try:
        data = request.get_json()

        # Validate input data
        if not data or 'email' not in data:
            return jsonify({"error": "Email is required", "statusCode": 400}), 400

        email = data['email']
        res = findUser(email)

        # Check if the user was found
        if res is None:
            return jsonify({"error": f"User with email '{email}' not found", "statusCode": 404}), 404

        return jsonify({"Expenses": res['expenses'], "StatusCode": 200}), 200

    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e), "statusCode": 500}), 500


@expense_bp.route('/getData', methods=['GET'])
def getAllExpense():
    try:


        res = findAllUsers()

        # Check if the user was found
        if res is None:
            return jsonify({"error": "No users found", "statusCode": 404}), 404
        
        overall_expenses = {}
        total_expense = 0
        
        for user in res:
            for purpose, amount in user.get("expenses", {}).items():
                overall_expenses[purpose] = overall_expenses.get(purpose, 0) + amount
                total_expense += amount

        overall_expenses["Total"]=total_expense
        return jsonify({"Data": overall_expenses, "StatusCode": 200}), 200

    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e), "statusCode": 500}), 500
