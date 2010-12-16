from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from tms.views import TmsNyxAuth


urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'tms/login.html'}, name='login'),
)

urlpatterns += patterns('tms.views',
    url(r'^$', 'index', name='index'),
    url(r'^reg/$', 'registration', name='registration'),
    url(r'^logout/$', 'logout', name='logout'),
    (r'^nyxauth/', include(TmsNyxAuth().urls(), namespace='nyxauth')),
    url(r'^irc/$', direct_to_template, {'template': 'tms/irc.html'}, name='irc'),
    url(r'^(?P<slug>[\w_-]+)/$', 'tournament', name='tournament'),
    url(r'^(?P<slug>[\w_-]+)/players/$', 'tournament_players', name='tournament_players'),
    url(r'^(?P<slug>[\w_-]+)/rounds/$', 'tournament_rounds', name='tournament_rounds'),
    url(r'^(?P<slug>[\w_-]+)/round/(?P<id>\d+)/$', 'tournament_round', name='tournament_round'),
    url(r'^(?P<slug>[\w_-]+)/report/$', 'result_report', name='result_report'),
    url(r'^(?P<slug>[\w_-]+)/join/$', 'join_tournament', name='join_tournament'),
    url(r'^(?P<slug>[\w_-]+)/leave/$', 'leave_tournament', name='leave_tournament'),
    url(r'^player/(?P<username>[\w_@-]+)/$', 'player_profile', name='player_profile'),
    url(r'^match/(?P<id>\d+)/replays/$', 'match_replays', name='match_replays'),
    url(r'^match/(?P<id>\d+)/replays/upload/$', 'upload_replay', name='upload_replay'),
)
