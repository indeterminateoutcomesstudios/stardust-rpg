from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=25)
    roll20_campaign_id = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{}: {}'.format(self.name, self.roll20_campaign_id)
