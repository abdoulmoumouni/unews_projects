from django import forms
from blog .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body','category','slug','utilisateur','image','resume']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'What\'s on your mind?'})
        self.fields['title'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'What\'s on your mind?'})
        self.fields['category'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'What\'s on your mind?'})
        self.fields['slug'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'What\'s on your mind?'})
        self.fields['utilisateur'].widget.attrs.update({'class' : 'form-control'})
        self.fields['image'].widget.attrs.update({'class' : 'form-control-file'})
        self.fields['resume'].widget.attrs.update({'class' : 'form-control-file'})

class LoginForm(forms.Form):
    username = forms.CharField(widget =forms.TextInput(attrs={'class':'form-control','placeholder':'Utilisateur'}))
    password = forms.CharField(widget =forms.PasswordInput(attrs={'class':'form-control','placeholder':'mot de pass'}))
    def clean(self):
        cleaned_data = super (LoginForm,self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
