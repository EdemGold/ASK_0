from django.urls import path
from front_desk import views


urlpatterns = [
    path('', views.home, name='home'),
    path('front-desk/', views.front_desk_dashboard, name='front-desk-dashboard'),
    path('add-referred-doctor/', views.add_referred_doctor, name='add-referred-doctor'),
    path('add-service/', views.add_service, name='add-service'),
    path('add-patient-requisition/', views.add_patient_requisition, name='add-patient-requisition'),
    path('add-patient/', views.add_patient, name='add-patient'),
    path('search-patient/', views.search_patient, name='search-patient'),
    path('patient-detail/<int:patient_id>/', views.patient_detail, name='patient-detail'),
    path('new-patient-requisition/', views.new_patient_requisition, name='new-patient-requisition'),
    path('patient-requisition/', views.add_patient_requisition, name='patient-requisition'),  # Fixed view function name
]
