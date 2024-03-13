from flask_restful import reqparse

parser2 = reqparse.RequestParser()
parser2.add_argument('team_leader', required=True)
parser2.add_argument('job', required=True)
parser2.add_argument('work_size', required=True)
parser2.add_argument('collaborators', required=True)
parser2.add_argument('start_date', required=True)
parser2.add_argument('end_date', required=True)
parser2.add_argument('is_finished', required=True)