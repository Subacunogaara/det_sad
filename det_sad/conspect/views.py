from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import Response, APIView
from .models import *
from .serializers import *
# Create your views here.


class LessonView(APIView):

    def get(self, request):
        objects = LessonModel.objects.all()
        serializer = LessonSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.POST)
        serializer = LessonSerializer(data=request.data)
        serializer.create_json()
        return HttpResponse(status=201)


def lessons(request):
    objects = SubjectModel.objects.all()
    context = {'subjects': objects}
    return render(request, 'index.html', context)

