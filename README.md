

## Kurulum

İndirdikten sonra proje dizini içerisinde :


blog sayfasında bulunan settings.py dosyasından en lat kısımlarda bulunan `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`,`AWS_STORAGE_BUCKET_NAME` ,`AWS_S3_ENDPOINT_URL`, alanları kendi sunucunuza göre doldurunuz 

`virtualenv venv`

 Linux & Mac:
`source venv/bin/activate`

 Windows:
`venv\Scripts\activate`

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuper`

`python manage.py runserver`

