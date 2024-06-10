from django.contrib import admin
from .models import Titanic

@admin.register(Titanic)
class TitanicAdmin(admin.ModelAdmin):
    list_display = ('PassengerId', 'Name', 'Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked')
    search_fields = ('Name', 'Ticket', 'Cabin')
    list_filter = ('Survived', 'Pclass', 'Sex', 'Embarked')
