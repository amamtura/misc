from datetime import datetime
from django.test import TestCase
from persons.models import Person


class PersonTest(TestCase):
    """ Test module for Person model """

    def setUp(self):
        Person.objects.create(
            email='john.doe@acme.com',
            name='John Doe',
            birthday=datetime.strptime('1979-01-15', '%Y-%m-%d').date(),
            zipcode='90210')

    def test_person(self):
        person_john = Person.objects.get(email='john.doe@acme.com')
        self.assertIsNotNone(person_john)

