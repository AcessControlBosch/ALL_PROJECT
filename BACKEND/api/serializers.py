from rest_framework import serializers
from .models import *

class UserTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = User
        fields = '__all__' 

class ApprenticeTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Apprentice
        fields = '__all__' 

class typeAssocienteTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = typeAssociente
        fields = '__all__' 

class AssociateTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Associate
        fields = '__all__' 

class MachineTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Machine
        fields = '__all__'

class QuestionTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Question
        fields = '__all__'

class GreenBookTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = GreenBook
        fields = '__all__'

class MaintenanceTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Maintenance
        fields = '__all__'

class ReleaseMachineTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = ReleaseMachine
        fields = '__all__'

class QRcodeTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = QRcode
        fields = '__all__'

class ObservationTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Observation
        fields = '__all__'

class MaintenanceOrderTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = MaintenanceOrder
        fields = '__all__'

class CoursesTable(serializers.ModelSerializer):

    class Meta: 
        many = True
        model = Courses
        fields = '__all__'