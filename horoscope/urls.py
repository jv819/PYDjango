from django.urls import path
from . import views as views_horoscope


urlpatterns = [
    path('aries/', views_horoscope.aries),
    path('taurus/', views_horoscope.taurus),
    path('gemini/', views_horoscope.gemini),
    path('cancer/', views_horoscope.cancer),
    path('leo/', views_horoscope.leo),
    path('virgo/', views_horoscope.virgo),
    path('libra/', views_horoscope.libra),
    path('scorpion/', views_horoscope.scorpion),
    path('sagittarius/', views_horoscope.sagittarius),
    path('capricorn/', views_horoscope.capricorn),
    path('aquarius/', views_horoscope.aquarius),
    path('pisces/', views_horoscope.pisces),
]
