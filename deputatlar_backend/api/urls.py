from django.urls import path
from .views import BlogList, BlogDetail

urlpatterns = [
    path('blog/<int:pk>/', BlogDetail.as_view(), name="BD"),
    path('blog/', BlogList.as_view(), name="BL")
]