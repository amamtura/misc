from datetime import datetime
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from persons.models import Person
from persons.api.serializers import PersonSerializer


# initialize the APIClient app
client = Client()


class GetAllPersonsTest(TestCase):
    """ Test module for GET all persons API """

    def setUp(self):
        Person.objects.create(
            email='john.doe@acme.com',
            name='John Doe',
            birthday=datetime.strptime('1979-01-15', '%Y-%m-%d').date(),
            zipcode='90210')
        Person.objects.create(
            email='jane.smith@gmail.com',
            name='Jane Smith',
            birthday=datetime.strptime('2001-12-30', '%Y-%m-%d').date(),
            zipcode='11111-1111')
        Person.objects.create(
            email='bob.jones@yahoo.com',
            name='Robert Jones',
            birthday=datetime.strptime('1950-04-10', '%Y-%m-%d').date(),
            zipcode='77001')

    def test_get_all_persons(self):
        # get API response
        response = client.get(reverse('get_post_persons'))
        # get data from db
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePersonTest(TestCase):
    """ Test module for GET single person API """

    def setUp(self):
        self.john = Person.objects.create(
            email='john.doe@acme.com',
            name='John Doe',
            birthday=datetime.strptime('1979-01-15', '%Y-%m-%d').date(),
            zipcode='90210')
        self.jane = Person.objects.create(
            email='jane.smith@gmail.com',
            name='Jane Smith',
            birthday=datetime.strptime('2001-12-30', '%Y-%m-%d').date(),
            zipcode='11111-1111')
        self.bob = Person.objects.create(
            email='bob.jones@yahoo.com',
            name='Robert Jones',
            birthday=datetime.strptime('1950-04-10', '%Y-%m-%d').date(),
            zipcode='77001')

    def test_get_valid_single_person(self):
        response = client.get(
            reverse('get_update_delete_person', kwargs={'pk': self.jane.pk}))
        person = Person.objects.get(pk=self.jane.pk)
        serializer = PersonSerializer(person)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_person(self):
        response = client.get(
            reverse('get_update_delete_person', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPersonTest(TestCase):
    """ Test module for inserting a new person """

    def setUp(self):
        self.valid_payload = {
            'email': 'john.doe@acme.com',
            'name': 'John Doe',
            'birthday': '1999-01-01',
            'zipcode': '90210'
        }
        self.invalid_payload = {
            'email': 'john.doe',  # bad email
            'name': 'John Doe',
            'birthday': '1999-01-01',
            'zipcode': '90210'
        }

    def test_create_valid_person(self):
        response = client.post(
            reverse('get_post_persons'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_person(self):
        response = client.post(
            reverse('get_post_persons'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSinglePersonTest(TestCase):
    """ Test module for updating an existing person record """

    def setUp(self):
        self.john = Person.objects.create(
            email='john.doe@acme.com',
            name='John Doe',
            birthday=datetime.strptime('1979-01-15', '%Y-%m-%d').date(),
            zipcode='90210')
        self.valid_payload = {
            'email': 'john.doe@acme.com',
            'name': 'John Doe',
            'birthday': '1999-01-01',
            'zipcode': '90210'
        }
        self.invalid_payload = {  
            'email': 'john.doe',  # bad email
            'name': 'John Doe',
            'birthday': '1999-01-01',
            'zipcode': '90210'
        }

    def test_valid_update_person(self):
        response = client.put(
            reverse('get_update_delete_person', kwargs={'pk': self.john.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_person(self):
        response = client.put(
            reverse('get_update_delete_person', kwargs={'pk': self.john.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePersonTest(TestCase):
    """ Test module for deleting an existing person record """

    def setUp(self):
        self.john = Person.objects.create(
            email='john.doe@acme.com',
            name='John Doe',
            birthday=datetime.strptime('1979-01-15', '%Y-%m-%d').date(),
            zipcode='90210')

    def test_valid_delete_person(self):
        response = client.delete(
            reverse('get_update_delete_person', kwargs={'pk': self.john.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_person(self):
        response = client.delete(
            reverse('get_update_delete_person', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

