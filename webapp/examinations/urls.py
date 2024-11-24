from django.urls import path
from . import views

urlpatterns = [
    path('<int:patient_id>/', views.PatientExaminationsView.as_view(), name='examinations'),
    path('<int:patient_id>/create', views.ExaminationCreateView.as_view(), name='examination_create'),
    path('<int:patient_id>/<int:pk>/details', views.ExaminationDetailView.as_view(), name='examination_details'),
    path('<int:patient_id>/<int:pk>/update', views.ExaminationUpdateView.as_view(), name='examination_update'),
    path('<int:patient_id>/<int:pk>/delete', views.ExaminationDeleteView.as_view(), name='examination_delete'),
]
