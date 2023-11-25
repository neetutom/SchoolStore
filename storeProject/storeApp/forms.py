from django import forms

from storeApp.models import Order, Course, Department

stationary_list = [
    ('1', 'Exam-Papers'),
    ('2', 'Pens'),
    ('3', 'Notebooks'),
    ('4', 'Textbooks'),
    ('5', 'White-Board'),
    ('6', 'Geometry-Box'),
    ('7', 'Folders'),
    ('8', 'Calendar'),

]
class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stationary'] = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=stationary_list
        )
        self.fields['course'].queryset = Course.objects.none()
        # print(self.data)
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('course_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('course_name')
