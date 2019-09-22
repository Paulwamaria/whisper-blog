from flask import render_template,redirect,url_for
from . import auth
from flask import flash
from .forms import RegistrationForm,LoginForm

from flask_login import login_user,logout_user,login_required



@auth.route('/register', methods=['GET',"POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account for {{form.username.data}} successifuly created','success')

        return redirect(url_for('main.index'))



    return render_template('auth/register.html',title="Register",registration_form =form )



@auth.route('/login',methods=["GET","POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'paulwamaria@gmail.com' and form.password.data == 'lee':
            flash('You have been logged in!','success')
            return redirect(url_for('main.index'))

        else:
            flash('Login unsuccesiful, please check username and password','danger')


    return render_template('auth/login.html', title="Login",login_form =form)