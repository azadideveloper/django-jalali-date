from django import forms
from .models import Test
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime



class TestForm(forms.ModelForm):
    class Meta: 
        model = Test
        fields = ('date',)

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label=('date'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
