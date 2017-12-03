from django.db import models


class Decision(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    status = models.IntegerField(default=0)
    encoded_url = models.CharField(max_length=50)
    participants_qty = models.IntegerField()
    creation_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Decision #%s' % str(self.id)  # pragma: no cover
