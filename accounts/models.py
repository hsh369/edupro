from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, email, bithdate, username, password = None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            bithdate = bithdate,
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, bithdate, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password = password,
            bithdate = bithdate,
            username = username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=10, unique =True)
    image = models.ImageField(upload_to='blogs',blank=True, null=True)
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+9981234567'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    bio = models.CharField(max_length = 400, blank=True, null= True)
    bithdate = models.DateField()

    rank = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    wallet = models.IntegerField(default=10)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['bithdate','username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

# class Connection(models.Model):
#     user_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
#     following_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ['user_id', 'following_id']

    
