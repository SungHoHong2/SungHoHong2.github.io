# login_required    유저 정보가 포함되어 있는지
# is_admin          유저가 관리자인지



# user_class : username, is_admin
# Request      user instance ( user 0 => login  user X => invalid login)
#
# Response     사용자에게 줄 메시지


class Request:
    def __init__(self, url, user=None):
        self.url = url
        self.user = user

class Response:
    def __init__(self, body):
        self.body = body
    pass

    def __repr__(self):
        return "Response :: {body}".format(body=self.body)

class User:
    def __init__(self, name , is_admin = False):
        self.name = name
        self.is_admin = is_admin


def home(request):
    pass


def mypage(request):
    if request.user:
        response = Response("정상적으로 접속")
    else :
        response = Response("로그인 필요")
    return response




user1 = User("sunghohong")
user2 = User("sunghohong2", is_admin= True)


request = Request("/mypage", user1)
request2 = Request("/mpage")


#print(mypage(request))
#print(mypage(request2))


#decoration
def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user:
            #print(request.user.is_admin)
            response = func(request, *args, **kwargs)
        else:
            response = Response("로그인이 필요합니다.")
        return response
    return wrapper


@login_required
def mypage(request):                            # decorator :: login_required !!!
    return Response("성공적으로 MyPage 에 접속했습니다.")


request = Request("/mypage/")
print(mypage(request))

request = Request("/mypage/", user1)
print(mypage(request))


def is_admin(func):
    def wrapper(request,*args, **kargs):
        if request.user and request.user.is_admin:
            response = func(request, *args, **kargs)
        else:
            response = Response("관리자 권한이 필요합니다.")
        return response
    return wrapper


@is_admin
@login_required
def admin(request):
    return Response("admin에 성공적으로 접속했습니다.")


request = Request("/admin/", user2)
print(admin(request))

# 현재는 로그인 권한과 관리자 권한 두개 다 작동한다.
request = Request("/admin/")
print(admin(request))


#home(request) #response의 객체 (body => home)



