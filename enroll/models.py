from django.db import models

class Image(models.Model):
   photo=models.ImageField(upload_to="myimage") #yanha store hoga
   date=models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.date
