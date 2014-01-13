from flask import Flask, render_template, request
import julian

app = Flask(__name__)

@app.route("/")
def index():
    julian_date = julian.todays_julian_date()
    return render_template("index.html", date=julian_date)

if __name__ == "__main__":
    app.run(debug=True)