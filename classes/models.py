from django.db import models


# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    creator_id = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True)


class Member(models.Model):
    class_id = models.ForeignKey("Classes.Class", on_delete=models.CASCADE)
    user_id = models.ForeignKey("accounts.User",  on_delete=models.CASCADE)
    joined_date = models.DateField( auto_now_add=True)
