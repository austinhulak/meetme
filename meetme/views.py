from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from meetme.forms import PhoneForm
from utils.time import get_available_times
from meetme.models import Account, Category, Reservation, Review
from utils.twillio import clean_phone_number


@login_required
def category(request, category_id):
    category = Category.objects.get(pk=category_id)

    context = {
        'category': category,
        'people':  Account.objects.filter(category=category, available=True).exclude(phone__isnull=True),
    }

    return render_to_response('meetme/category.html',
                              context,
                              context_instance=RequestContext(request))


@login_required
def main(request):
    categories = Category.objects.all()

    for item in categories:
        item.image_filename = '/static/images/{}.png'.format(item.name.lower())

    context = {
        'categories': categories,
    }

    if not request.user.phone:
        return HttpResponseRedirect(reverse('set_phone'))

    return render_to_response('meetme/main.html',
                              context,
                              context_instance=RequestContext(request))


@login_required
def set_phone(request):
    if request.method == 'POST':
        # clean the phone number before validating it
        post_data = request.POST.copy()
        post_data['phone'] = clean_phone_number(post_data['phone'])

        form = PhoneForm(post_data)
        if form.is_valid():
            request.user.phone = form.cleaned_data['phone']
            request.user.save()

            return HttpResponseRedirect(reverse('main'))
    else:
        form = PhoneForm()

    context = {
        'form': form
    }

    return render_to_response('meetme/set_phone.html',
                              context,
                              context_instance=RequestContext(request))


@login_required
def profile(request, profile_id):

    user = Account.objects.get(id=profile_id)
    reviews = Review.objects.filter(account=user)

    context = {
        'user': user,
        'reviews': reviews,
        'available_times': get_available_times(),
    }

    return render_to_response('meetme/profile.html',
                              context, context_instance=RequestContext(request))


def login(request):
    context = {}

    # when the user is already logged in go to the main page
    if request.user.id:
        return HttpResponseRedirect(reverse('main'))

    return render_to_response('meetme/login.html',
                              context,
                              context_instance=RequestContext(request))


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('main'))


def privacy(request):
    return render_to_response('meetme/terms.html')


def im_available(request):
    if request.method != 'POST':
        raise Exception('not post!')

    category_id = request.POST['category_id']

    request.user.available = True
    request.user.category = Category.objects.get(pk=category_id)
    request.user.save()

    return HttpResponse('ok')


def make_request(request):
    if request.method != 'POST':
        raise Exception('not post!')

    account_id = request.POST['account_id']
    time_range = request.POST['time_range']

    visitor = request.user
    local = Account.objects.get(pk=account_id)
    day = 1
    #time_range = 1

    reservation = Reservation.objects.create(
        local=local,
        visitor=visitor,
        day=day,
        time_range=time_range
    )

    return HttpResponseRedirect(reverse('show_reservation', args=(reservation.id,)))


def show_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    if request.method == "POST":
        reservation.local_response = request.POST['local_response']
	reservation.save()
	return HttpResponseRedirect(reverse('have_fun'))

    context = {
        'reservation': reservation,
    }

    return render_to_response('meetme/show_reservation.html',
                              context,
                              context_instance=RequestContext(request))


def have_fun(request):
    return render_to_response('meetme/have_fun.html')

def support(request):
    return render_to_response('meetme/terms.html')


def terms(request):
    return render_to_response('meetme/terms.html')
