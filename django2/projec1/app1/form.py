from app1.models import user
from django.forms import ModelForm

class userform(ModelForm):
    class Meta:
        model=user
        fields='__all__'
    