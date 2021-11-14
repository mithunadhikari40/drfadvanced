# drfadvanced
##### Django rest framework advanced concepts with poetry, virtualenv and swagger, followed from https://www.youtube.com/watch?v=83KYtHsUvLY&ab_channel=FaradayAcademy
##### Instruction are available on https://github.com/faraday-academy/django-setup-wiki and https://github.com/mithunadhikari40/django-setup-wiki"

##### django installation with virtualenv
`mkvirtualenv drfadvanced --python=/usr/bin/python3.9`

`workon drfadvanced`

`  pip install django ( It will take some time) `

`python -m django --version`

`django-admin startproject drfadvanced`

` You need to edit the file /settings.py and change the allowed hosts line ALLOWED_HOSTS = [ '*' ] `

`python manage.py makemigrations`

`python manage.py migrate`

` python manage.py runserver`

`Or the instructions can be found at https://www.dj4e.com/assn/dj4e_install.md`


##### psql setup guide

`https://www.postgresqltutorial.com/install-postgresql-linux/`




