from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Company
from api.serializers import CompanySerializer

@api_view(['GET', 'POST'])
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # request.data — это данные, которые ты прислал из Postman
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # Вызовет тот самый create() в сериализаторе
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Передаем объект 'company', чтобы обновить именно его
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save() # Вызовет update() в сериализаторе
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)