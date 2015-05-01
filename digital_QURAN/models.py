from django.db import models
from compiler.pyassem import order_blocks
from django.utils.timezone import now
from django.forms.models import model_to_dict

# Create your models here.

media_url = '/media/'
RECITATION_VERSE_BY_VERSE_ROOT='/media/recitations/verse-by-verse/'
RECITATION_PAGE_BY_PAGE_ROOT='/media/recitations/page-by-page/'

def language_flag_image(instance, filename):
    return 'lang_flag/%s/%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename,
    )

def translation_file(instance, filename):
    return 'translation_files/%s/%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename,
    )
    
SURA_TYPE_CHOICES = (
    ('Meccan', 'Meccan'),
    ('Medinan', 'Medinan')
)


class Juz(models.Model):
    index = models.IntegerField(primary_key=True)
    sura = models.IntegerField()
    aya = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def to_dict(self):
        dict = model_to_dict(self)
        return dict

    def to_dict_api(self):
        dict = model_to_dict(self, exclude=[])
        return dict

    def __str__(self):
        return self.index

    def __unicode__(self):
        return u'%s' % (self.index)

    class Meta:
        verbose_name = '1.0- Juz __ META-DATA'
        verbose_name_plural = "1.0- Juz __ META-DATA"
        

class Sura(models.Model):
    index = models.IntegerField(primary_key=True)
    ayas = models.IntegerField()
    start = models.IntegerField()
    name = models.CharField(max_length=255)
    tname = models.CharField(max_length=255)
    ename = models.CharField(max_length=255)
    type = models.CharField(max_length=45, default='Meccan', choices=SURA_TYPE_CHOICES)
    order = models.IntegerField()
    rukus = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def to_dict(self):
        dict = model_to_dict(self)
        return dict

    def to_dict_api(self):
        dict = model_to_dict(self, exclude=[])
        return dict

    def __str__(self):
        return self.tname

    def __unicode__(self):
        return u'%s' % (self.tname)

    class Meta:
        verbose_name = '1.1 - Sura __ META-DATA'
        verbose_name_plural = "1.1 - Sura __ META-DATA"
        

class Hizb(models.Model):
    index = models.IntegerField(primary_key=True)
    sura = models.IntegerField()
    aya = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def to_dict(self):
        dict = model_to_dict(self)
        return dict

    def to_dict_api(self):
        dict = model_to_dict(self, exclude=[])
        return dict

    def __str__(self):
        return self.index

    def __unicode__(self):
        return u'%s' % (self.index)

    class Meta:
        verbose_name = '1.2 - Hizb __ META-DATA'
        verbose_name_plural = "1.2 - Hizb __ META-DATA"      
        

class Manzil(models.Model):
    index = models.IntegerField(primary_key=True)
    sura = models.IntegerField()
    aya = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def to_dict(self):
        dict = model_to_dict(self)
        return dict

    def to_dict_api(self):
        dict = model_to_dict(self, exclude=[])
        return dict

    def __str__(self):
        return self.index

    def __unicode__(self):
        return u'%s' % (self.index)

    class Meta:
        verbose_name = '1.3 - Manzil __ META-DATA'
        verbose_name_plural = "1.3 - Manzil __ META-DATA"   
        

class Ruku(models.Model):
    index = models.IntegerField(primary_key=True)
    sura = models.IntegerField()
    aya = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def to_dict(self):
        dict = model_to_dict(self)
        return dict

    def to_dict_api(self):
        dict = model_to_dict(self, exclude=[])
        return dict

    def __str__(self):
        return self.index

    def __unicode__(self):
        return u'%s' % (self.index)

    class Meta:
        verbose_name = '1.4 - Ruku __ META-DATA'
        verbose_name_plural = "1.4 - Ruku __ META-DATA"  
        
        
class Page(models.Model):
    index = models.IntegerField(primary_key=True)
    sura = models.IntegerField()
    aya = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def to_dict(self):
        dict = model_to_dict(self)
        return dict

    def to_dict_api(self):
        dict = model_to_dict(self, exclude=[])
        return dict

    def __str__(self):
        return self.index

    def __unicode__(self):
        return u'%s' % (self.index)

    class Meta:
        verbose_name = '1.5 - Page __ META-DATA'
        verbose_name_plural = "1.5 - Page __ META-DATA" 


