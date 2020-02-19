## Project for work with database by Django-orm.

Project for get from database passcard information, storage information and 
active passcard information by filter request by Django-orm, and show
it in web browser.

## Getting Started

- Clone repository from github.
- Create and activate your virtual environment.
- Install required modules from ```requirements.txt```.
- Set up project/settings.py file, all parameters hide in ```.env``` file.
- Create ```.env``` (variable environment)
 file and fill in the file with your data.
    ```python
    DB_PASSWORD='database password'
    DB_USER='database user'
    DB_NAME='database name'
    DB_PORT='port'
    DB_HOST='database host'
    DB_ENGINE='database engine'
    SECRET_KEY='secret key to generate hashes'
    DEBUG=false
  ```

## Running
Running from command line
```
python manage.py sunserver 0.0.0.0:8000
```
information will be visible in web browser on localhost [http://127.0.0.1:8000/] 

## License

You may copy, distribute and modify the software.