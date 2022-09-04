from django.db import models
import datetime as dt

# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



    def __str__(self):
        return f"Name: {self.name}, Total Votes: {self.votes}"

    def __repr__(self):
        return f"ID: {self.id}\nName: {self.name}, Total Votes: {self.votes}"


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField("date published")
    
    def is_recently_published(self):
        return self.publication_date + dt.timedelta(days=1) > dt.datetime.now()
    
    def __str__(self):
        return f"{self.question_text} \nPublishedAt: {self.publication_date}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    