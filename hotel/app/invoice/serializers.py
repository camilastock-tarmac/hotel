from rest_framework import serializers

class InvoiceItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
