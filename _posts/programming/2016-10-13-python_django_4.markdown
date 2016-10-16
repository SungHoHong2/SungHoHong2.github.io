---
published: true
title: Django Customizaiton Tutorial
layout: post
category: programming
permalink: /programming/django_4
---


### Template, Static 경로 통일 

- settings.py

```

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    STATIC_DIR,
]

```

<br>

<hr>


### 로그인 기능 추가 

- urls.py 

``` python


    url(r'^member/', include('member.urls', namespace='member')),

```

<br>

- member/urls.py

``` python

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]

```

<br>

- templates/blog/base.html


``` html

          << if user.is_authenticated >>
          <li>
            <a href="#">
              <span class="glyphicon glyphicon-plus"></span> New post
            </a>
          </li>
          <li>
            <a href="<< url 'member:logout' >>">Logout</a>
          </li>
          << else >>
          <li>
            <a href="<< url 'member:login' >>?next=<< request.path >>">Login</a>
          </li>
          << endif >>
          
          
    << if messages >>
    <div>
      << for message in messages >>
        <div class="alert
          << if message.level == DEFAULT_MESSAGE_LEVELS.ERROR >>alert-danger
          << elif message.level == DEFAULT_MESSAGE_LEVELS.INFO >>alert-info
          << elif message.level == DEFAULT_MESSAGE_LEVELS.SUCCESS >>alert-success
          << elif message.level == DEFAULT_MESSAGE_LEVELS.WARNING >>alert-warning
          << elif message.level == DEFAULT_MESSAGE_LEVELS.DEBUG >>alert-danger
          << endif >>" role="alert">
          <span><< message >></span>
        </div>
      << endfor >>
    </div>
    << endif >>

```

<br>


- member/views.py

```

def login(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return HttpResponse('username 또는 password는 필수항목입니다')
        user = auth_authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            messages.success(request, '로그인에 성공하였습니다')
            return redirect(next)
        else:
            messages.error(request, '로그인에 실패하였습니다')
            return render(request, 'member/login.html', {})
    else:
        return render(request, 'member/login.html', {})


def logout(request):
    auth_logout(request)
    messages.info(request, '로그아웃 되었습니다')
    return redirect('blog:post_list')

```

<br>


<br> 


<hr>


### User 테이블 Customization

- member/models.py

```

from django.db import models
from django.contrib.auth.models import \
    AbstractBaseUser, AbstractUser, \
    BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(
            self,
            email,
            last_name,
            first_name,
            nickname,
            password=None):
        user = self.model(
            email=email,
            last_name=last_name,
            first_name=first_name,
            nickname=nickname
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
            self,
            email,
            last_name,
            first_name,
            nickname,
            password):
        user = self.model(
            email=email,
            last_name=last_name,
            first_name=first_name,
            nickname=nickname
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=24, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('last_name', 'first_name', 'nickname', )

    objects = MyUserManager()

    def get_full_name(self):
        return '%s%s' % (self.last_name, self.first_name)

    def get_short_name(self):
        return self.first_name


```

<br>

- settings.py

```

AUTH_USER_MODEL = 'member.MyUser'

```


<br> 

- blog/models.py


``` python

lass Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

```


<br>


- member/admin.py

``` python

admin.site.register(MyUser)

```


<hr>




<br>

### Login 

- member/forms.py

```python 


class SignupModelForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget= forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label='Password Confirm', widget= forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = MyUser

        fields = [
            'email',
            'last_name',
            'first_name',
            'nickname',
            'password1',
            'password2',
        ]

        widgets = {
            'email' : forms.EmailInput(attrs= {'class' : 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
        }


    def save(self, commit= True):
        user = super(SignupModelForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

```


<br>

- member/views/__init.py 

``` python 

from .login import login
from .logout import logout
from .signup import signup, signup2, signup3

```

<br>

- member/views/signup.py (compartmentalized)

``` python 

def signup3(request):
    context = {}
    if request.method == 'POST':
        form = SignupModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = SignupModelForm()
        context['form'] = form
        return render(request, 'member/signup2.html', context)

```


<br>

- member/views/login.py

``` python

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate as auth_authentication, login as auth_login, logout as auth_logout
from django.contrib import messages
from member.models import MyUser


def login(request):
    next = request.GET.get('next')

    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return HttpResponse("username error")

        MyUser = auth_authentication(email=username, password=password)

        if MyUser is not None:
            auth_login(request, MyUser)
            messages.success(request, "login success")
            return redirect(next)
        else:
            messages.error(request, "login failed")
            return render(request, 'member/login.html', {'error_message' : 'login failed'})

    else:

        return render(request, 'member/login.html', {})


```


<br>


- member/views/loginout.py


``` python

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate as auth_authentication, login as auth_login, logout as auth_logout
from django.contrib import messages


def logout(request):
    auth_logout(request)
    messages.success(request, "login out success")
    return redirect('post_list')

```






