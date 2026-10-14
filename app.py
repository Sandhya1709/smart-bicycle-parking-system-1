from flask import Flask, render_template, request, send_file
from fake_database import add_user
from generate_qr import generate_qr

app = Flask(__name__)

# Home page

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        new_user = add_user(name, email)

        return render_template(
            "qr.html",
            user=new_user
        )

    return render_template("register.html")


@app.route("/qr/<user_id>")
def show_qr(user_id):
    qr_buffer = generate_qr(user_id)

    return send_file(
        qr_buffer,
        mimetype="image/png"
    )


@app.route("/qr/<user_id>/download")
def download_qr(user_id):
    qr_buffer = generate_qr(user_id)

    return send_file(
        qr_buffer,
        mimetype="image/png",
        as_attachment=True,
        download_name=f"{user_id}.png"
    )


if __name__ == "__main__":
    app.run(debug=True)