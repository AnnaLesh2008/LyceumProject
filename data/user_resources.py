from flask_restful import Resource
from werkzeug.security import generate_password_hash

from data import db_session
from flask import abort, jsonify
from data.user import User
from data.parser import parser


def set_password(self, password):
    self.hashed_password = generate_password_hash(password)

def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(User).get(news_id)
    if not news:
        abort(404, message=f"Users {news_id} not found")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_news_not_found(users_id)
        session = db_session.create_session()
        news = session.query(User).get(users_id)
        return jsonify({'news': news.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email'))})

    def delete(self, users_id):
        abort_if_news_not_found(users_id)
        session = db_session.create_session()
        news = session.query(User).get(users_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})

class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email')) for item in news]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = Users(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email = args['email'],
            hashed_password=set_password(args['password'])
        )
        session.add(news)
        session.commit()
        return jsonify({'id': news.id})