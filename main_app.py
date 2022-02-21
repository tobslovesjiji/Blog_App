from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '0a03872ea9d2848cb5e66bf7f4e3cdfa'

posts = [

    {
       'author': 'tobs',
       'title': 'Blog Post 1',
       'content': 'First post content',
       'date_posted': 'February 14th, 2022'
    },

    {
       'author': 'jaks',
       'title': 'Blog Post 2',
       'content': 'Second post content',
       'date_posted': 'February 15th, 2022'
    },

    {
       'author': 'jiji',
       'title': 'Blog Post 3',
       'content': 'Third post content',
       'date_posted': 'February 16th, 2022'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__=='__main__':
    app.run(debug=True)