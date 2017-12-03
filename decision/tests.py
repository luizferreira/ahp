from django.utils import timezone
from django.test import TestCase
# from test_plus.test import TestCase as PlusTestCase

from decision.models import Decision


class DecisionTests(TestCase):

    def test_str(self):
        decision = Decision(
            title='Test Decision',
            description='Test Description',
            participants_qty=10,
            creation_date=timezone.now(),
        )
        decision_str = 'Test Decision (%s)' % \
            decision.creation_date.strftime('%d/%m/%Y %H:%M')
        assert decision.__str__() == decision_str

    def test_creation(self):
        decision = Decision(
            title='Test Decision',
            description='Test Description',
            participants_qty=10,
            creation_date=timezone.now(),
        )
        assert type(decision) == Decision
