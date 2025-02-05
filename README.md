*** Test register/

Request user creation

```
curl --location 'http://127.0.0.1:8000/register_user/'
--form 'email="test@gmail.com"'
--form 'username="juanma"'
--form 'first_name="Juan Manuel"'
--form 'last_name="de las Heras Arroyo"'
--form 'password="Enunlugardelamancha"'
```
Response
```
{
    "id": 3,
    "email": "test@gmail.com",
    "username": "juanma",
    "first_name": "Juan Manuel",
    "last_name": "de las Heras Arroyo"
}
```

Test api/token/

request valid user

```
curl --location 'http://127.0.0.1:8000/api/token/' --form 'username="juanma"' --form 'password="enunlugardelamancha"'
```
Response
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczODgxMTg4MiwiaWF0IjoxNzM4NzI1NDgyLCJqdGkiOiJmMmQzYzY3YTU5MTI0ZDFhOTk2YTBlNGQ4ZjE1OTE1NyIsInVzZXJfaWQiOjJ9.iKfQ-8ehj2hL4MTStdr2Y2fqzkkemiKXzJDg4u-0mxs",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4NzI5MDgyLCJpYXQiOjE3Mzg3MjU0ODIsImp0aSI6IjE3ZGViOTYxNDkwYTQxMzY5NmVkNzJlY2JlYjhlMjYwIiwidXNlcl9pZCI6Mn0.muisS9ehx6cUBVnUUdm3oTLN-KFcF9dWiF3gb1uLh4g"
}
```

request invalid user

```
curl --location 'http://127.0.0.1:8000/api/token/' --form 'username="baduser"' --form 'password="enunlugardelamancha"'
```
Response
```
{
    "detail": "No active account found with the given credentials"
}
```

request valid task creation
```
curl --location 'http://127.0.0.1:8000/create_task/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4NzI5MDgyLCJpYXQiOjE3Mzg3MjU0ODIsImp0aSI6IjE3ZGViOTYxNDkwYTQxMzY5NmVkNzJlY2JlYjhlMjYwIiwidXNlcl9pZCI6Mn0.muisS9ehx6cUBVnUUdm3oTLN-KFcF9dWiF3gb1uLh4g' \
--form 'title="Submit test results to NDS"' \
--form 'details="After finishing the project, submit github link to NDS for evaluation"' \
--form 'username="juanma"' \
--form 'starts_on="2025-02-04T12:00"' \
--form 'ends_on="2025-02-05T09:00"'
```
Response
```
{
    "id": 3,
    "title": "Submit test results to NDS",
    "author": {
        "id": 2,
        "username": "juanma",
        "first_name": "Juan Manuel",
        "last_name": "de las Heras Arroyo"
    },
    "details": "After finishing the project, submit github link to NDS for evaluation",
    "priority": 0,
    "starts_on": "2025-02-04T12:00:00Z",
    "ends_on": "2025-02-05T09:00:00Z",
    "created_on": "2025-02-05T03:22:38.278357Z",
    "updated_on": "2025-02-05T03:22:38.278321Z",
    "status": 0
}
```