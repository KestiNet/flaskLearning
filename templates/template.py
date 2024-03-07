from Flask import Flask, render_template, request
app = Flask("My first Application")

@app.route('/sample')
def getSampleHtml():
    return render_template ('sample.html')

app.route('/user/< username >', methods = ['GET'])
def greetUser(username):
    return render_template("result.html", username=username)

@app.route('user', methods=['GET'])
def greeetUserBasedOnReq():
    username = request.args.get("username")
    return rende_template("result.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)


