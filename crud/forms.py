from django import forms
from .models import Computer ,UserProfileInfo
from django.contrib.auth.models import User

customerCodeChoices = (
    ('igu', 'US'), ('igl', 'LA'), ('chs', 'CA'), ('igp', 'AP'), ('igj', 'JP'), ('EMEA', 'EMEA'))



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('position' ,'email')
         
class ComputerForm(forms.Form):
    resourceId = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'resourceId',
            'class': 'form-control',
            'placeholder': 'Enter device name'
        }
    ))

    subAccount = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'subAccount',
            'class': 'form-control',
            'placeholder': 'Enter queue name'
        }
    ))

    value = forms.ChoiceField(widget=forms.Select(
        attrs={
            'id': 'value',
            'class': 'form-control'
        }
    ), choices=(('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze')))

    customerCode = forms.ChoiceField(widget=forms.Select(
        attrs={
            'id': 'customerCode',
            'class': 'form-control'
        }
    ), choices=customerCodeChoices)


class AliasForm(forms.Form):
    computers = Computer.objects.only('resourceId')

    alias = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'alias',
            'class': 'form-control',
            'placeholder': 'Enter alias for the resource'
        }
    ))

    resourceId = forms.ModelChoiceField(widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ), queryset=computers)


class FilterForm(forms.Form):
    #computers = Computer.objects.only('subAccount')

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        #self.fields['subAccount'].choices = [(computer.subAccount, computer.subAccount) for computer in
                                            # Computer.objects.all()]
    '''                                         
    resourceId = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'resourceId',
            'class': 'form-control',
            'placeholder': 'Enter resource ID'
        }
    ))
    '''
    
    subAccount = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'Queue name',
            'class': 'form-control',
            'placeholder': 'Enter Queue name'
        }
    ))
    
    customerCode = forms.ChoiceField(widget=forms.Select(
        attrs={
            'id': 'customerCode',
            'class': 'form-control'
        }
    ), choices=customerCodeChoices)

    value = forms.ChoiceField(widget=forms.Select(
        attrs={
            'id': 'value',
            'class': 'form-control'
        }
    ), choices=(('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze')))
    
    filterName = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'filterName',
            'class': 'form-control',
            'placeholder': 'Enter filter name'
        }
    ))

    filterDesc = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'filterDesc',
            'class': 'form-control',
            'placeholder': 'Enter filter description'
        }
    ))

    filterWeight = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'filterWeight',
            'class': 'form-control',
            'placeholder': 'Enter filter weight'
        }
    ))

    ticketGroup = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'ticketGroup',
            'class': 'form-control',
            'placeholder': 'Enter ticket group'
        }
    ))
