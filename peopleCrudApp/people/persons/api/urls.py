from django.conf.urls import url

from .views import PersonList, PersonDetail

urlpatterns = [
    url(r'^$', PersonList.as_view()),
    url(r'^(?P<pk>[0-9]+)$', PersonDetail.as_view()),
]

