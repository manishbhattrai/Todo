from rest_framework import serializers
from todo.models import Todo
from django.contrib.auth.models import User




class UserRegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only = True, style = {'input_type':'password'})
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username','email','password','password2']

    def validate(self, data):

        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("Password didn't match.")
        
        if len(password) <8:
            raise serializers.ValidationError("Password should be more than 8 characters.")
        
        return data
    
    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)

        user.set_password(password)
        user.save()
        
        return user


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only = True)



class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['title','description','user','is_completed','due_date','priority','created_at','updated_at']
        read_only_fields = ['created_at', 'updated_at', 'user']

