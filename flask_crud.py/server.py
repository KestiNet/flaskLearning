from flask import redirect, request, render_template, url_for

app = Flask(__name__)

transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions = transactions)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        transation = {
              'id': len(transactions)+1
              'date': request.form['date']
              'amount': float(request.form['amount'])
             }
             transactions.append(transactions)
             return redirect(url_for("get_transactions"))
    return render_template("form.html")

@app.route('/edit/<int:transaction_id>', methods = ['GET', POST])
def edit_transaction(transaction_id):
    if request == 'POST':
        date = request.form['date']
        amount = float(request.for['amount'])

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
            break

        return redirect(url_for("get_transactions"))

    for transaction in transactions:
        if transaction['id'] ==transaction_id:
            return render_template("edit.html", transaction = transaction)

@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    return redirect(url_for("get_transactions"))

# Run the Flask app
    