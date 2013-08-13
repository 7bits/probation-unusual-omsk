from django.forms import ModelForm
from UnusualOmsk.subscription.models import subscription_mail

class subscription_form(ModelForm):
    class Meta:
        model = subscription_mail
