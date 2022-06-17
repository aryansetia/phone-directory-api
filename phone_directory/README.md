### Prerequisites
To run this app, first install all the dependencies and packages.
```python3
pip install requirements.txt
```

### Run the app
As all the required packages are install now, you can run the app by using the below command
```python3
python manage.py runserver
```

### Available endpoints and thier format
- http://127.0.0.1:8000/api/register/
```json
{
    "name":"aryan",
    "password":"dhjweuaudasbdnsa",
    "email":"xyz@gmail.com",
    "contact_number":"12345678910"
}
```
- http://127.0.0.1:8000/api/login/
```json
{
    "username":"aryan",
    "password":"dhjweuaudasbdnsa",
}
```
- http://127.0.0.1:8000/api/spams/
```json
{
    "contact_number":"12345678910"
}
```

- http://127.0.0.1:8000/api/contacts/
```json
{
    "name":"john doe",
    "contact_number":"000011112222",
    "email":"abc@gmail.com",
}

```

- http://127.0.0.1:8000/api/search-by-name/
```json
{
    "name":"john doe"
}

```

To view all contacts:
- http://127.0.0.1:8000/api/contacts/ (GET METHOD)