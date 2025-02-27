from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from resolver import services
from resolver import serializers



class DnsResolveApiView(APIView):

    def get(self, request):
        """Render the browsable API form"""
        serializer = serializers.DnsResolveSerializer()
        return Response({
            'message': 'Enter domain name and record type below.',
            'form': serializer.data
        })

    def post(self, request):
        serializer = serializers.DnsResolveSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        domain = serializer.validated_data['domain']
        record_type = serializer.validated_data['record_type']
        try:
            result = services.resolve_dns(domain, record_type)
            return Response(result)
        except ValueError as e:
            return Response(
                {'error': str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


class ReverseDnsResolveApiView(APIView):
    def get(self, request):
        serializer = serializers.ReverseDnsResolveSerializer()
        return Response({
            'message': 'Enter domain name and record type below.',
            'form': serializer.data
        })

    def post(self, request):
        serializer = serializers.ReverseDnsResolveSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ip_address = serializer.validated_data['ip_address']
        try:
            result = services.reverse_dns(ip_address)
            return Response(result)
        except ValueError as e:
            return Response(
                {'error': str(e)}, status=status.HTTP_400_BAD_REQUEST
            )
