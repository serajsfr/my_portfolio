from django import forms
from .models import Profile, Contact, Project, Skill

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'linkedin', 'github']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'link', 'demo']

    technologies = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),   
        widget=forms.CheckboxSelectMultiple
    )