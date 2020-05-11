from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice = models.ForeignKey(Choice, models.CASCADE, related_name='votes')
    poll = models.ForeignKey(Poll, models.CASCADE)
    voted_by = models.ForeignKey(User, models.CASCADE)

    class Meta:
        unique_together = ('poll', 'voted_by')