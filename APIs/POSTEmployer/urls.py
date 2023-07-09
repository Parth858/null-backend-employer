from django.urls import path
from .views import JobPostView

urlpatterns = [
    path('job/', JobPostView.as_view(), name='job_post'),
]