---
published: true
title: Elastic Deploy 
layout: post
category: programming
permalink: /programming/django_server_2
---


### The location of credentials of Users 
- ~/.aws/config  ( default settings )  
- ~/.aws/credentials 


### The locaiton of the keys 
- cd ~/.ssh


### Creating RDS 
- Created RDS are positioned in the security groups 
- Security group of RDS should open ports with the group ID of elastic Web service


<br> 

```

# creating a project with git initialized 
    $ git init 
    $ pyenv local instagram_second 
    $ pip install --upgrade pip
    $ pip install django
    - create django application 
    - switch the root folder name into django_app 
    
   
# create user in AWS 
    - add permissions 
    - AdministratorAccess
    - AWSElasticBeanstalkWebTier
    - AWSElasticBeanstalkWorkerTier
    - AWSElasticBeanstalkMulticontainerDocker
    - and other two 
    - save the credential files in secure area 

# install awsebcli 
    - install all the necessary apis for using aws 
    $ pip install awsebcli
    - install key pair in ~/.ssh 
    
    
# deploy the django-app to the server 
    - commit the updates in the git 
    $ pip freeze > requirements.txt
    $ eb create
    $ eb deploy 
    - check the process of the deployemnt in the aws website
 

# connect hte WSGI path 
    $ mkdir .ebextensions
    $ vi .ebextensions/django.config
    
    option_settings:
      aws:elasticbeanstalk:container:python:
        WSGIPath: django_app/eb_again/wsgi.py
        NumProcesses: 3
        NumThreads: 20
      aws:elasticbeanstalk:application:environment:
        DJANGO_SETTINGS_MODULE: eb_again.settings
        PYTHONPATH: /opt/python/current/app/django_app:$PYTHONPATH
        LANG: "ko_KR.utf8"
        LC_ALL: "ko_KR.UTF-8"
        LC_LANG: "ko_KR.UTF-8"

    - add the address to the allowed host 
    $ eb deloy 
    
 
 # connecting RDS 
     $ mkdir .django-conf
     $ cd .django-conf
     $ vi settings_deploy.json
        
        {
          "databases": {
            "default": {
              "ENGINE": "django.db.backends.postgresql_psycopg2",
              "NAME": "<db name>",
              "USER": "<db user>",
              "PASSWORD": "<db password>",
              "HOST": "<db endpoint>",
              "PORT": "5432"
            }
          }
        } 
            
     
     $ vi .gitignore
     
        .aws-conf/
        .django-conf/    
         

```


<br> 

- update settings.py 


``` python 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
CONF_DIR = os.path.join(ROOT_DIR, '.django-conf')
STATIC_ROOT = os.path.join(ROOT_DIR, 'static_root')


if DEBUG:
    config = json.loads(open(os.path.join(CONF_DIR, 'settings_debug.json')).read())
else:
    config = json.loads(open(os.path.join(CONF_DIR, 'settings_deploy.json')).read())


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = config['databases']

```

```

# installing psycopg2 for connecting Postgre
    $ pip install psycopg2
    $ vi .ebignore
        !.django-conf/
    


# create static-directory 

    - update django.config
        aws:elasticbeanstalk:container:python:staticfiles:
        "/static/": "static_root/"    
    
        container_commands:
          01_collectstatic:
            command: "source /opt/python/run/venv/bin/activate && python django_app/manage.py collectstatic --noinput"
          02_migrate:
            command: "source /opt/python/run/venv/bin/activate && python django_app/manage.py migrate --noinput"
         
         
# connect the security group between RDS and Elastic            


    


```




sudo -s
source /opt/python/run/venv/bin/activate
source /opt/python/current/env
cd /opt/python/current/app
then run your command.

./manage.py migrate


