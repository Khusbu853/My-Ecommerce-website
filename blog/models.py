from django.db import models

# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=100)
    head1 = models.CharField(max_length=500,default="")
    content_head1 = models.CharField(max_length=1000, default="")
    head2 = models.CharField(max_length=500,default="")
    content_head2 = models.CharField(max_length=1000, default="")
    head3 = models.CharField(max_length=500,default="")
    content_head3 = models.CharField(max_length=1000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.title