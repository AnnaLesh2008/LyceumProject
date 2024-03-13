import flask
blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_news():
    return "Обработчик в news_api"

