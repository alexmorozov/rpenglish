from django.contrib import admin

from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline

from .models import Bit, Script, Line


class LineInline(SortableStackedInline):
    model = Line
    extra = 1


@admin.register(Bit)
class BitAdmin(NonSortableParentAdmin):
    inlines = (LineInline, )
    select_related = ('script', )


class BitInline(SortableStackedInline):
    model = Bit
    extra = 1


@admin.register(Script)
class ScriptAdmin(NonSortableParentAdmin):
    inlines = (BitInline, )
