from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import resolve_dns
from .serializers import DnsResponseSerializer

class DnsResolveView(APIView):

    def get(self, request):
        domain = request.query_params.get('domain')
        record_type = request.query_params.get('type')
        if not domain:
            return Response(
                {'error': "domain parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            result = resolve_dns(domain, record_type)
            serializer = DnsResponseSerializer(result)
            return Response(serializer.data)
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

