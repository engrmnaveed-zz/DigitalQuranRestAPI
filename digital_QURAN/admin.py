from django_admin_bootstrapped.admin.models import SortableInline

from django.contrib import admin
from models import *

meta_change_option = True

class JuzAdmin(admin.ModelAdmin):
    list_display = ('index', 'sura', 'aya')
    fields = (('sura', 'aya'), )
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return meta_change_option

class SuraAdmin(admin.ModelAdmin):
    list_display = ('index', 'ayas', 'start', 'name', 'tname', 'ename', 'type', 'order', 'rukus')
    fields = ('ayas', 'start', 'name', 'tname', 'ename', 'type', 'order', 'rukus')
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return meta_change_option

class HizbAdmin(admin.ModelAdmin):
    list_display = ('index', 'sura', 'aya')
    fields = (('sura', 'aya'), )
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return meta_change_option

class ManzilAdmin(admin.ModelAdmin):
    list_display = ('index', 'sura', 'aya')
    fields = (('sura', 'aya'), )
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return meta_change_option

class RukuAdmin(admin.ModelAdmin):
    list_display = ('index', 'sura', 'aya')
    fields = (('sura', 'aya'), )
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return meta_change_option

class PageAdmin(admin.ModelAdmin):
    list_display = ('index', 'sura', 'aya')
    fields = (('sura', 'aya'), )
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return meta_change_option

class SajdaAdmin(admin.ModelAdmin):
    list_display = ('index', 'sura', 'aya', 'type')
    fields = (('sura', 'aya'), 'type')
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return meta_change_option

class QuranTextAdmin(admin.ModelAdmin):
    list_display = ('index', 'sura', 'aya', 'text')
    fields = (('sura', 'aya'), 'text')
    list_filter = ('sura', 'aya')
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return meta_change_option

admin.site.register(Juz, JuzAdmin)
admin.site.register(Sura, SuraAdmin)
admin.site.register(Hizb, HizbAdmin)
admin.site.register(Manzil, ManzilAdmin)
admin.site.register(Ruku, RukuAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Sajda, SajdaAdmin)
admin.site.register(QuranText, QuranTextAdmin)


class QuranTranslationTextAdmin(admin.ModelAdmin):
    list_display = ('tranlation', 'sura', 'aya', 'text')
    fields = (('sura', 'aya'), 'text')
    list_filter = ('tranlation', 'sura', 'aya')
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False



class QuranTranslationAdmin(admin.ModelAdmin):
    list_display = ('language','name','translator')
    fields = ('language','name','translator', 'language_flag_img', 'translation_file')

    def save_form(self, request, form, change):
        """
            Given a ModelForm return an unsaved instance. ``change`` is True if
            the object is being changed, and False if it's being added.
            """
        obj = form.save(commit=False)
        try:
            obj.id = QuranTranslation.objects.latest('id').id + 1
        except QuranTranslation.DoesNotExist:
            obj.id = 1
        from django.utils.datastructures import MultiValueDictKeyError
        try:
            f = request.FILES['translation_file']
        except MultiValueDictKeyError:
            f = False
        if f:
            lines = f.readlines()
            for line in lines:
                data = line.split('|')
#                 try:
                QuranTranslationText(tranlation=obj, sura=int(data[0]), aya=int(data[1]), text=data[2]).save()
#                 except:
#                     print data
#                     print 'Naveed'
#                     print line

        return obj

admin.site.register(QuranTranslation, QuranTranslationAdmin)
admin.site.register(QuranTranslationText, QuranTranslationTextAdmin)


class RecitationVerseByVerseAdmin(admin.ModelAdmin):
    list_display = ('index', 'language', 'translator', 'quality_Kbps')
    fields = ('index', 'language', 'translator', 'quality_Kbps')
    list_filter = ('index', 'language', 'translator', 'quality_Kbps')
    
class RecitationPageByPageAdmin(admin.ModelAdmin):
    list_display = ('index', 'language', 'translator', 'quality_Kbps')
    fields = ('index', 'language', 'translator', 'quality_Kbps')
    list_filter = ('index', 'language', 'translator', 'quality_Kbps')
    
admin.site.register(RecitationVerseByVerse, RecitationVerseByVerseAdmin)
admin.site.register(RecitationPageByPage, RecitationPageByPageAdmin)
