from django.contrib import admin
from django.urls import path,include
from . import views
from property.views import *


urlpatterns = [

    path('create_project/',ProjectCreationView.as_view(),name='create_project'),
    path('add_property/',AddpropertyView.as_view(),name='properties'),
    path('list_project/',ProjectListView.as_view(),name='project_list'),
    path('list_property/',PropertyListView.as_view(),name='property_list'),
    path('list_project1/',ProjectList1View.as_view(),name='project_list1'),
    path('delete_project/<int:pk>',ProjectDeleteView.as_view(),name='delete_project'),
    path('update_project/<int:pk>',ProjectUpdateView.as_view(),name='update_project'),
    path('detail_project/<int:pk>',ProjectDetailView.as_view(),name='detail_project'),
    path('create_project_team/',Create_Project_team.as_view(),name='create_project_team'),
    path('list_project_team/',ProjectTeamListView.as_view(),name='project_team_list'),
    path('list_project_team1/<int:pk>',ProjectTeamByProject.as_view(),name='project_team_list1'),
]
 

