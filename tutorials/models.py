from enum import unique
from multiprocessing.util import abstract_sockets_supported
from tabnanny import verbose
from django.db import models
from django.urls import reverse
# Create your models here.


class Tutorial(models.Model):
    name = models.CharField("Title", max_length=100)
    description = models.CharField("Description", max_length=300)
    rank = models.DecimalField(
        "Rank", default=0, max_digits=2, decimal_places=1)
    price = models.IntegerField("Price", default=0)
    votes = models.IntegerField("Votes number", default=0)

    # auto filled fields
    created_date = models.DateField("Created date", auto_now_add=True)
    last_modified = models.DateField("Last modified", auto_now=True)

    # Relations with other tables
    type_id = models.ForeignKey("tutorials.TutorialType", verbose_name=(
        "Tutorial Type"), on_delete=models.SET_NULL, blank=True, null=True)
    class_id = models.ForeignKey("classes.Class", verbose_name=(
        "Class"), on_delete=models.SET_NULL, blank=True, null=True)
    user_id = models.ForeignKey("accounts.User",related_name='tutorials', verbose_name=(
        "Creator"), on_delete=models.CASCADE)

    class Meta:
        ordering = ['-rank']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('tutorial-detail-view', args=[str(self.pk)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

    def set_rank(self, rate):
        total = self.rank*self.votes
        self.votes = self.votes+1
        self.rank = (total + rate)/self.votes
        super().save(self)

class Blog(models.Model):
    image = models.ImageField(upload_to='blogs', blank=True, null=True)
    name = models.CharField("Title", max_length=300)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField("Last modified", auto_now=True)
    tutorial_id = models.ForeignKey(
        "tutorials.Tutorial", verbose_name="Tutorial",related_name='blogs', on_delete=models.CASCADE)

    class Meta:
        ordering = ['pk']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.pk)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

class Task(models.Model):
    image = models.ImageField(
        "Image", upload_to='tasks', blank=True, null=True)
    question = models.CharField("Question", max_length=500)

    tutorial_id = models.ForeignKey(
        "tutorials.Tutorial",related_name='tasks', verbose_name="Tutorial", on_delete=models.CASCADE)

    class Meta:
        ordering = ['pk']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.pk)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.question

class TaskAnswer(models.Model):
    answer = models.CharField(max_length=500)
    checking = models.BooleanField(default=True)
    task_id = models.ForeignKey("tutorials.Task", on_delete=models.CASCADE)

    class Meta:
        ordering = ['pk']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.pk)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.answer

class Comment(models.Model):
    comment = models.CharField("Comment", max_length=100)
    publish_date = models.DateField("Published Date", auto_now_add=True)
    user_id = models.ForeignKey(
        "accounts.User", verbose_name="User", on_delete=models.CASCADE)
    tutorial_id = models.ForeignKey(
        "tutorials.Tutorial", verbose_name="Tutorial", on_delete=models.CASCADE)
    rank = models.IntegerField("Rating", blank=True, null=True)

    class Meta:
        unique_together = ['id', 'user_id']
        ordering = ['-publish_date']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.pk)])

    def __str__(self):
        """String for representing the Comment object (in Admin site etc.)."""
        return self.comment

    def save(self, *args, **kwargs):

        # set rank to tutorial
        if self.rank:
            Tutorial.set_rank(self.tutorial_id, self.rank)
        super().save(*args, **kwargs)

class TutorialType(models.Model):
    name = models.CharField(max_length=50)
    tutorials_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.pk)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name
