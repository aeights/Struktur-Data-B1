from flask import (
    render_template,
    Blueprint,
    session,
    redirect
)

Home = Blueprint(
    name="Home", import_name=__name__, template_folder="../../templates/pages/Home"
)

@Home.route("/")
@Home.route("/home")
def home():
    if "username" in session:
        return render_template(
            template_name_or_list="pages/Home/landing-page.html",
            title="Selamat Datang",
            active_url="/",
            username = session["username"]
        )
    else:
        return redirect('/login')
