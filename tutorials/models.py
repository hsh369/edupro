from email.policy import default
from statistics import mode
from django.db import models
from django.urls import reverse
# Create your models here.


class Tutorial(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    rank = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    price = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    #class_id = models.ForeignKey()
    #user_id = models.ForeignKey()

    class Meta:
        ordering = ['-rank']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.pk)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

class Blog(models.Model):
    # image?
    name = models.CharField(max_length=300)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    tutorial_id = models.ForeignKey(
        "tutorials.Tutorial", on_delete=models.CASCADE)
    
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
    # image ?
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    tutorial_id = models.ForeignKey(
        "tutorials.Tutorial", on_delete=models.CASCADE)

    class Meta:
        ordering = ['pk']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.pk)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=500)
    check = models.BooleanField(default=True)
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