from flask import Flask, render_template, request, session, redirect
from myplace import Myplace
from bs4 import BeautifulSoup
import subprocess
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
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
@app.route("/add_one_profile", methods=["GET","POST"])
def add_one_profile():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into profile (girl_boy_id,role,socialmedia_id,optionnel_visage_voix,status_developer,username,password,email,phone,country_id) values (:girl_boy_id,:role,:socialmedia_id,:optionnel_visage_voix,:status_developer,:username,:password,:email,:phone,:country_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from profile')


        return render_template("profileform.html", profiles=user, one_user=one_user, the_title="add new profile", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from profile')
    one_user = query_db("select * from profile limit 1", one=True)
    return render_template("profileform.html", profiles=user, one_user=one_user, the_title="add new profile", touslescountry=touslescountry)

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from country')


        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_skills_music", methods=["GET","POST"])
def add_one_skills_music():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into skills_music (orchestra,chamber_music,concerto_solo,creation_artistique,performance_live_online,user_id) values (:orchestra,:chamber_music,:concerto_solo,:creation_artistique,:performance_live_online,:user_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from skills_music')


        return render_template("skills_musicform.html", skills_musics=user, one_user=one_user, the_title="add new skills_music")


    user = query_db('select * from skills_music')
    one_user = query_db("select * from skills_music limit 1", one=True)
    return render_template("skills_musicform.html", skills_musics=user, one_user=one_user, the_title="add new skills_music")

@app.route("/add_one_skills_it", methods=["GET","POST"])
def add_one_skills_it():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into skills_it (orchestration_conteneurs_musicale,network_engineerung,dev_tools,monitoring_stats_vues_popularite,socialmedia_skill_it) values (:orchestration_conteneurs_musicale,:network_engineerung,:dev_tools,:monitoring_stats_vues_popularite,:socialmedia_skill_it)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from skills_it')


        return render_template("skills_itform.html", skills_its=user, one_user=one_user, the_title="add new skills_it")


    user = query_db('select * from skills_it')
    one_user = query_db("select * from skills_it limit 1", one=True)
    return render_template("skills_itform.html", skills_its=user, one_user=one_user, the_title="add new skills_it")

@app.route("/add_one_content_flow", methods=["GET","POST"])
def add_one_content_flow():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslessocialmedia= query_db("select * from socialmedia")

        one_user = query_db("insert into content_flow (content,type_it_musical,socialmedia_id) values (:content,:type_it_musical,:socialmedia_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from content_flow')


        return render_template("content_flowform.html", content_flows=user, one_user=one_user, the_title="add new content_flow", touslessocialmedia=touslessocialmedia)


    touslessocialmedia= query_db("select * from socialmedia")

    user = query_db('select * from content_flow')
    one_user = query_db("select * from content_flow limit 1", one=True)
    return render_template("content_flowform.html", content_flows=user, one_user=one_user, the_title="add new content_flow", touslessocialmedia=touslessocialmedia)

@app.route("/add_one_socialmedia", methods=["GET","POST"])
def add_one_socialmedia():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into socialmedia (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from socialmedia')


        return render_template("socialmediaform.html", socialmedias=user, one_user=one_user, the_title="add new socialmedia")


    user = query_db('select * from socialmedia')
    one_user = query_db("select * from socialmedia limit 1", one=True)
    return render_template("socialmediaform.html", socialmedias=user, one_user=one_user, the_title="add new socialmedia")

@app.route("/add_one_projet", methods=["GET","POST"])
def add_one_projet():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into projet (skills_music_id,skills_it,profile_id,website_description) values (:skills_music_id,:skills_it,:profile_id,:website_description)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from projet')


        return render_template("projetform.html", projets=user, one_user=one_user, the_title="add new projet")


    user = query_db('select * from projet')
    one_user = query_db("select * from projet limit 1", one=True)
    return render_template("projetform.html", projets=user, one_user=one_user, the_title="add new projet")

