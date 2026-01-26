from ckeditor.widgets import CKEditorWidget
from django import forms
from register.models.publics import Public


# PublicForm
# ----------------------------------------------------------------------------------------------------------------------
class PublicForm(forms.ModelForm):
    class Meta:
        model = Public
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(config_name='default'),
        }
