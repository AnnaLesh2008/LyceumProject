from flask_restful import reqparse, abort, Api
from flask import request, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask import Flask, render_template, redirect, abort
from forms.user import RegisterForm, LoginForm
from data.jobs import Jobs
from data.user import User
from forms.job import JobRegisterForm
from data import db_session
from data import user_resources
from data import jobs_resource
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
api = Api(app)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
def i():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return render_template("base2.html", news=news)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")

        user3 = User()
        user3.surname = form.name.data
        user3.name = form.surname.data
        user3.email = form.email.data
        user3.position = form.position.data
        user3.speciality = form.speciality.data
        user3.age = form.age.data
        user3.address = form.address.data
        user3.set_password(form.password.data)
        db_sess = db_session.create_session()
        db_sess.add(user3)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/addjob', methods=['GET', 'POST'])
@login_required
def addjob():
    form = JobRegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = False
        current_user.job.append(job)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('new_job.html', title='Добавление новости',
                           form=form)


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = JobRegisterForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                         Jobs.user == current_user
                                         ).first()
        if job:
            form.job.data = job.job
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
            db_sess.commit()
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                         Jobs.user == current_user
                                         ).first()
        if job:
            form.job.data = job.job
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
            db_sess.commit()
        else:
            abort(404)
    return render_template('edit_job.html',
                           title='Редактирование работки',
                           form=form
                           )


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).filter(Jobs.id == id,
                                      Jobs.user == current_user
                                      ).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')

from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

# job = Jobs()
# job.team_leader = 1
# job.job = 'deployment of residential modules 1 and 2'
# job.work_size = 15
# job.collaborators = '2, 3'
# job.is_finished = False


# db_sess.add(job)
# db_sess.commit()
api.add_resource(user_resources.UsersListResource, '/api/v2/users')
api.add_resource(user_resources.UsersResource, '/api/v2/users/<int:users_id>')
api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')
api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:jobs_id>')
if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    # app.register_blueprint(jobs_api.blueprint)
    # db_sess = db_session.create_session()
    # colonist = db_sess.query(User).filter(User.age < 18)
    # colonist1 = db_sess.query(User).filter((User.position.like('%chief%')) | (User.position.like('%middle%')))
    # for user in colonist:
    #     print(user + f"{user.age} years")

    # db_sess = db_session.create_session()
    # news = db_sess.query(Jobs).all()
    app.run(port=8080, host='127.0.0.1')
