from django import forms
from .models import ReferredDoctor, Service, PatientRequisition, Patient

class ReferredDoctorForm(forms.ModelForm):
    class Meta:
        model = ReferredDoctor
        fields = ['name', 'telephone', 'email']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price']

class ExistingPatientRequisitionForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    referred_by = forms.ModelChoiceField(queryset=ReferredDoctor.objects.all())
    requisitions = forms.ModelMultipleChoiceField(queryset=Service.objects.all())
    discount = forms.DecimalField()
    total_amount_paid = forms.DecimalField()

    class Meta:
        model = PatientRequisition
        fields = ['patient', 'referred_by', 'requisitions', 'discount', 'total_amount_paid']

    def __init__(self, *args, **kwargs):
        super(ExistingPatientRequisitionForm, self).__init__(*args, **kwargs)
        self.fields['referred_by'].queryset = ReferredDoctor.objects.all()
        self.fields['requisitions'].queryset = Service.objects.all()

class NewPatientRequisitionForm(forms.ModelForm):
    full_name = forms.CharField(max_length=200)
    sex = forms.ChoiceField(choices=(('Male', 'Male'), ('Female', 'Female')))
    age = forms.IntegerField()
    telephone = forms.CharField(max_length=15)
    email = forms.EmailField()
    referred_by = forms.ModelChoiceField(queryset=ReferredDoctor.objects.all())
    requisitions = forms.ModelMultipleChoiceField(queryset=Service.objects.all())
    discount = forms.DecimalField()
    total_amount_paid = forms.DecimalField()

    class Meta:
        model = PatientRequisition
        fields = ['full_name', 'sex', 'age', 'telephone', 'email', 'referred_by', 'requisitions', 'discount', 'total_amount_paid']

    def __init__(self, *args, **kwargs):
        super(NewPatientRequisitionForm, self).__init__(*args, **kwargs)
        self.fields['referred_by'].queryset = ReferredDoctor.objects.all()
        self.fields['requisitions'].queryset = Service.objects.all()()
        self.fields['requisitions'].queryset = Service.objects.all()

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['full_name', 'sex', 'age', 'telephone', 'email']

