from django import forms
from django.core.exceptions import ValidationError

from contacts.models import Contact, Address

from django.forms.models import inlineformset_factory


class ContactForm(forms.ModelForm):

    confirm_email = forms.EmailField(
        "Confirm email",
        required=True,
    )


    # inlineformset_factory creates a Class from a parent model (Contact)
    # to a child model (Address)
    ContactAddressFormSet = inlineformset_factory(
        Contact,
        Address,
    )

    class Meta:
        model = Contact

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email'] = email

        return super(ContactForm, self).__init__(*args, **kwargs)

