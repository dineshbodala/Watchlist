from django.db import models
import datetime
class Crypto(models.Model):  
    crypto_name = models.CharField(max_length=100) 
    added_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return '%s'%(self.added_time.replace(second=0, microsecond=0))
