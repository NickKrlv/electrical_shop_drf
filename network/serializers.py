from rest_framework import serializers
from .models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt_to_supplier', 'level')

    def validate(self, data):
        if self.instance and 'debt_to_supplier' in data:
            raise serializers.ValidationError({"debt_to_supplier": "Updating debt_to_supplier is not allowed."})
        return data
