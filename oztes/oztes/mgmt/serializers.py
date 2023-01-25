from rest_framework import serializers
from .models import Agent, Emp



class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id','Emp' , 'OS']

    def create(self, validated_data):
        """
        Create and return a new `Agent` instance, given the validated data.
        """
        return Agent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Agent` instance, given the validated data.
        """
        instance.Emp = validated_data.get('Emp', instance.Emp)
        instance.OS = validated_data.get('OS', instance.OS)
        instance.save()
        return instance

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = ['id' , 'Name', 'LastName','Email', 'OU']

    def create(self, validated_data):
        """
        Create and return a new `Agent` instance, given the validated data.
        """
        return Emp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Agent` instance, given the validated data.
        """
        instance.Name = validated_data.get('Name', instance.Name)
        instance.LastName = validated_data.get('LastName', instance.LastName)
        instance.Email = validated_data.get('Email', instance.Email)
        instance.OU = validated_data.get('OU', instance.OU)
        instance.save()
        return instance