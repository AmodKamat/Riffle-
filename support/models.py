from django.db import models
from customusermodel.models import User
class Support(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,verbose_name="User ID")
    topic = models.CharField(max_length=100, verbose_name="Topic")
    description = models.CharField(max_length=350, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    is_resolved = models.BooleanField(default=False, verbose_name="Is Resolved")

    def __str__(self):
        return f"{self.user_id} - {self.topic}"

    class Meta:
        verbose_name = "Support"