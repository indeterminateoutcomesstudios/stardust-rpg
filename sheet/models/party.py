from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=25)
    roll20_campaign_id = models.PositiveIntegerField(default=0)

    @property
    def roll20_url(self) -> str:
        return f'https://app.roll20.net/campaigns/details/{self.roll20_campaign_id}'

    def __str__(self):
        return f'{self.name}: {self.roll20_campaign_id}'
