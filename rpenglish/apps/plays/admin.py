#--coding: utf8--

from django.contrib import admin

from .models import Play, PlayStudents


class PlayStudentsInline(admin.TabularInline):
    model = PlayStudents
    extra = 0


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    inlines = [PlayStudentsInline, ]
