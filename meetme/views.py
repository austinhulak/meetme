from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from meetme.models import Account, Category, Reservation


def category(request, category_id):
    pass


@login_required
def main(request):
    context = {
        'categories': Category.objects.all(),
    }

    return render_to_response('meetme/main.html',
                              context,
                              context_instance=RequestContext(request))

@login_required
def profile(request, profile_id):

    context = {}

    return render_to_response('meetme/profile.html',
                                context, context_instance=RequestContext(request))


def login(request):
    context = {}

    return render_to_response('meetme/login.html',
                              context,
                              context_instance=RequestContext(request))


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('main'))


def privacy(request):
    return render_to_response('meetme/terms.html')


def make_request(request):
    if request.method != 'POST':
        raise Exception('not post!')

    account_id = request.POST['account_id']

    visitor = request.user
    local = Account.objects.get(pk=account_id)
    day = 1
    time_range = 1

    reservation = Reservation.objects.create(
        local=local,
        visitor=visitor,
        day=day,
        time_range=time_range
    )

    return HttpResponse('ok')


def support(request):
    return render_to_response('meetme/terms.html')


def terms(request):
    return render_to_response('meetme/terms.html')
