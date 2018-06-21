from django import forms

from .models import chart_row

class chart_row_add(forms.ModelForm):

    class Meta:
        model = chart_row
        fields = ('func','period', 'dt',)
