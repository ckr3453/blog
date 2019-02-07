
from django.contrib import admin
from django.urls import path
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"), #패스컨버터를 사용하여 정수형숫자로 객체들(블로그 글들)을관리, detail 함수로 blog_id를 넘겨줌
    path('blog/new/', blog.views.new, name="new"),
    path('blog/create/', blog.views.create, name="create"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 병렬적으로 추가 (좀더 효율적, 추후에 학습 필요) (urlpatterns += (~~)와 같음)
