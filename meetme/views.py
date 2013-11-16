from django.shortcuts import render_to_response


def main(request):
    context = {}

    return render_to_response('meetme/main.html', context)
