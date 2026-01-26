from ckeditor.widgets import CKEditorWidget
from django import forms
from register.models.content import TextContent, StaffContent


# Content
# ----------------------------------------------------------------------------------------------------------------------
# TextContentForm
class TextContentForm(forms.ModelForm):
    class Meta:
        model = TextContent
        fields = '__all__'
        widgets = {
            'body': CKEditorWidget(config_name='default'),
        }


# StaffContentForm
class StaffContentForm(forms.ModelForm):
    class Meta:
        model = StaffContent
        fields = '__all__'
        widgets = {
            'bio': CKEditorWidget(config_name='default'),
        }


# PopupContentForm
class PopupContentForm(forms.ModelForm):
    class Meta:
        model = StaffContent
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(config_name='default'),
        }
