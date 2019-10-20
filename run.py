# The main difference between the two is that the blog post submission form and blog post listings will be on separate pages in our Build-a-Blog app.
from datetime import datetime
from flask import Flask, request, redirect, render_template, url_for, flash
from forms import Registration,Login

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key='768a109a77986d0fb77db7edd56dad5d'

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:NZVfW5UnVvnLygtJ@localhost:8889/build-a-blog'

app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
from models import User,Post

posts = [
    {

        'author':'Adrienne Christina',
        'title': 'I found the error!',
        'content': 'So I guess comments in the editor can mess up everything....',
        'date_posted': 'October 16, 2019'
    },
    {
       'author':'Adrienne Christina',
        'title': 'Ugh',
        'content': 'Guess what happened today? Nothing new, more stress and frustration!',
        'date_posted': 'October 17, 2019' 
    }
]
posts_again = [
    {

        'author':'Adrienne Christina',
        'title': 'yeet',
        'content': 'So I guess comments in the editor can mess up everything....',
        'date_posted': 'October 16, 2019'
    },
    {
       'author':'Adrienne Christina',
        'title': 'is it working yet?',
        'content': 'Guess what happened today? Nothing new, more stress and frustration!',
        'date_posted': 'October 17, 2019' 
    }
]



@app.route('/', methods=['GET','POST'])
def index():
        return render_template('blog.html',posts=posts)


@app.route('/newblog',methods=['GET','POST'])
def new_post():
    return render_template('newblog.html') 

@app.route('/addnewpost',methods=['GET','POST'])
def userposts():
    return render_template('userposts.html') #title='New Post', form=form) 
    title='' 
    if 'submit'==True:
        return render_template('submitted.html') 

@app.route('/posts_on_click',methods=['GET','POST'])
def posts_on_click():
    return render_template('posts_on_click.html',posts_again=posts_again) 

# @app.route('/submitted',methods=['GET','POST'])
# def submitted():
#     if request.method=='POST':
#         return render_template('submitted.html') 

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registration()
    # if request.method=='POST':
    #     email = request.form['email']
    #     password = request.form['password']
    #     confirm_password == request.form['confirm_password']
    #     if password == confirm_password:
    #         flash(f'Welcome, {form.username.data}!')
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome, {form.username.data}! You can now log back in anytime.')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    form = Login()
    # if request.method=='POST':
    #     email = request.form['email']
    #     password = request.form['password']
    #     user = User.query.filter_by(email=email).first()
        
    #     if user and user.password == password:
    #         flash(f'Welcome back, {form.username.data}!')
    if form.validate_on_submit():
        flash(f'Welcome back, {form.username.data}!')
    else:
            #return '<h1>no work</h1>'
        flash(f'Invalid username/password')
    return redirect(url_for('index',form=form))
    #return render_template('blog.html', title='Login', form=form)

if __name__ == '__main__':
    app.run()
