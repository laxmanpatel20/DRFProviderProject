
from rest_framework import serializers
from DEFProjectDemoApp.models import Employee, Department, Country
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):

    employees = EmployeeSerializer(read_only=True, many=True, source="Departments")

    class Meta:
        model = Department
        fields = '__all__'

class CountrySarializer(serializers.ModelSerializer):

    employees = EmployeeSerializer(read_only=True, many=True, source="Countries")

    class Meta:
        model = Country
        fields = '__all__'

