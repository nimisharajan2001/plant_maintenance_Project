
from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static, serve
from app import views



urlpatterns = [
    re_path('admin/', admin.site.urls),
    
    re_path(r'^$', views.login, name='login'),
    re_path(r'^reg$', views.reg, name='reg'),
    re_path(r'^registration$', views.registration, name='registration'),
    re_path(r'^pwd$', views.pwd, name='pwd'),
    re_path(r'^reset_password$', views.reset_password, name='reset_password'),

    #-----------------client--------------------
    re_path(r'^index$', views.index, name='index'),
    re_path(r'^about$', views.about, name='about'),
    re_path(r'^services$', views.services, name='services'),
    re_path(r'^portfolio$', views.portfolio, name='portfolio'),
    re_path(r'^request$', views.request, name='request'),
    re_path(r'^contact$', views.contact, name='contact'),
    re_path(r'^addreq$', views.addreq, name='addreq'),
    re_path(r'^reqsave$', views.reqsave, name='reqsave'),
    re_path(r'^sort$', views.sort, name='sort'),
    re_path(r'^show$', views.show, name='show'),
    re_path(r'^staff$', views.staff, name='staff'),
    
    #-----------------Owner Module--------------------
    re_path(r'^owner_dashboard$', views.owner_dashboard, name='owner_dashboard'),
    re_path(r'^owner_addperson$', views.owner_addperson, name='owner_addperson'),
    re_path(r'^owner_allotworkorder$', views.owner_allotworkorder, name='owner_allotworkorder'),
    re_path(r'^owner_addvendors$', views.owner_addvendors, name='owner_addvendors'),
    re_path(r'^owner_purchaseorder$', views.owner_purchaseorder, name='owner_purchaseorder'),
    re_path(r'^owner_vendorsnewpayment$', views.owner_vendorsnewpayment, name='owner_vendorsnewpayment'),
    re_path(r'^owner_salesorder$', views.owner_salesorder, name='owner_salesorder'),
    re_path(r'^owner_reports$', views.owner_reports, name='owner_reports'),
    
    #-----------------Maintenance Committee--------------------
    re_path(r'^committee_viewworkorder$', views.committee_viewworkorder, name='committee_viewworkorder'),
    re_path(r'^committe_acceptwork/(?P<id>\d+)/$', views.committe_acceptwork,
                  name='committe_acceptwork'),
    re_path(r'^committe_rejectwork/(?P<id>\d+)/$', views.committe_rejectwork,
                  name='committe_rejectwork'),
    re_path(r'^committee_stockdetails$', views.committee_stockdetails, name='committee_stockdetails'),
    re_path(r'^committee_updatestockdetails/(?P<id>\d+)$', views.committee_updatestockdetails, name='committee_updatestockdetails'),
    re_path(r'^committee_updateworkstatus$', views.committee_updateworkstatus, name='committee_updateworkstatus'),
    re_path(r'^committee_packingdetails$', views.committee_packingdetails, name='committee_packingdetails'),
    re_path(r'^committee_repairingdetails$', views.committee_repairingdetails, name='committee_repairingdetails'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
