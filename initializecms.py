from django.conf import settings
import sys
import os
username = sys.argv[1]
password = sys.argv[2]
email = sys.argv[3]
port = sys.argv[4]
with open("/usr/src/app/vlog/vlog/settings.py", "a") as a_file:
  a_file.write("\n")
  a_file.write("ALLOWED_HOSTS = ['*']")
with open("/usr/src/app/vlog/vlog/settings.py", "a") as a_file:
  a_file.write("\n")
  a_file.write(f"DATABASES = {{ \
    'default': {{ \
        'ENGINE': 'django.db.backends.postgresql_psycopg2', \
        'NAME': 'postgres', \
        'USER': 'postgres', \
        'PASSWORD': '1nf0M@t1cs', \
        'HOST': '{username}-db', \
        'PORT': '5432', \
    }} \
   }}" )   
  a_file.write("\n")
print(username)
print(port)
os.system("python manage.py migrate")
script= f'python manage.py shell < adduser.py'
os.system(script)
os.system(f"python manage.py runserver {port}")