from django.db.models import *

# Create your models here.


class SubjectModel(Model):
    name = CharField(max_length=150, verbose_name='Название темы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class AnswerModel(Model):
    subject = ForeignKey(SubjectModel, on_delete=CASCADE, verbose_name='Тема')
    text = TextField(verbose_name='Варианты ответов')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class LessonModel(Model):
    name = CharField(max_length=150, verbose_name='Название')
    subjects = ManyToManyField(SubjectModel, verbose_name='Темы')
    date_created = DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Конспект'
        verbose_name_plural = 'Конспекты'


class LessonJSONModel(Model):
    text = TextField()
