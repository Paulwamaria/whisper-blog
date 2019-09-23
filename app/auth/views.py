from flask import render_template,redirect,url_for
from . import auth
from flask import flash,request
from .forms import RegistrationForm,LoginForm
from .. models import User, Post
from .. import db,bcrypt
from flask_login import login_user,logout_user,login_required,current_user




@auth.route('/register', methods=['GET',"POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    
    if form.validate_on_submit():
        
        user = User(username=form.username.data,email=form.email.data,password = form.password.data)
       
        db.session.add(user)
        db.session.commit()
        flash(f"Account for {form.username.data} successifuly created",'success')

        return redirect(url_for('auth.login'))



    return render_template('auth/register.html',title="Register",registration_form =form )



@auth.route('/login',methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('auth/login.html', title='Login', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth.route('/account')
@login_required
def account():

    return render_template('auth/account.html',title='Account')