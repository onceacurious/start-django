from django.forms import ModelForm
from .models import Inquiry


class InquiryRoom(ModelForm):
    class Meta:
        model = Inquiry
        fields = '__all__'
        exclude = ['inquiry_at']
