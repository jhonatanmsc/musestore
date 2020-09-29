from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_jwt.compat import PasswordField
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from django.utils.translation import gettext_lazy as _

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'is_staff', 'is_active', 'is_superuser', 'last_login']
        read_only_fields = ['id', 'last_login', 'is_active', 'is_superuser']


class TokenSerializer(JSONWebTokenSerializer):

    def __init__(self, *args, **kwargs):
        super(TokenSerializer, self).__init__(*args, **kwargs)
        self.fields['email'] = serializers.CharField(label=_("Email"))
        self.fields['password'] = PasswordField(label=_('password'), write_only=True)

    def validate(self, attrs):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    if not user.is_staff:
                        msg = _('Este usuário é inválido.')
                    else:
                        msg = _('Esta conta de usuário está desabilitada.')
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = _('Não foi possível efetuar login com credenciais fornecidas.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Deve incluir "email" e "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)
