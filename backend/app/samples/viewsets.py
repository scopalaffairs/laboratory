from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Reading
from .serializers import ReadingSerializer


class ReadingAPIView(APIView):
    def get_object(self, pk):
        try:
            reading = Reading.objects.get(pk=pk)
            if reading is not None:
                return reading
        except Reading.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = ReadingSerializer(data)

        else:
            data = Reading.objects.all()
            serializer = ReadingSerializer(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        serializer = ReadingSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None, format=None):
        reading_to_update = self.get_object(pk)
        serializer = ReadingSerializer(
            instance=reading_to_update, data=request.data, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        reading_to_delete = self.get_object(pk)
        reading_to_delete.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
