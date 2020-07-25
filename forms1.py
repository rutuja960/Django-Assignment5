from django import forms

class MyForm(forms.Form):
    username=forms.CharField(label="username",max_length=100)
    password=forms.CharField(label="password",widget=forms.PasswordInput)
    email=forms.CharField(label="email",max_length=100)
    phone=forms.IntegerField(label="phone")