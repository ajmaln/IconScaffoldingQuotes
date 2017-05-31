from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls.base import reverse_lazy
from .settings import LOGIN_URL
from django.contrib.auth.decorators import user_passes_test

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), reverse_lazy('index'), redirect_field_name=None)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_forbidden(auth_views.login), {'template_name': 'Quote/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': LOGIN_URL}, name='logout'),
    url(r'^quotes/', include('Quote.urls')),
]
