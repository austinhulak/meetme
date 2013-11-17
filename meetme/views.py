from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def main(request):
    context = {}

    return render_to_response('meetme/main.html',
                              context,
                              context_instance=RequestContext(request))


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('main'))


def privacy(request):
    return render_to_response('meetme/terms.html')


def support(request):
    return render_to_response('meetme/terms.html')


def terms(request):
    return render_to_response('meetme/terms.html')
