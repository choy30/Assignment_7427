from django import forms

from blog.models import Dog, Activity, Breed

breedChoices = Breed.objects.all().values_list('name', 'name')

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('name', 'weight', 'dob', 'image','description', 'owner', 'breed')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'weight': forms.NumberInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'owner': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'input', 'type':'hidden'}),
            'breed': forms.Select(choices=breedChoices, attrs={'class': 'form-control'}),
        }
class UpdateDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('weight', 'image', 'description', 'breed')
        widgets = {
            'weight': forms.NumberInput(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'breed': forms.Select(choices=breedChoices, attrs={'class': 'form-control'}),
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'date', 'description', 'location', 'owner')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'location': forms.Textarea(attrs={'class':'form-control'}),
            'owner': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'input', 'type':'hidden'}),
        }
class UpdateActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('date', 'description', 'location')
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'location': forms.Textarea(attrs={'class':'form-control'}),
        }