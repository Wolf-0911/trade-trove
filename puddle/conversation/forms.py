from django import forms

from .models import ConversationMessage

CLASS_STYLE = 'w-full py-4 px-6 rounded-xl border'

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widget = {
            'content': forms.Textarea(attrs={
                'class': CLASS_STYLE
            })
        }