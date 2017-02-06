import uuid

from django.utils.crypto import get_random_string
from open_facebook import OpenFacebook
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer

from .models import *
from rest_framework.authtoken.models import Token

AUTH_TOKEN = ""
graph = OpenFacebook(AUTH_TOKEN)


class UserSerializer(DocumentSerializer):
    user = graph.get('me')

    f_name = user['first_name']
    l_name = user['last_name']
    email = user['email']
    dob = user['birthday']
    gender = user['gender']
    city_home = user['hometown']['name']
    city_current = user['location']['name']
    p_link = user['link']
    f_id = str(user['id'])

    try:
        existing_user = User.objects.get(fb_id=f_id)
    except User.DoesNotExist:
        new_user = User(first_name=f_name,
                        last_name=l_name,
                        email_id=email,
                        date_of_birth=dob,
                        gender=gender,
                        hometown=city_home,
                        current_location=city_current,
                        fb_id=f_id,
                        profile_link=p_link)
        new_user.save()

        class Meta:
            model = User
            fields = ('first_name', 'last_name', 'email_id', 'date_of_birth', 'gender',
                      'hometown', 'current_location', 'fb_id', 'profile_link', 'created_date',
                      'update_date')
