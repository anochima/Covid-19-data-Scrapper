from django.urls import path
from . import views


urlpatterns = [
    path('/', views.index, name='index'),
    path('/global/',views.globalRecords, name='global'),
    path('/faq/', views.Faqs, name='faq'),
    path('/highlights/',views.highlight, name='highlights'),
    path('/report/', views.report, name='report'),
    path('/guides/', views.guide, name='guides'),
    path('/about/',views.about, name='about'),
]