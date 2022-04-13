from rest_framework import serializers


class AddressSerializer(serializers.Serializer):

    line1 = serializers.CharField(max_length=100)
    output_format = serializers.ChoiceField(choices=["xml", "json"])
