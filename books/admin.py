'''
Файл, для описания того, как будут выглядеть наши модели
во встроенной админ панели джанго
'''
from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    '''
    Класс админ панели для модели Авторов
    '''
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)


class BookAdmin(admin.ModelAdmin):
    '''
    Класс админ панели для модели Книг
    '''
    list_display = ('title', 'author__name') # Через __ мы можем обращаться к полям связанной модели
    search_fields = ('title', 'author__name') # В нашем случае мы обращаемся в полю name модели Author
    list_filter = ('author', )
    ordering = ('title',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)