class Sajda(models.Model):
    index = models.IntegerField(primary_key=True)
    sura = models.IntegerField()
    aya = models.IntegerField()
    type = models.CharField(max_length=45)
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def to_dict(self):
        dict = model_to_dict(self)
        return dict

    def to_dict_api(self):
        dict = model_to_dict(self, exclude=[])
        return dict

    def __str__(self):
        return self.index

    def __unicode__(self):
        return u'%s' % (self.index)

    class Meta:
        verbose_name = '1.6 - Sajda __ META-DATA'
        verbose_name_plural = "1.6 - Sajda __ META-DATA" 


class QuranText(models.Model):
    index = models.IntegerField(primary_key=True)
    sura = models.IntegerField()
    aya = models.IntegerField()
    text = models.TextField()
     
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
     
    def to_dict(self):
        dict = model_to_dict(self)
        return dict
 
    def to_dict_api(self):
        dict = model_to_dict(self, exclude=[])
        return dict
 
    def __str__(self):
        return self.index

    def __unicode__(self):
        return u'%s' % (self.index)

    class Meta:
        verbose_name = '2.0 - Quran Text'
        verbose_name_plural = "2.0 - Quran Text"
        
        
class QuranTranslation(models.Model):
    language =  models.CharField(max_length=45)
    name =  models.CharField(max_length=255)
    translator =  models.CharField(max_length=255)
    language_flag_img = models.FileField(upload_to=language_flag_image)
    translation_file = models.FileField(upload_to=translation_file, help_text='Required : One aya translation per line in format "sura|aya|translation" and file must have all 6236 aya included')
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
     
    def to_dict(self):
        dict = model_to_dict(self)
        return dict
 
    def to_dict_api(self):
        dict = model_to_dict(self, exclude=['language_flag_img', 'translation_file'])
        dict['language_flag_img'] = media_url + self.language_flag_img.url
        return dict
 
    def __str__(self):
        return self.language + ' - ' + self.name

    def __unicode__(self):
        return u'%s - %s' % (self.language, self.name)

    class Meta:
        verbose_name = '3.0 - Quran Translation'
        verbose_name_plural = "3.0 - Quran Translation"


class QuranTranslationText(models.Model):
    tranlation = models.ForeignKey(QuranTranslation)
    sura = models.IntegerField()
    aya = models.IntegerField()
    text = models.TextField()
     
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
     
    def to_dict(self):
        dict = model_to_dict(self)
        return dict
 
    def to_dict_api(self):
        dict = model_to_dict(self, exclude=[])
        return dict
 
    def __str__(self):
        return self.tranlation.language + ' - ' + self.tranlation.name

    def __unicode__(self):
        return u'%s - %s' % (self.tranlation.language, self.tranlation.name)

    class Meta:
        verbose_name = '3.1 - Quran Translation Text'
        verbose_name_plural = "3.1 - Quran Translation Text"
        
        
class RecitationVerseByVerse(models.Model):
    index = models.IntegerField(primary_key=True)
    language =  models.CharField(max_length=45)
    translator =  models.CharField(max_length=255)
    quality_Kbps = models.IntegerField(help_text='Interger Value, eg: for 64 Kbps just enter 64')
     
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
     
    def to_dict(self):
        dict = model_to_dict(self)
        return dict
 
    def to_dict_api(self):
        dict = model_to_dict(self, exclude=[])
        dict['media_root'] = RECITATION_VERSE_BY_VERSE_ROOT + str(self.index) + '/'
        return dict
 
    def __str__(self):
        return self.language + ' - ' + self.translator

    def __unicode__(self):
        return u'%s - %s' % (self.language, self.translator)

    class Meta:
        verbose_name = '4.0- Quran Recitation Verse-By-Verse'
        verbose_name_plural = "4.0- Quran Recitation Verse-By-Verse"
        
        
class RecitationPageByPage(models.Model):
    index = models.IntegerField(primary_key=True)
    language =  models.CharField(max_length=45)
    translator =  models.CharField(max_length=255)
    quality_Kbps = models.IntegerField(help_text='Interger Value, eg: for 64 Kbps just enter 64')
     
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
     
    def to_dict(self):
        dict = model_to_dict(self)
        return dict
 
    def to_dict_api(self):
        dict = model_to_dict(self, exclude=[])
        dict['media_root'] = RECITATION_PAGE_BY_PAGE_ROOT + str(self.index) + '/'
        return dict
 
    def __str__(self):
        return self.language + ' - ' + self.translator

    def __unicode__(self):
        return u'%s - %s' % (self.language, self.translator)

    class Meta:
        verbose_name = '4.1- Quran Recitation Page-By-Page'
        verbose_name_plural = "4.1- Quran Recitation Page-By-Page"

    
