from django.conf.urls import url

from .views import index, login_page, register_page


urlpatterns = [
    url(r'^login$', login_page),
    url(r'^$', index),
    url(r'^register', register_page),
]
