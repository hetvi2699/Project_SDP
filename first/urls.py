from first.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path  


urlpatterns=[

			url('login',login),
			url('new_registration1',new_registration1),
			url('new_registration2',new_registration2),
			url('new_registration3',new_registration3),
			url('examreq',examreq),
			#url('exam',examRes),
			url('exam',exam_start),
			#url('display',display),
			url('exampro',exampro),
			url('certificate',certificate),
			url('new_certificate',new_certificate),
			url('new_registration4',new_registration4),
			url('auth_view',auth_view),
			url('registration1',registration1),
			url('registration2',registration2),
			url('registration3',registration3),
			url('registration4',registration4),
			url('payment',payment),
			url('welcome',welcome),
			url('logout',logout),
			url('download_pdf', download_pdf),	
			url('certi',certi),
			url('paymenterror',paymenterror),
			url('examcompleted',examcompleted),
			#url('Demo',Demo),
			url('addque',addque),
			url(r'^enterque/$',enterque),
			path('edit/<int:id>',edit),  
    		path('update/<int:id>',update),  
    		path('delete/<int:id>',destroy),  
			url('show',show),
			url('frgtpwd',frgtpwd),
			url('contactus',contactus),
]


