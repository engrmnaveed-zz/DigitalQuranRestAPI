__author__ = 'Naveed'

from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('digital_QURAN.views',
    url(r'^get_meta_data$'              , 'get_meta_data_quran_api'      , name='get_meta_data_quran_api'),
    url(r'^get_quran_text/([^/]+)$'             , 'get_quran_text_quran_api_1'      , name='get_quran_text_quran_api_1'),
    url(r'^get_quran_text/([^/]+)/([^/]+)$'             , 'get_quran_text_quran_api_2'      , name='get_quran_text_quran_api_2'),
    url(r'^get_translations$'           , 'get_translations_quran_api'      , name='get_translations_quran_api'),
    url(r'^get_translation_text/([^/]+)/([^/]+)$'       , 'get_translation_text_quran_api_1'      , name='get_translation_text_quran_api_1'),
    url(r'^get_translation_text/([^/]+)/([^/]+)/([^/]+)$'       , 'get_translation_text_quran_api_2'      , name='get_translation_text_quran_api_2'),
    url(r'^get_recitations_verse$'            , 'get_recitations_verse_quran_api'      , name='get_recitations_quran_api'),
    url(r'^get_recitations_page$'       , 'get_recitations_page_quran_api'      , name='get_recitation_track_quran_api'),
)