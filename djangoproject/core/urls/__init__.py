from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView
from django.conf import settings

urlpatterns = patterns('core.views.main_views',
    url(r'^$', 'home'),
    url(r'^admail/$', 'admail'),
    url(r'^mailtest/$', 'mailtest'),
    url(r'^about/$', RedirectView.as_view(url='http://blog.freedomsponsors.org/about/')),
    url(r'^dev/$', RedirectView.as_view(url='http://blog.freedomsponsors.org/developers/')),
)

# 301 redirects
urlpatterns += patterns('',
    url(r'^home/$',    RedirectView.as_view(url='/',         permanent=True)),
    url(r'^faq$',      RedirectView.as_view(url='/faq',      permanent=True)),
    url(r'^jslic$',    RedirectView.as_view(url='/jslic',    permanent=True)),
    url(r'^stats$',    RedirectView.as_view(url='/stats',    permanent=True)),
    url(r'^feedback$', RedirectView.as_view(url='/feedback', permanent=True)),

    url(r'^issue/$',              RedirectView.as_view(url='/search/',        permanent=True, query_string=True)),
    url(r'^issue/(?P<temp>.*)$',  RedirectView.as_view(url='/issue/%(temp)s', permanent=True, query_string=True)),

    url(r'^project/$',                         RedirectView.as_view(url='/project/', permanent=True)),
    url(r'^project/(?P<project_id>\d+)/$',     RedirectView.as_view(url='/project/%(project_id)s/', permanent=True)),
    url(r'^project/(?P<project_id>\d+)/edit$', RedirectView.as_view(url='/project/%(project_id)s/edit', permanent=True)),

    url(r'^user/$',                                   RedirectView.as_view(url='/user/', permanent=True)),
    url(r'^user/(?P<user_id>\d+)/$',                  RedirectView.as_view(url='/user/%(user_id)s/', permanent=True)),
    url(r'^user/(?P<user_id>\d+)/(?P<user_slug>.*)$', RedirectView.as_view(url='/user/%(user_id)s/%(user_slug)s', permanent=True)),
)

urlpatterns += patterns('core.views.paypal_views',
    url(r'^paypal/cancel$', 'paypalCancel'),
    url(r'^paypal/return$', 'paypalReturn'),
    url(r'^paypal/'+settings.PAYPAL_IPNNOTIFY_URL_TOKEN+'$', 'paypalIPN'),
)

urlpatterns += patterns('core.views.bitcoin_views',
    url(r'^bitcoin/'+settings.BITCOIN_IPNNOTIFY_URL_TOKEN+'$', 'bitcoinIPN'),
)

urlpatterns += patterns('core.views.json_views',
    url(r'^json/project$', 'project'),
    url(r'^json/by_issue_url$', 'by_issue_url'),
    url(r'^json/get_offers$', 'get_offers'),
    url(r'^json/list_issue_cards', 'list_issue_cards'),
    url(r'^json/add_tag', 'add_tag'),
    url(r'^json/remove_tag', 'remove_tag'),
    url(r'^json/latest_activity', 'latest_activity'),
    url(r'^json/toggle_watch', 'toggle_watch'),
    url(r'^json/check_username_availability/(?P<username>.+)', 'check_username_availability'),
)
