from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib import auth
import pintrest


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = auth.models.User
        fields = ('email', 'username', 'password', 'password_confirm')


    def save(self, **kwargs):
        # user = User(email=self.validated_data.get('email'), username=self.validated_data.get('username'))
        u = pintrest.models.User(
            first_name="john",
            last_name="doe",
            account=auth.models.User(email=self.validated_data.get('email'), username=self.validated_data.get('username'))
        )
        
        # u.account = auth.models.User(email=self.validated_data.get('email'), username=self.validated_data.get('username'))

        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError(
                { 
                    'password': "Passworkd doesn't match"
                }
            )
        else:
            u.account.set_password(self.validated_data.get('password'))
            u.account.save()
            u.save()
            return u.account

