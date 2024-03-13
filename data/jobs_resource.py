from flask_restful import Resource
from werkzeug.security import generate_password_hash

from data import db_session
from flask import abort, jsonify
from data.jobs import Jobs
from data.parser2 import parser2
from data.user_resources import abort_if_news_not_found


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        return jsonify({'jobs': jobs.to_dict(
            only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))})

    def delete(self, users_id):
        abort_if_news_not_found(users_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(users_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})

class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished')) for item in jobs]})

    def post(self):
        args = parser2.parse_args()
        session = db_session.create_session()
        news = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            end_date=args['end_date'],
            is_finished = args['is_finished']
        )
        session.add(news)
        session.commit()
        return jsonify({'id': news.id})