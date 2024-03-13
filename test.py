import requests
from requests import get, post, delete

print(get('http://localhost:8080/api/jobs').json())
print(get('http://localhost:8080/api/jobs/4').json())
print(get('http://localhost:8080/api/jobs/999').json())
print(get('http://localhost:8080/api/jobs/q').json())

#тесты для добавления работы
print(post('http://localhost:8080/api/jobs', json={}).json())

print(post('http://localhost:8080/api/jobs',
           json={'job': 'name_of_job'}).json())

print(post('http://localhost:8080/api/jobs',
           json={'job': 'name_of_job',
                 'team_leader': '4',
                 'work_size': 50,
                 'collaborators': '5, 8'}).json())

print(delete('http://127.0.0.1:8080/api/delete_job/999').json())

print(delete('http://127.0.0.1:8080/api/delete_job/1').json())

