from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module, Answer


ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      fields=['title', 'description'],
                                      extra=1,
                                      can_delete=True)

class AnswerForm(forms.ModelForm):
    """Форма для отправки ответа учеником"""
    class Meta:
        model = Answer
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control'})
        }

class GradeForm(forms.ModelForm):
    """Форма для выставления оценки учителем"""
    class Meta:
        model = Answer
        fields = ['grade']
        widgets = {
            'grade': forms.RadioSelect(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')])
        }