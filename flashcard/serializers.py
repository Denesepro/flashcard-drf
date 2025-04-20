from rest_framework import serializers

from flashcard.models import Flashcard


class CreateFlashCardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'


class UpdateFlashCardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('question', 'answer',)

class ListFlashCardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = '__all__'
