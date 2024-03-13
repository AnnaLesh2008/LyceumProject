from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/5').json())
print(get('http://localhost:5000/api/v2/users/85').json())

print(post('http://localhost:5000/api/v2/users').json())
print(post('http://localhost:5000/api/v2/users', json={'name':'Name'}).json())
print(post('http://localhost:5000/api/v2/users', json={'name':'Name', 'surname': 'Surname', 'age': '15',
                                                       'position': 'position', 'speciality': 'speciality',
                                                       'address': 'address', 'email': 'email', 'hashed_password': 'jujriuriririri'}).json())

print(delete('http://localhost:5000/api/v2/users/5').json())
print(delete('http://localhost:5000/api/v2/users/9999').json())


