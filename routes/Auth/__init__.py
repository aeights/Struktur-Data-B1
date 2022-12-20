from flask import (
    render_template,
    redirect,
    Blueprint,
    request,
    session
)

from controller import *

Auth = Blueprint(
    name="Auth", import_name=__name__, template_folder="../../templates/pages/Auth"
)

@Auth.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("u_login") and request.form.get("p_login"):
            user = request.form.get("u_login")
            pw = request.form.get("p_login")
            result = controller_login(user,pw)[0]
            error = controller_login(user,pw)[1]
            if result:
                session["username"] = user
                print("ok")
                return redirect("/")
    return render_template(
        template_name_or_list="pages/Auth/login.html",
        title="Login",
        active_url="/login",
        error = error
    )

@Auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if request.form.get("u_daftar") and request.form.get("p_daftar"):
            user = request.form.get("u_daftar")
            pw = request.form.get("p_daftar")
            controller_daftar(user,pw)
            show_account()
            return redirect('/login')
    return render_template(
        template_name_or_list="pages/Auth/register.html",
        title="Register",
        active_url="/register"
    )

@Auth.route("/edit", methods=["GET", "POST"])
def edit():
    if "username" in session:
        error = None
        if request.method == "POST":
            if request.form.get("u_lama") and request.form.get("p_lama"):
                user_lama = request.form.get("u_lama")
                pw_lama = request.form.get("p_lama")
                user_baru = request.form.get("u_baru")
                pw_baru = request.form.get("p_baru")
                result = controller_login(user_lama,pw_lama)[0]
                error = controller_login(user_lama,pw_lama)[1]
                if result:
                    controller_edit(user_lama,user_baru,pw_baru)
                    return redirect('/login')
        return render_template(
            template_name_or_list="pages/Profile/edit.html",
            title="Edit",
            active_url="/edit",
            error = error
        )
    else:
        return redirect('/login')

@Auth.route("/delete", methods=["GET", "POST"])
def delete():
    if "username" in session:
        controller_hapus(session["username"])
        session.pop("username",None)
        return redirect('/login')
    else:
        return redirect('/login')

@Auth.route("/logout", methods=["GET", "POST"])
def logout():
    if "username" in session:
        session.pop("username",None)
        return redirect('/login')
    else:
        return redirect('/login')