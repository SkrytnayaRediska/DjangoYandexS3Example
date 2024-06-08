from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser, FormParser
from testapp.models import TestModel
from testapp.serializers import TestModelSerializer
from rest_framework.response import Response


class TestViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer
    parser_classes = (MultiPartParser, FormParser)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.file.delete(False)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
