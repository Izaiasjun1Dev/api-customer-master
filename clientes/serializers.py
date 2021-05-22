from rest_framework import serializers
from clientes.models import Cliente
from .validators import *


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):

        if not validate_nome(data['nome']):
            raise serializers.ValidationError({
                'Nome': 'Não inclua numeros neste campo'
            })

        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({
                'Cpf': "O cpf é invalido"
            })

        if not validate_rg(data['rg']):
            raise serializers.ValidationError({
                'Rg': 'Um RG valido deve conter 9 caracteres, verifique o seu RG!'
            })

        if not validate_celular(data['celular']):
            raise serializers.ValidationError({
                'Celular': 'O numero de celular deve conter o seguinte format 11 11111-1111'
            })

        return data
