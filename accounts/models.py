from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Model for superadmin
class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None): #The prototype of create_user() should accept the username field, plus all required fields as arguments
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using = self._db) # is usually defined as "default" from your database configuration in settings.py.
        return user
    
    def create_superuser(self,first_name,last_name,username,email,password=None):
        user = self.create_user(
                email = self.normalize_email(email),
                username = username,
                password = password,
                first_name = first_name,
                last_name = last_name,
        )
           #permission
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using =self._db)
        return user   
#custom user model
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email   = models.EmailField(max_length=100,unique=True,verbose_name='Email Address')
    phone_number = models.CharField(max_length=50)
    
    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name'] #has no effect in other parts of Django, like creating a user in the admin.
   

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,add_label):
        return True