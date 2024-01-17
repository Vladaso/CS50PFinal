from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from Quizzer import Quizzer
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import json
from flask import flash
import os

app = Flask(__name__)  
app.secret_key = 'test'
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, username, email, password, cat=None, description=None):
        self.id = username
        self.email = email
        self.password = password
        self.cat = cat
        self.description = description


def main():
    app.run(debug=True)


@login_manager.user_loader
def load_user(user_id):
    if os.path.getsize('users.json') > 0:
            with open('users.json', 'r') as f:
                users = json.load(f)
    else:
        users = {}
    if user_id in users:
        user_data = users[user_id]
        return User(user_id, user_data['email'], user_data['password'],user_data['cat'],user_data['description'])
    return None


@app.route("/",methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        current_user.cat = get_cat(evaluate(request.form))[0]
        current_user.description = get_cat(evaluate(request.form))[1]
        with open('users.json', 'r') as f:
            users = json.load(f)
        users[current_user.id]['cat'] = current_user.cat
        users[current_user.id]['description'] = current_user.description
        with open('users.json', 'w') as f:
            json.dump(users, f)
        return redirect(url_for("my_cat"))
    quiz = Quizzer()
    return render_template("index.html", quiz = quiz)

def get_cat(num):
    cat_mapping = {
         0: ["American Shorthair", "Even tempered and quiet."],
    1: ["American Shorthair", "Even tempered and quiet."],
    2: ["American Wirehair", "Even temperament."],
    3: ["American Wirehair", "Even temperament."],
    4: ["Bombay", "Playful and affectionate, they make great lap cats."],
    5: ["Bombay", "Playful and affectionate, they make great lap cats."],
    6: ["British Shorthair", "Curious cats that like to relax. They also enjoy company and will chill happily on the couch next to you."],
    7: ["British Shorthair", "Curious cats that like to relax. They also enjoy company and will chill happily on the couch next to you."],
    8: ["Burmese", "This breed becomes attached to their family very quickly and is very outgoing."],
    9: ["Burmese", "This breed becomes attached to their family very quickly and is very outgoing."],
    10: ["Chartreux", "Gentle, playful yet quiet cats."],
    11: ["Chartreux", "Gentle, playful yet quiet cats."],
    12: ["Himalayan", "These cats like peaceful environments, so may not enjoy a home full of children but may be good as a companion for a senior."],
    13: ["Himalayan", "These cats like peaceful environments, so may not enjoy a home full of children but may be good as a companion for a senior."],
    14: ["LaPerm", "Affectionate and gentle, likes sitting on your lap but also very active so enjoy games."],
    15: ["LaPerm", "Affectionate and gentle, likes sitting on your lap but also very active so enjoy games."],
    16: ["Maine Coon", "Gentle cats that are good companions that enjoy mental challenges so they like lots of playtime."],
    17: ["Maine Coon", "Gentle cats that are good companions that enjoy mental challenges so they like lots of playtime."],
    18: ["RagaMuffin", "Affectionate, docile and loves people - and yes, we love the name as much as you do!"],
    19: ["Turkish Van", "Sweet and curious."],
    20: ["Abyssinian", "Busy, active, purposeful, and affectionate cats with lots of energy. These kitties are intelligent and talkative!"],
    21: ["Bengal", "Curious, energetic and athletic. Require plenty of stimulation both mentally and physically."],
    22: ["Devon Rex", "Has the look and personality of a Pixie."],
    23: ["Norwegian Forest Cat", "An active breed that loves hunting and climbing."],
    24: ["Ocicat", "A strong, active and sociable cat."],
    25: ["Siamese", "Determined, vocal, active, affectionate cats but they don’t like being left alone."],
    26: ["Siamese", "Determined, vocal, active, affectionate cats but they don’t like being left alone."],
    27: ["Ragdoll", "Lots of energy and very curious cats so like to know what’s going on!"],
    28: ["Ragdoll", "Lots of energy and very curious cats so like to know what’s going on!"],
    29: ["Balinese", "Known for their intelligence and inquisitive nature, they make loving companions that will sit quietly with you, and often enjoy being petted."],
    30: ["Balinese", "Known for their intelligence and inquisitive nature, they make loving companions that will sit quietly with you, and often enjoy being petted."]
    }
    return cat_mapping[num]

def evaluate(answers):
    sum = 0
    for key, value in answers.items():
            sum += int(value)
    if sum>30 or sum<0:
        raise ValueError("Invalid score")
    return sum

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if os.path.getsize('users.json') > 0:
            with open('users.json', 'r') as f:
                users = json.load(f)
        else:
            users = {}

        if username in users and check_password_hash(users[username]['password'], password):
            login_user(User(username, users[username]['email'], users[username]['password'], users[username]['cat'], users[username]['description']))
            return redirect(url_for("index"))
        flash("Invalid login details")
    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if os.path.getsize('users.json') > 0:
            with open('users.json', 'r') as f:
                users = json.load(f)
        else:
            users = {}

        if username in users:
            flash("Username already exists")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)
        users[username] = {"email": email, "password": hashed_password, "cat": None, "description": None}

        with open('users.json', 'w') as f:
            json.dump(users, f)

        user = User(username, email, password)
        login_user(user)
        return redirect(url_for("index"))

    return render_template("register.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/results")
@login_required
def my_cat():
    user_cat = current_user.cat
    user_desc = current_user.description
    return render_template('results.html', cat=user_cat, description = user_desc)


def create_users_file():
    if not os.path.exists('users.json'):
        with open('users.json', 'w') as f:
            json.dump({}, f)

if __name__ == "__main__":
    create_users_file()
    main()