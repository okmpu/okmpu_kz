from ckeditor.widgets import CKEditorWidget
from django import forms
from register.models.university import Faculty, Department, Division, Project, Success, Document, Personal


# FacultyForm
# ----------------------------------------------------------------------------------------------------------------------
class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'
        widgets = {
            'about': CKEditorWidget(config_name='default'),
        }


# DepartmentForm
# ----------------------------------------------------------------------------------------------------------------------
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'about': CKEditorWidget(config_name='default'),
        }


# DivisionForm
# ----------------------------------------------------------------------------------------------------------------------
class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = '__all__'
        widgets = {
            'about': CKEditorWidget(config_name='default'),
        }


# PersonalForm
# ----------------------------------------------------------------------------------------------------------------------
class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'
        widgets = {
            'about': CKEditorWidget(config_name='default'),
        }


# ProjectForm
# ----------------------------------------------------------------------------------------------------------------------
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(config_name='default'),
        }


# SuccessForm
# ----------------------------------------------------------------------------------------------------------------------
class SuccessForm(forms.ModelForm):
    class Meta:
        model = Success
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(config_name='default'),
        }
