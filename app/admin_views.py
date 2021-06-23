from app import app
@app.route("/admin")
def admin():
    return "admin"
@app.route("/adminprofile")
def admin_profile():
    return "welocme to admin"