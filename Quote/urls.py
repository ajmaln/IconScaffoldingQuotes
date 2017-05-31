from django.conf.urls import url

from Quote.views import QuoteCreta
from .views import Index, QuoteCreate, QuoteView, AddItem, ItemDelete


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)$', QuoteView.as_view(), name='quote'),
    url(r'^create/', QuoteCreta.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/add', AddItem.as_view(), name='add_item'),
    url(r'^(?P<pk>[0-9]+)/delete/(?P<id>[0-9]+)', ItemDelete.as_view(), name='delete_item')
]