from django import forms
class signupf(forms.Form):
    user=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'User Name',
        'id':'inputName'
    }))
    emailid=forms.EmailField(max_length=100,
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Email address',
        'id':'inputEmail'
    }))
    passw=forms.CharField(max_length=50,
    widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password',
        'id':'inputPassword'
    }))

class loginformf(forms.Form):
    useremail=forms.EmailField(max_length=100,
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Email address',
        'id':'inputEmai'
    }))
    userpass=forms.CharField(max_length=50,
    widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password',
        'id':'inputPasswor'
    }))

class railwayform(forms.Form):
    trackl=forms.CharField(max_length=4,
    widget=forms.TextInput(attrs={
        'id':'exampleInputEmail1', 
        'placeholder':'Enter Year'
    }))

class tourismform(forms.Form):
    yeartf=forms.CharField(max_length=4,
    widget=forms.TextInput(attrs={
        'placeholder':'Enter Year',
        'id':'exampleInputEmail1'
    }))

class educationform(forms.Form):
    yearef=forms.CharField(max_length=4,
    widget=forms.TextInput(attrs={
        'placeholder':'Enter Year',
        'id':'exampleInputEmail1'
    }))

class fertilizerform(forms.Form):
    yearff=forms.CharField(max_length=4,
    widget=forms.TextInput(attrs={
        'placeholder':'Enter Year',
        'id':'exampleInputEmail1'
    }))

    
