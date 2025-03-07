from django.urls import path
from django.shortcuts import redirect

from . import views
from .views import register, login_view, logout_view, dashboard, add_transaction, edit_transaction, delete_transaction


def index(request):
    return redirect('/dashboard/')


urlpatterns = [
    path('', index),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_transaction/<str:type>/', views.add_transaction, name='add_income_transaction'),
    path('add_transaction/<str:type>/', views.add_transaction, name='add_expense_transaction'),
    path('edit/<int:id>/', edit_transaction, name='edit_transaction'),
    path('delete/<int:id>/', delete_transaction, name='delete_transaction'),
]
