from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    subject_name = models.CharField(max_length=250)

    def __str__(self):
        return self.subject_name

    def save_subject(self):
        self.save()


class FlashCard(models.Model):
    title = models.CharField(max_length=250)
    notes = models.CharField(max_length=2500)
    owner = models.ForeignKey(User)
    subject = models.ForeignKey(Subject)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_card(self):
        self.save()

    def delete_card(self):
        self.delete()
