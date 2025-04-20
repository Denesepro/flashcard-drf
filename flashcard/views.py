from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from flashcard.models import Flashcard
from flashcard.serializers import CreateFlashCardSerializers, UpdateFlashCardSerializers, ListFlashCardSerializers


class CreateFlashCardView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = CreateFlashCardSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)

class UpdateFlashCardView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self,request,id):
        flashcard = get_object_or_404(Flashcard,id=id)
        serializer = UpdateFlashCardSerializers(data=request.data , instance=flashcard)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteFlashCardView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self,request,id):
        flashcard = get_object_or_404(Flashcard,id=id)
        flashcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListFlashCardView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,user_id):
        flashcards = get_list_or_404(Flashcard,user_id=user_id)
        serializer = ListFlashCardSerializers(flashcards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


