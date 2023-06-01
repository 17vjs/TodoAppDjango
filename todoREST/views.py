from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todoREST.models import Task
from .serializers import TaskSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
class TaskView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        print(request.user)
        if id !=None:
            result = Task.objects.get(id=id)
            serializers = TaskSerializer(result)
            return Response({'success': 'success', "tasks":serializers.data}, status=200)
        result = Task.objects.all()
        serializers = TaskSerializer(result, many=True)
        return Response({'status': 'success', "tasks":serializers.data}, status=200)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id):
        result = Task.objects.get(id=id)
        serializer = TaskSerializer(result, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    def delete(self, request, id=None):
        result = get_object_or_404(Task, id=id)
        result.delete()
        return Response({"status": "success", "data": "Record Deleted"})