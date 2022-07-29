from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path("users/", UserAPI.as_view(), name="users"),
    path("users/<int:pk>/", UserAPI.as_view(), name="usersParameters"),

    path("apprentices/", ApprenticeAPI.as_view(), name="apprentices"),
    path("apprentices/<int:pk>/", UserAPI.as_view(), name="apprenticesParameters"),

    path("typeAssociente/", typeAssocienteAPI.as_view(), name="typeAssocientes"),
    path("typeAssociente/<int:pk>/", typeAssocienteAPI.as_view(), name="typeAssocientesParameters"),

    path("associates/", AssociateAPI.as_view(), name="associates"),
    path("associates/<int:pk>/", AssociateAPI.as_view(), name="associatesParameters"),

    path("machines/", MachineAPI.as_view(), name="machines"),
    path("machines/<int:pk>/", MachineAPI.as_view(), name="machinesParameters"),

    path("questions/", QuestionsAPI.as_view(), name="questions"),
    path("questions/<int:pk>/", QuestionsAPI.as_view(), name="questionsParameters"),

    path("greenbooks/", GreenBookAPI.as_view(), name="greenbooks"),
    path("greenbooks/<int:pk>/", GreenBookAPI.as_view(), name="greenbooksParameters"),

    path("maintenances/", MaintenanceAPI.as_view(), name="maintenances"),
    path("maintenances/<int:pk>/", MaintenanceAPI.as_view(), name="maintenancesParameters"),

    path("maintenances/", MaintenanceAPI.as_view(), name="maintenances"),
    path("maintenances/<int:pk>/", MaintenanceAPI.as_view(), name="maintenancesParameters"),



]