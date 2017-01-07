from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
 
# Create your views here.
def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view FBV
    #print(request.user)
    #print(request.user.is_authenticated())\
	obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return HttpResponse("hello {sc}".format(sc=obj.url))

class KirrCBView(View): #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponse("hello again {sc}".format(sc=shortcode))

	def post(self, request, *args, **kwargs):
        return HttpResponse()


