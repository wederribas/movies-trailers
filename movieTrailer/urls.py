from django.conf.urls import url
from django.contrib import admin

from movies.views import HomeView, AboutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^about/', AboutView.as_view()),
]
