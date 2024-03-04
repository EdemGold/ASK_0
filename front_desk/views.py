from django.shortcuts import render, redirect
from .forms import PatientRequisitionForm, ExistingPatientRequisitionForm, NewPatientRequisitionForm, ReferredDoctorForm, ServiceForm
from .models import ReferredDoctor, Service, Patient

def home(request):
    return render(request, 'home.html')

def front_desk_dashboard(request):
    patients = None
    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        if search_query:
            patients = Patient.objects.filter(full_name__icontains=search_query)
    return render(request, 'front_desk_dashboard.html', {'patients': patients})

def add_referred_doctor(request):
    if request.method == 'POST':
        form = ReferredDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('front-desk-dashboard')
    else:
        form = ReferredDoctorForm()
    return render(request, 'add_referred_doctor.html', {'form': form})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('front-desk-dashboard')
    else:
        form = ServiceForm()
    return render(request, 'add_service.html', {'form': form})

def add_patient_requisition(request):
    if request.method == 'POST':
        form = PatientRequisitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('front-desk-dashboard')
    else:
        form = PatientRequisitionForm()
    return render(request, 'add_patient_requisition.html', {'form': form})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('front-desk-dashboard')
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})

def search_patient(request):
    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        patients = Patient.objects.filter(full_name__icontains=search_query)
        return render(request, 'search_patient.html', {'patients': patients})
    return render(request, 'search_patient.html')

def patient_detail(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if request.method == 'POST':
        if 'existing_patient' in request.POST:
            form = ExistingPatientRequisitionForm(request.POST)
        else:
            form = NewPatientRequisitionForm(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            if 'existing_patient' not in request.POST:
                patient_data = {
                    'full_name': form.cleaned_data['full_name'],
                    'sex': form.cleaned_data['sex'],
                    'age': form.cleaned_data['age'],
                    'telephone': form.cleaned_data['telephone'],
                    'email': form.cleaned_data['email'],
                }
                patient = Patient.objects.create(**patient_data)
                requisition.patient = patient
            requisition.save()
            return redirect('patient-detail', patient_id=patient_id)
    else:
        form = ExistingPatientRequisitionForm()
    return render(request, 'patient_detail.html', {'patient': patient, 'form': form})

def new_patient_requisition(request):
    if request.method == 'POST':
        form = NewPatientRequisitionForm(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            patient_data = {
                'full_name': form.cleaned_data['full_name'],
                'sex': form.cleaned_data['sex'],
                'age': form.cleaned_data['age'],
                'telephone': form.cleaned_data['telephone'],
                'email': form.cleaned_data['email'],
            }
            patient = Patient.objects.create(**patient_data)
            requisition.patient = patient
            requisition.save()
            return redirect('front-desk-dashboard')
    else:
        form = NewPatientRequisitionForm()
    return render(request, 'new_patient_requisition.html', {'form': form})
