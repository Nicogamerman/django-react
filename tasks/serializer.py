from rest_framework import serializers
from .models import Task

#convierto tipo de datos de python a JSON
class TasksSerializer(serializers. ModelSerializer):
    class Meta:
        model = Task
        #fields = ('id','title','description','done')
        fields= '__all__' #de esta forma traigo todos los campos de los models.