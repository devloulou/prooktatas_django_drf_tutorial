from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import GroupCategoryModel, SubCategoryModel
from .serializers import GroupCategoryModelSerializer, SubCategoryModelSerializer
from rest_framework.views import APIView

@api_view(['GET'])
def test_view(request):
    return Response(
        data={"result": "ok"},
        status=status.HTTP_200_OK)

@api_view(['GET'])
def test_view2(request):
    return Response(
        data={"result": "ok"},
        status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def group_category_view(request):
    if request.method == 'GET':
        # g_category egy queryset objectum / instance
        g_category = GroupCategoryModel.objects.all()
        g_serializer = GroupCategoryModelSerializer(g_category, many=True)
        return Response(g_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        g_serializer = GroupCategoryModelSerializer(data=request.data)
        if g_serializer.is_valid():
            g_serializer.save()
            return Response(g_serializer.data, status=status.HTTP_201_CREATED)
        return Response(g_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# APIView
class SubCategoryView(APIView):

    def get(self, request, format=None):
        sub_category = SubCategoryModel.objects.all()
        serializer = SubCategoryModelSerializer(sub_category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SubCategoryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)