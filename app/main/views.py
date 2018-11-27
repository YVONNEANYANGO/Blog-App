from flask import render_template,request,redirect,url_for,abort
# from app import app
from ..models import Comment, User, Blog
from .. import db,photos
from . import main
from flask_login import login_required,current_user
from .forms import UpdateProfileForm, FlyingForm,AdventureForm,CruiseForm,GlampingForm
# from ..models import Comments
from .forms import CommentForm
# Comment = comment.Comment

def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome A FANTASY EXPERIENCE BLOG Website Online'
    return render_template('index.html', title = title)

# Views
@main.route('/')
@login_required
def index():
    '''
    View root page function that returns the index page and its data
    '''

    message = 'Welcome A FANTASY EXPERIENCE BLOG Website !!!'
    print(message)
    return render_template('index.html',message = message)


@main.route('/blog/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):


    @main.route('/user/<uname>')
    def profile(uname):
        '''
        views
        '''
        user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html')


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/comment/<blog_id>', methods = ["GET","POST"]) 
def comment(blog_id):

    '''
    View blog page function that returns the blog details page and its data
    '''
    blog = Blog.query.filter_by(id = blog_id).first()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.body.data
        new_comment = Comment(comment = comment, blog = blog)
        db.session.add(new_comment)
        db.session.commit()

    return render_template('comment.html',comment_form =  comment_form)

@main.route('/flying', methods = ["GET","POST"])
def flying():
    form = FlyingForm()
    if form.validate_on_submit():
        flying = form.body.data
        blog = Blog(description = flying, user = current_user, category = "flying")
        db.session.add(blog)
        db.session.commit()
        
    blogs = Blog.query.filter_by(category = "flying")
    '''
    View blog page function that returns the pitch details page and its data
    '''
    return render_template('flying.html', form = form, flying_data = blogs)

@main.route('/adventure', methods = ["GET","POST"])
def Adventure():
    form = AdventureForm()
    if form.validate_on_submit():
        adventure = form.body.data 
        blog = Blog(description = adventure, user = current_user, category = "adventure")
        db.session.add(blog)
        db.session.commit()
        
    blogs = Blog.query.filter_by(category = "adventure")
    
    '''
    View blog page function that returns the blog details page and its data
    '''
    return render_template('adventure.html',form =form, adventure_data =blogs)

@main.route('/cruise', methods = ["GET","POST"])
def cruise():
    form = CruiseForm()
    if form.validate_on_submit():
        cruise = form.body.data
        blog = Blog(description = cruise, user = current_user, category = "cruise")
        db.session.add(blog)
        db.session.commit()


    blogs = Blog.query.filter_by(category = "cruise")
    
    '''
    View blog page function that returns the blog details page and its data
    '''
    return render_template('cruise.html', form = form, cruise_data = blogs)

@main.route('/glamping', methods = ["GET","POST"])
def glamping():
    form = GlampingForm()
    if form.validate_on_submit():
        glamping = form.body.data
        blog = Blog(description = glamping, user = current_user, category = "glamping")
        db.session.add(blog)
        db.session.commit()
        
    blogs = Blog.query.filter_by(category = "glamping")
    
    '''
    View blog page function that returns the blog details page and its data
    '''
    return render_template('glamping.html', form = form, glamping_data = blogs)
@main.route("/view/comments/<blog_id>")
def view_comments(blog_id):

    comments = Comment.query.filter_by(blog_id = blog_id)

    return render_template("view_comments.html", comments = comments)
# # comment-section
# @main.route('/comments/<int:id>', methods=['GET','POST']