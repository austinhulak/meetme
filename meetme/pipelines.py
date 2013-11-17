from urllib2 import urlopen

from social_auth.backends.facebook import FacebookBackend


def get_user_avatar(backend, details, response, social_user, uid, user, *args, **kwargs):
    url = None
    if backend.__class__ == FacebookBackend:
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']

    user.image_url = url
    user.save()

    #if url:
    #    profile = user.get_profile()
    #    avatar = urlopen(url).read()
    #    fout = open(filepath, "wb")  # filepath is where to save the image
    #    fout.write(avatar)
    #    fout.close()
    #    profile.photo = url_to_image  # depends on where you saved it
    #    profile.save()
