from django.shortcuts import get_object_or_404
from .models import Student
from django.shortcuts import redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentListSerializer, StudentCreateSerializer, CheckboxesForm, StudentDeleteSerializer
from rest_framework import generics
from rest_framework import status


class StudentList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request):
        queryset = Student.objects.all()
        return Response({'profiles': queryset})


class StudentDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(Student, pk=pk)
        serializer = StudentListSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(Student, pk=pk)
        serializer = StudentListSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('api-create:list')


class StudentCreate(APIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'create.html'

    def get(self, request, format=None):
        serializer = StudentCreateSerializer
        return Response({'serializer': serializer})

    def post(self, request, format=None):
        serializer = StudentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('api-create:list')
        else:
            return Response({'serializer': serializer}, status=status.HTTP_400_BAD_REQUEST)


# class StudentDelete(APIView):
#     queryset = Student.objects.all()
#     #serializer_class = StudentDeleteSerializer
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'delete.html'
#
#     def get(self, request, format=None):
#         serializer = Student.objects.all()
#         return Response({'serializer': serializer})
#
#     def post(self, request, *args, **kwargs):
#         obj = Student.objects.all()
#         if request.method== 'POST':
#            obj.delete()
#            return Response("obj deleted", status=status.HTTP_204_NO_CONTENT)

class StudentDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'delete.html'

    def get(self, request):
        queryset = Student.objects.all()
        return Response({'profiles': queryset})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            product_ids = request.POST.getlist('id[]')
            for id in product_ids:
                product = Student.objects.aget(pk=id)
                product.delete()
            return redirect('api-create:delete')
