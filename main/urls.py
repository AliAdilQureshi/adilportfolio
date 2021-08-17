from django.urls import path
from main.views import home, services, skill, team, contact, portfolio, ContactSuccess
urlpatterns = [
  path('', home, name='home'),
  path('services/', services, name='services'),
  path('skill/', skill, name='skill'),
  path('team/', team, name="team"),
  path('contact/', contact, name="contact"),
  path('portfolio/', portfolio, name='portfolio'),
  path('contact/success/', ContactSuccess, name='contactsuccess'),

]