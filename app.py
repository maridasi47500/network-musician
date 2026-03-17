from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,country_id,phone,email) values (:username,:country_id,:phone,:email)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_itskills", methods=["GET","POST"])
def add_one_itskills():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into itskills (name) values (:name)",request.form)
        user = query_db('select * from itskills')
        return render_template("itskillsform.html", itskillss=user, one_user=one_user, the_title="add new itskills")
    user = query_db('select * from itskills')
    one_user = query_db("select * from itskills limit 1", one=True)
    return render_template("itskillsform.html", itskillss=user, one_user=one_user, the_title="add new itskills")

@app.route("/add_one_musicalskills", methods=["GET","POST"])
def add_one_musicalskills():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into musicalskills (name) values (:name)",request.form)
        user = query_db('select * from musicalskills')
        return render_template("musicalskillsform.html", musicalskillss=user, one_user=one_user, the_title="add new musicalskills")
    user = query_db('select * from musicalskills')
    one_user = query_db("select * from musicalskills limit 1", one=True)
    return render_template("musicalskillsform.html", musicalskillss=user, one_user=one_user, the_title="add new musicalskills")

@app.route("/add_one_userhasmusicalskill", methods=["GET","POST"])
def add_one_userhasmusicalskill():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into userhasmusicalskill (skill_id,user_id) values (:skill_id,:user_id)",request.form)
        user = query_db('select * from userhasmusicalskill')
        return render_template("userhasmusicalskillform.html", userhasmusicalskills=user, one_user=one_user, the_title="add new userhasmusicalskill")
    user = query_db('select * from userhasmusicalskill')
    one_user = query_db("select * from userhasmusicalskill limit 1", one=True)
    return render_template("userhasmusicalskillform.html", userhasmusicalskills=user, one_user=one_user, the_title="add new userhasmusicalskill")

@app.route("/add_one_userhasitskill", methods=["GET","POST"])
def add_one_userhasitskill():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into userhasitskill (skill_id,user_id) values (:skill_id,:user_id)",request.form)
        user = query_db('select * from userhasitskill')
        return render_template("userhasitskillform.html", userhasitskills=user, one_user=one_user, the_title="add new userhasitskill")
    user = query_db('select * from userhasitskill')
    one_user = query_db("select * from userhasitskill limit 1", one=True)
    return render_template("userhasitskillform.html", userhasitskills=user, one_user=one_user, the_title="add new userhasitskill")

