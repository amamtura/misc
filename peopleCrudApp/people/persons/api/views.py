from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from persons.models import Person
from .serializers import PersonSerializer


class PersonList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        order_by = self.request.query_params.get('order_by', 'id')
        return Person.objects.all().order_by(order_by)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PersonDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

