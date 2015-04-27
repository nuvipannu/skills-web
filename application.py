from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route("/index")
# def index():
#     return "we are here"

@app.route("/application-form")
def mn_application_form():
    return render_template("application-form.html")

@app.route("/application", methods=["GET"])
def mn_response():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    job = request.args.get("job")
    salary = request.args.get("salary")

    return render_template("application-response.html", firstname=firstname, lastname=lastname, job=job, salary=salary)

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)