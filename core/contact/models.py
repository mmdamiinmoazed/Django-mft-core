from django.db import models

# Create your models here.
class ContactModel(models.Model) : 
    fullname = models.CharField(max_length=50 ,  ) 

                                                                              
    email = models.EmailField(max_length=50 ,  )
    phone = models.CharField(max_length=12 ,)
    subject = models.CharField(choices=[("register" , "register-problem" ) , ("login" , "login-problem") , ("complain" , "complain")] , max_length=10)
    message = models.CharField(max_length=10000  ,  )
    def __str__(self):
        return f"{ self.fullname } - {self.subject}"