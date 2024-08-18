from django.urls import path
from . import views
urlpatterns = [
    path('', views.patients_home, name='patients_home'),
    path('create', views.patient_create, name='patient_create'),
    path('<int:pk>', views.PatientDetailView.as_view(), name='patient_details'),
    path('<int:pk>/update', views.PatientUpdateView.as_view(), name='patient_update'),
    path('<int:pk>/delete', views.PatientDeleteView.as_view(), name='patient_delete')
]
