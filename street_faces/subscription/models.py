from django.db import models


# Create your models here.
class subscription_mail(models.Model):
    email = models.EmailField(max_length=75, verbose_name=u"e-mail")

    def __unicode__(self):
        return unicode(self.email)
