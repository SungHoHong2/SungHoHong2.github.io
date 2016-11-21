---
published: true
title: Deploy Django project with Elastic Beanstalk 
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
    


# add auto commands and route for static directory 
    - update django.config
        aws:elasticbeanstalk:container:python:staticfiles:
        "/static/": "static_root/"    
    
        container_commands:
          01_collectstatic:
            command: "source /opt/python/run/venv/bin/activate && python django_app/manage.py collectstatic --noinput"
          02_migrate:
            command: "source /opt/python/run/venv/bin/activate && python django_app/manage.py migrate --noinput"
         
         
# connect the security group between RDS and Elastic            



# add default admin in settings_deploy.json
   - need additional command in order to create the superuser 
   
        "defaultSuperuser": {
            "username": "<username>",
            "password": "<password>"
        }


# connect S3 for static files
    $ cat ~/.aws/config 
        
        aws_access_key_id = [key]
        aws_secret_access_key = [key]
    
        [default]
        region = ap-northeast-2
        output = json
        
    $ pip install awscli boto django-storages
    $ python 
    $ import boto
    $ conn = boto.connect_s3('accesskey', 'secretkey')
    $ conn.create_bucket('사용할 bucket이름')

# check the ARN in IAM users 
# go to S3 in AWS 

# add Add bucket policy 
    {
        "Statement": [
            {
              "Sid":"PublicReadForGetBucketObjects",
              "Effect":"Allow",
              "Principal": {
                    "AWS": "*"
                 },
              "Action":["s3:GetObject"],
              "Resource":["arn:aws:s3:::BUCKET-NAME/*"
              ]
            },
            {
                "Action": "s3:*",
                "Effect": "Allow",
                "Resource": [
                    "arn:aws:s3:::BUCKET-NAME",
                    "arn:aws:s3:::BUCKET-NAME/*"
                ],
                "Principal": {
                    "AWS": [
                        "USER-ARN"
                    ]
                }
            }
        ]
    }



# create eb-mysite-project/django_app/eb_mysite/custom_storages.py

        from django.conf import settings
        from django.core.files.storage import get_storage_class
        from storages.backends.s3boto import S3BotoStorage
        
        
        class StaticStorage(S3BotoStorage):
            location = settings.STATICFILES_LOCATION
        
        
        class MediaStorage(S3BotoStorage):
            location = settings.MEDIAFILES_LOCATION

# add apps in settings 

    INSTALLED_APPS = [
        ...
        'storages',
    ]


# add in settings_deploy.json 

    {
      "aws": {
        "AWS_STORAGE_BUCKET_NAME": "",
        "AWS_ACCESS_KEY_ID": "",
        "AWS_SECRET_ACCESS_KEY": ""
      }
    }
    
    
# add settings.py 
    
    STATIC_S3 = True

    if not DEBUG or STATIC_S3:
        AWS_HEADERS = {
            'Expires': 'Thu, 31 Dec 2199 20:00:00 GMT',
            'Cache-Control': 'max-age=94608000',
        }
        AWS_STORAGE_BUCKET_NAME = config['aws']['AWS_STORAGE_BUCKET_NAME']
        AWS_ACCESS_KEY_ID = config['aws']['AWS_ACCESS_KEY_ID']
        AWS_SECRET_ACCESS_KEY = config['aws']['AWS_SECRET_ACCESS_KEY']
        AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    
        STATICFILES_LOCATION = 'static'
        STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
        STATICFILES_STORAGE = 'mysite.custom_storages.StaticStorage'
    
        MEDIAFILES_LOCATION = 'media'
        MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
        DEFAULT_FILE_STORAGE = 'mysite.custom_storages.MediaStorage'
    else:
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        STATIC_URL = '/static/'
        MEDIA_URL = '/media/'
        

```



### when git ignore does not work 

```

    git rm -r --cached [wanted hidden directory]
    git add .
    git commit -m "fixed untracked files"

```