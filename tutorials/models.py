from multiprocessing.util import abstract_sockets_supported
from django.db import models
from django.urls import reverse
# Create your models here.


class Tutorial(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    rank = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    price = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    #auto filled fields
    created_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    
    #Relations with other tables
    type_id = models.ForeignKey("tutorials.TutorialType", verbose_name=("Tutorial Type"), on_delete=models.SET_NULL, blank= True, null=True)
    class_id = models.ForeignKey("classes.Class", verbose_name=("Class"), on_delete=models.SET_NULL, blank=True, null=True)
    user_id = models.ForeignKey("accounts.User", verbose_name=("Creator"), on_delete=models.CASCADE)
    
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
    image = models.ImageField(upload_to='blogs',blank=True, null=True)
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
    image = models.ImageField(upload_to='tasks',blank=True, null=True)
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
        abstract = True
        ordering = ['pk']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.pk)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.answer

class Comment(models.Model):
    comment = models.CharField( max_length=100)
    publish_date = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, blank =True, null= True)
    tutorial_id = models.ForeignKey("tutorials.Tutorial", on_delete=models.CASCADE)

class TutorialType(models.Model):
    name = models.CharField(max_length=50)
    tutorials_count = models.IntegerField(default=0)
