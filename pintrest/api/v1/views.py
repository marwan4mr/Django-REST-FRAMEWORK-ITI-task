from re import S
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pintrest.models import Movie
from .serializers import MovieSerializer
from django.shortcuts import get_object_or_404

# custom permission 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.decorators import api_view,permission_classes,authentication_classes
class UserCanDeleteMovie(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Can-Delete").exists():
            return True
        else:
            return False
    
@api_view(["GET", "POST"])
def movie_index(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(instance=movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        return create_movie(request)

def create_movie(request):
    print(f'\nrequest.post: {request.POST}\n')
    print(f'\nrequest.data: {request.data}\n')
    
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def handle_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return get_movie(movie)
    if request.method == 'PATCH' or request.method == 'PUT':
        return update_movie(request, movie)
    if request.method == 'DELETE':
    # seems like i need to make cusom endpoints like movie/1/delete
        return delete_movie(movie)
   
def get_movie(movie):
    serializer = MovieSerializer(instance=movie)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
    
def update_movie(request, movie):

    if request.method == "PUT":
        serialized_movie = MovieSerializer(instance=movie, data=request.data)
    elif request.method == "PATCH":
        serialized_movie = MovieSerializer(instance=movie, data=request.data, partial=True)
    if serialized_movie.is_valid(): 
        serialized_movie.save()
        return Response(data=serialized_movie.data, status= status.HTTP_200_OK)
    else:
        return Response(data=serialized_movie.error, status= status.HTTP_400_BAD_REQUEST)

def delete_movie(movie):
    try:
        movie.delete()
        return Response(data={"delete": "success"}, status=status.HTTP_200_OK)
    except Exception  as e:
        print(e)
