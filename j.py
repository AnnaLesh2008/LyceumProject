from requests import get, post, delete

print(get('http://localhost:5000/api/v2/jobs').json())
print(get('http://localhost:5000/api/v2/jobs/5').json())
print(get('http://localhost:5000/api/v2/jobs/85').json())

print(post('http://localhost:5000/api/v2/jobs').json())
print(post('http://localhost:5000/api/v2/jobs', json={'job':'Job'}).json())
print(post('http://localhost:5000/api/v2/jobs', json={'team_leader':'Team_leader', 'job': 'Job', 'work_size': '15',
                                                       'collaborators': '2, 8', 'start_date': 'today',
                                                       'end_date': 'POTOM', 'is_finished': 'False'}).json())

print(delete('http://localhost:5000/api/v2/jobs/5').json())
print(delete('http://localhost:5000/api/v2/jobs/9999').json())
