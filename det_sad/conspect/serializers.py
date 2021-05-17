from rest_framework.serializers import *
from .models import *


class AnswerSerializer(ModelSerializer):

    class Meta:
        model = AnswerModel
        fields = ['id', 'text']


class SubjectSerializer(ModelSerializer):
    answers = SerializerMethodField()

    class Meta:
        model = SubjectModel
        fields = ['id', 'name', 'answers']

    def get_answers(self, obj):
        answers = obj.answermodel_set.all()
        serializer = AnswerSerializer(answers, many=True)
        return serializer.data


class LessonSerializer(ModelSerializer):
    subjects = SubjectSerializer(many=True)

    def create_json(self):
        json = str(self.initial_data)
        text_model = LessonJSONModel.objects.create(text=json)
        print(json)
        return text_model

    class Meta:
        model = LessonModel
        fields = ['id', 'name', 'date_created', 'subjects']
        depth = 10


