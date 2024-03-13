import flask
from flask import jsonify, make_response, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/delete_job/<int:job_id>', methods=['DELETE'])
def delete_one_job(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return make_response(jsonify({'Ошибочка': 'Нет, такой работы:)'}), 404)
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'id', 'job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
        }
    )

@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['job', 'team_leader', 'work_size', 'collaborators']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    jobs = Jobs(
        job = request.json['job'],
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'id': jobs.id})

@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def create_jobs(job_id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).get(job_id)
    jobs = Jobs(
        job = request.json['job'],
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'id': jobs.id})
