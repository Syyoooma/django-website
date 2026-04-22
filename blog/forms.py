from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(
        label='Тема повідомлення',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label='Ваша пошта',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    message = forms.CharField(
        label='Текст повідомлення',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )