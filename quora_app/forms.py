from django import forms
from .models import Questions, Answers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class QuestionsForm(forms.ModelForm):
    '''
        while create and update Question this form is managed.
    '''
    class Meta:
        model = Questions
        fields = ('title', 'content', 'visable', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept':'image/*'}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Check the file extension
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
            print(image.name.split('.')[-1].lower())
            extension = image.name.split('.')[-1].lower()
            if extension not in valid_extensions:
                raise ValidationError(_('Invalid file format. Only JPG, JPEG, PNG, and GIF images are allowed.'))
        return image

