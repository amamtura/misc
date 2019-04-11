from django.conf.urls import url

from .views import PersonList, PersonDetail

urlpatterns = [
    url(r'^$', PersonList.as_view(), name='get_post_persons'),
    url(r'^(?P<pk>[0-9]+)$', PersonDetail.as_view(), name='get_update_delete_person'),
]

