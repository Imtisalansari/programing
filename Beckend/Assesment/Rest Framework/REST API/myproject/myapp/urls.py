from django.urls import path
from .views import get_random_joke, DoctorListCreateView, DoctorRetrieveUpdateDeleteView  # ✅ Fixed import

urlpatterns = [
    path('random-joke/', get_random_joke, name='random_joke'),
    path("doctors/", DoctorListCreateView.as_view(), name="doctor-list-create"),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDeleteView.as_view(), name='doctor-detail'),  # ✅ Fixed name
]
