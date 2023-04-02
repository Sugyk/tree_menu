from django import forms
from .models import Folder
from django.core.exceptions import ValidationError


class AdminMenuForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = '__all__'

    def clean_parent(self):
        form_parent = self.cleaned_data['parent']
        print(self.cleaned_data)
        if form_parent == self.instance:
            raise ValidationError('Object can not have himself as a parent!')
        # if  not form_parent and not self.cleaned_data['menu']:
        #     raise ValidationError('You must complete either "root" or "parent"!')
        if form_parent:
            self.cleaned_data['menu'] = form_parent.menu
        return form_parent
