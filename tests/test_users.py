import pytest
from jose import jwt
from app import schemas
from app.config import settings
# from tests.conftest import test_user, session, client

# This iss the Second way of doing this 


# def test_root(client):

#     res = client.get(" /")
#     print(res.json().get('message'))
#     assert res.json().get('message') == 'Hello World'
#     assert res.status_code == 200



# Goood code
def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "hello123@gmail.com", "password": "password123"})
     
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201


# def test_login_user(test_user, client):
#     res = client.post(
#         "/login", data={"username": test_user['email'] , "password" : test_user['password']})
#     login_res = schemas.Token(**res.json())
#     payload = jwt.decode(login_res.access_token,
#                           settings.secret_key, algorithms=[settings.algorithm])
#     id = payload.get("user_id")
#     assert id == test_user['id']    
#     assert login_res.token_type == "bearer"
#     assert res.status_code == 200




# def test_incorrect_login(test_user, client):
#     res = client.post(
#         "/login", data={"username": test_user['email'], "password":"wrongPassword"})
    
#     assert res.status_code == 403
#     assert res.json().get('detail') == 'Invalid Credentials'
 


# @pytest.mark.parametrize("email, password, status_code", [
#     ('wrongemail@gmail.com', 'password123', 403),
#     ('sanjeev@gmail.com', 'wrongpassword', 403),
#     ('wrongemail@gmail.com', 'wrongpassword', 403),
#     (None, 'password123', 422),
#     ('sanjeev@gmail.com', None, 422)
# ])

# def test_incorrect_login(test_user, client, email, password, status_code):
#     res = client.post(
#         "/login", data={"email": email, "password": password})

#     assert res.status_code == status_code
#     # assert res.json().get('detail') == 'Invalid Credentials'




# def test_incorrect_login(test_user, client):
#     res = client.post(
#         "/login", data={"username": test_user['email'], "password": "wrongPassword"})

#     assert res.status_code == 403
#     assert res.json().get('detail') == 'Invalid Credentials'






# def test_incorrect_login(test_user, client):
#     res = client.post(
#         "/login", data={"username": test_user['email'], "password": "wrongPassword"})

#     assert res.status_code == 403
#     assert res.json().get('detail') == 'Invalid Credentials'





















# def test_login_user(test_user, client):
#     res = client.post(
#         "/login", data={"username": test_user['email'], "password": test_user['password']})
#     login_res = schemas.Token(**res.json())
#     payload = jwt.decode(login_res.access_token,
#                          settings.secret_key, algorithms=[settings.algorithm])
#     id = payload.get("user_id")
#     assert id == test_user['id']
#     assert login_res.token_type == "bearer"
#     assert res.status_code == 200








# THIS IS THE VALIDATIONS ERRORS :


# def test_create_user(client):
#     res = client.post(
#         "/users", json={"email": "helo123@gmail.com", "password": "password123"})
    
#     new_user = schemas.UserOut(**res.json())
#     assert new_user.email == "helo123@gmail.com"
#     assert res.status_code == 201









# def test_create_user(client):

#     res = client.post("/users/", json={"email": "helo123@gmail.com", "password": "password123"})
    
#     new_user = schemas.UserOut(**res.json())
#     assert new_user.email == "helo123@gmail.com"
#     assert res.status_code == 201


 














# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#        yield db
#     finally:
#        db.close()

















# def test_create_user():

#     res = client.post(
#         "/users/", json={"email": "hello123@gmail.com", "password": "password123"})

#     new_user = schemas.UserOut(**res.json())
#     assert new_user.email  == "hello123@gmail.com"
#     assert res.status_code == 201

# def test_create_user(client):
#     res = client.post(
#         "/users/", json={"email": "hello123@gmail.com", "password": "password123"})

#     new_user = schemas.UserOut(**res.json())
#     assert new_user.email == "hello123@gmail.com"
#     assert res.status_code == 201



# tHIS IS THE 


