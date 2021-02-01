from . import views
from django.urls import path

urlpatterns = [
    # http://127.0.0.1:8000/payment/jump/
    path('jump/',views.JumpView.as_view()),
    # http://127.0.0.1:8000/payment/result/
    path('result/',views.ResultView.as_view()),
]
