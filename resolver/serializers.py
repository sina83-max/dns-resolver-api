from rest_framework import serializers

class DnsResponseSerializer(serializers.Serializer):
    domain = serializers.CharField()
    type = serializers.CharField()
    records = serializers.ListField(child=serializers.CharField())
    ttl = serializers.IntegerField()

class DnsResolveSerializer(serializers.Serializer):
    domain = serializers.CharField(
        help_text= 'The domain name to be resolved(e.g: google.com)',
        required= True
    )
    record_type = serializers.ChoiceField(
        choices=['A', 'AAAA', 'MX', 'CNAME', 'TXT'],
        default='A',
        help_text='DNS record type(default: A)'
    )

class ReverseDnsResolveSerializer(serializers.Serializer):
    ip_address = serializers.CharField(
        help_text='Enter the IP address that need to be reversed(e.g: 8.8.8.8)',
        required=True
    )