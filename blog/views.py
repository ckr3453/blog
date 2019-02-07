from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects # 쿼리셋 # 메소드
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog' : blog_detail})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

# render 함수와 redirect 함수의 차이점은?
# 인자에 따라서, 어떤상황에 사용할지에 따라서 차이가있음.
# 함수안에서 처리된 변수를 html로 넘겨 처리하고싶을때 사용(render)
# 프로젝트 외에 url에 연결할수 있음.(redirect)

def create(request): # 입력받은 내용을 DB에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now() #현재시간 불러오기
    blog.save() # 지금까지 작성된 객체를 DB에 저장하라.
    return redirect('/blog/'+str(blog.id)) # 위에 과정을 처리하고 인자(url)로 넘기세요(이동하세요).
    # blog.id 는 정수형이기 때문에 url로 바꿔주기위해서는 str로 변환