from django import forms
from django.utils.safestring import mark_safe

STYLIST_CHOICES = [
    ('Oliver Jake', 'Oliver Jake'),
    ('Jack Liam', 'Jack Liam'),
    ('Adam Phillips', 'Adam Phillips'),
    ('Charlie Kyle', 'Charlie Kyle'),
    ('Michael Richard', 'Michael Richard'),
    ('Jhon Doe', 'Jhon Doe'),
    ('Dylan Adams', 'Dylan Adams'),
    ('Josh Dunn', 'Josh Dunn'),
    ('Olivia Samantha', 'Olivia Samantha'),
    ('James Bond', 'James Bond'),
]

class BookingForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Name",
                'autocomplete':'off',
            }
        )
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
                'placeholder': "Email",
                'autocomplete':'off',
            }
        )
    )
    phone = forms.CharField(
        required=True,
        max_length=12,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Phone",

                'autocomplete':'off',
            }
        )
    )
    
    date = forms.DateField(
        required=True,
        widget=forms.DateInput(format='%d/%m/%Y',
            attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': "DD/MM/YYYY",
                'autocomplete':'off',
            }
        )
    )
    time = forms.TimeField(
        required=True,
        widget=forms.TimeInput(
            format='%H:%M',
            attrs={
                'class': 'form-control',
                'type': 'time',
                'placeholder': "HH:MM",
                'autocomplete':'off',
            }
        )
    )
    stylist = forms.ChoiceField(
        choices=STYLIST_CHOICES,
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': "Select Stylist",
                'autocomplete':'off',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{field_classes} control-group input-group'

    def as_div(self):
        output = ''
        for field in self:
            output += f'''
                <div class="control-group">
                    <div class="input-group">
                        {field}
                        <div class="input-group-append">
                            <div class="input-group-text">
                                <i class="fa fa-{self.get_icon(field.name)}"></i>
                            </div>
                        </div>
                    </div>
                </div>
            '''
        return mark_safe(output)

    def get_icon(self, field_name):
        icons = {
            'name': 'user',
            'email': 'envelope',
            'phone': 'phone',
            'date': 'calendar',
            'time': 'clock',
            'stylist': 'scissors'
        }
        return icons.get(field_name, 'pencil-alt')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return phone

