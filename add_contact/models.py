from django.db import models

class AddContact(models.Model):
    name =models.CharField(max_length=100)
    phone1=models.CharField(max_length=50,blank=False)
    phone2=models.CharField(max_length=50,blank= True)
    email=models.EmailField(max_length=100)
    picture=models.ImageField(upload_to='pic',blank=True)
    address=models.CharField(max_length=150,blank=True)
    business_key=models.CharField(max_length=50)
    textfield=models.TextField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

