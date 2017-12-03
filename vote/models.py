from django.db import models

from decision.models import Decision


class Vote(models.Model):

    decision = models.ForeignKey(Decision, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return 'Vote #%s' % str(self.id)  # pragma: no cover
