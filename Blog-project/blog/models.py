from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class MenuList(models.Model):
    module_name = models.CharField(max_length=100, db_index=True)
    menu_name = models.CharField(max_length=100, unique=True, db_index=True)
    menu_url = models.CharField(max_length=200, unique=True)
    menu_icon = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.IntegerField(default=0)
    is_main_menu = models.BooleanField(default=False)
    is_sub_menu = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='menu_created_by')
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'menu_list'
       

    def __str__(self):
        return self.menu_name
    
    
    
    
    
class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_permission_user')
    menu = models.ForeignKey(MenuList, on_delete=models.CASCADE, related_name='user_permission_menu')
    can_view = models.BooleanField(default=False)
    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='permission_created_by')
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    class Meta:
        db_table = 'user_permission'

    def __str__(self):
        return f"{self.user.username} - {self.menu.menu_name}"
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'post'
       
    def __str__(self):
        return self.title