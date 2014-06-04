from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medicalrobots.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','mainapp.views.index', name="home_url"),
    url(r'^researchthemes/?','mainapp.views.research_themes', name="research_themes_url"),
    url(r'^researchthemes/(?P<id>\d+)/?','mainapp.views.research_theme', name="research_theme_url"),
    url(r'^objectives/?','mainapp.views.objectives', name="objectives_url"),
    url(r'^objectives/(?P<id>\d+)/?','mainapp.views.objective', name="objective_url"),
    url(r'^equipments/?','mainapp.views.equipments', name="equipments_url"),
    url(r'^equipments/(?P<id>\d+)/?','mainapp.views.equipment', name="equipment_url"),
    url(r'^people/?','mainapp.views.people', name="people_url"),
    url(r'^people/(?P<id>\d+)/?','mainapp.views.user_profile', name="user_profile_url"),
    url(r'^achievements/?','mainapp.views.achievements', name="achievements_url"),
    url(r'^achievements/(?P<id>\d+)/?','mainapp.views.achievement', name="achievement_url"),
    url(r'^contact/?','mainapp.views.contact', name="contact_url"),
    
)
