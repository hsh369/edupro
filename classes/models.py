from django.db import models


# Class model to create private classes 
class Class(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    creator_id = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, blank=True, null=True)
    
    class Meta:
        ordering = ["-created_date"]
        
    def __str__(self):
        return self.name
    
# members of private classes 
class Member(models.Model):
    class_id = models.ForeignKey("classes.Class", on_delete=models.CASCADE)
    user_id = models.ForeignKey("accounts.User",  on_delete=models.CASCADE)
    joined_date = models.DateField( auto_now_add = True)

    class Meta:
        unique_together = ['class_id', 'user_id']
        
    
