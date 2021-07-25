from django.conf import settings
import sys
import os
username = "admin"
password = "admin"
email = "admin@admin.com"
from django.contrib.auth import get_user_model 
User = get_user_model() 
if(not User.objects.filter(username=username).exists()):
  User.objects.create_superuser(username,email,password).save()