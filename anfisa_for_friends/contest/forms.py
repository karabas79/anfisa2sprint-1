from django import forms

from .models import Contest


# Для использования формы с моделями меняем класс на forms.ModelForm.
class ContestForm(forms.ModelForm):
    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Contest
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        widgets = {
            'description': forms.Textarea({'cols': '22', 'rows': '5'}),
            'comment': forms.Textarea({'cols': '22', 'rows': '5'})
        }
