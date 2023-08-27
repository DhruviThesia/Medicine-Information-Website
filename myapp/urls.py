from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.insert),
    path('login',views.login),
    path('home',views.home),
    path('about',views.about),
    path('createPost',views.createPost),
    path('service',views.service),
    path('company',views.company),
    path('readMore/<int:id>',views.readMore),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


