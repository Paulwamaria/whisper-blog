import secrets,os
from app import create_app
from flask import render_template,redirect,url_for
from . import auth
from flask import flash,request
from .forms import RegistrationForm,LoginForm,UpdateAccountForm,PostForm 
from .. models import User, Post
from .. import db,bcrypt
from flask_login import login_user,logout_user,login_required,current_user


app=create_app()

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

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex +f_ext
    picture_path = os.path.join(app.root_path, 'static/images',picture_fn)
    form_picture.save(picture_path)

    return picture_fn


@auth.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username=form.username.data 
        current_user.email=form.email.data
        db.session.commit()
        flash('Your account has been updated','success')
        return redirect(url_for('auth.account'))

    elif request.method== 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file=url_for('static', filename='images/' + current_user.image_file)
    return render_template('auth/account.html',title='Account', image_file = image_file, update_form = form )


@auth.route('/post/new', methods = ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data,content = form.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created','success')
        return redirect(url_for('main.index'))
    return render_template('create_post.html', title =' New Post',post_form=form, legend='New post')

@auth.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html',post=post, title = post.title) 


@auth.route('/post/<int:post_id>/update',methods= ['GET','POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated","success")
        return redirect(url_for('auth.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html',post=post, legend = 'Update Post',post_form=form) 


@auth.route('/post/<int:post_id>/delete',methods= ['GET','POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been delete succesifuly','success')

    return redirect(url_for('main.index'))