from django.forms import ModelForm
from UnusualOmsk.subscription.models import SubscriptionMail

class SubscriptionForm(ModelForm):
    class Meta:
        model = SubscriptionMail
