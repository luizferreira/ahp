from django.utils import timezone
from django.test import TestCase

from decision.models import Decision
from decision.tests import DECISION_TEST_DATA
from vote.models import Vote


class VoteTests(TestCase):

    def setUp(self):
        self.decision = Decision(**DECISION_TEST_DATA)
        self.vote = Vote(
            finished=False,
            decision=self.decision,
        )

    def test_str(self):
        assert self.vote.__str__() == 'Vote #%s' % self.vote.id

    def test_creation(self):
        assert type(self.vote) == Vote
