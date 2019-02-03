
from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"), #패스컨버터를 사용하여 정수형숫자로 객체들(블로그 글들)을관리, detail 함수로 blog_id를 넘겨줌
    path('blog/new/', blog.views.new, name="new"),
    path('blog/create/', blog.views.create, name="create"),
]
