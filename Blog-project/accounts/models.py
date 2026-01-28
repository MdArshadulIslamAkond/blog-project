from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    phone = models.CharField(max_length=25)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    address = models.TextField()
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        # return self.user
        return self.user.first_name + ' ' + self.user.last_name 