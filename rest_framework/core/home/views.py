from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PeopleSerializer,LoginSerializer
from rest_framework.views import APIView 
from rest_framework import viewsets
from rest_framework import status


@api_view(['GET'])
def index(request):
    courses = {
        'course_name':'Python',
        'learn':{'Flask','Django','FastApi','Tornado'},
        'course_provider':'Scaler'
    }

    return Response(courses)


class PersonApi(APIView):
    def get(self, request):
        objs = Person.objects.filter(color__isnull = False)
        serializer = PeopleSerializer(objs,many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def put(self, request):
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delere(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({
            'message':"Person data deleted"
        })



@api_view(['GET','POST','PUT','DELETE'])
def people(request):
    if request.method == 'GET':
        objs = Person.objects.filter(color__isnull = False)
        serializer = PeopleSerializer(objs,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    elif request.method == "PUT":
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "PATCH":
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    else:
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({
            'message':"Person data deleted"
        })
        

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        print(data)
        return Response({
            'message':"Success"
        }) 

    return Response(serializer.errors)



class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()

    def list(self,request):
        search = request.GET.get('search')
        querySet = self.queryset
        if search:
            querySet = querySet.filter(name__startswith = search)

        serializer = PeopleSerializer(querySet,many=True)

        return Response({'status':200,'data':serializer.data}, status=status.HTTP_200_OK)