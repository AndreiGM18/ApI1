from flask import Flask, request

app = Flask(__name__, static_folder="public")

# you can use a dict as user/pass database
ALLOWED_USERS = { "admin": "n0h4x0rz-plz" }


@app.route("/index.html")
def index():
    # TODO: render the index page using our template
    return render_template("index.html")


# TODO (Task 03 - Authentication)
@app.route("/login.html")
def login():
    error_msg = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        # TODO: verify credentials and set the session variables
        pass
    # return render_template("login.html", error_msg=error_msg)
    return "TODO"

@app.route("/logout.html")
def logout():
    # clear authentication status
    #session["authenticated"] = 0;
    #return redirect("/index.html")
    return "TODO"

# TODO (Task 04 - File Upload)
@app.route("/upload.html")
def upload():
    return "TODO"


if __name__ == "__main__":
    app.run(debug=True)

