from django.utils import timezone
from django.test import TestCase
# from test_plus.test import TestCase as PlusTestCase

from decision.models import Decision


DECISION_TEST_DATA = {
    'title': 'Test Decision',
    'description': 'Test Description',
    'participants_qty': 10,
    'creation_date': timezone.now(),
}


class DecisionTests(TestCase):

    def setUp(self):
        self.decision = Decision(**DECISION_TEST_DATA)

    def test_creation(self):
        assert type(self.decision) == Decision
