"""Defines URL patterns for daisy_diary_app."""

from django.urls import path
from . import views

app_name = 'daisy_diary_app'
urlpatterns = [
    # Home Page
    path('',views.index, name='index'),
    # Page that shows all Dates.
    path('dates/', views.dates, name='dates'),

    path('dates/<int:date_id>/', views.date, name='date'),
]

"""Defines url patterns for learning_logs."""

# from django.conf.urls import url

# from . import views

# urlpatterns = [
#     # Home page.
#     url(r'^$', views.index, name='index'),
    
#     # Show all topics.
#     url(r'^topics/$', views.topics, name='topics'),
    
#     # Detail page for a single topic.
#     url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
# ]
