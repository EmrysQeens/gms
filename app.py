from flask import redirect, Flask

app =  Flask(__name__)

@app.route("/")
def index():
	return redirect("https://drive.google.com/file/d/1-UwVfzntr0klItfUVUWuBp2ZLcjCEeNq/view?usp=drivesdk")


if __name__ == "__main__":
	app.run(debug=True, port=5000)
