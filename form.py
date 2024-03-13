# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         return redirect('/success')
#     return render_template('login.html', title='Авторизация', form=form)
#
#
# @app.route('/success')
# def success():
#     return '<h1>Успешно!</h1>'