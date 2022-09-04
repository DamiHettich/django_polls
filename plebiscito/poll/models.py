from django.db import models
import datetime as dt
from django.utils import timezone

# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    publication_date = models.DateTimeField(default=timezone.now())

    def is_recently_published(self):
        return self.publication_date + dt.timedelta(days=1) > timezone.now()

    def __str__(self):
        return f"Name: {self.name}, Total Votes: {self.votes}"

    def __repr__(self):
        return f"ID: {self.id} Name: {self.name}, Total Votes: {self.votes}"


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)


    def __str__(self):
        return f"Q: {self.question_text}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"Text: {self.choice_text}, Votes: {self.votes}"
