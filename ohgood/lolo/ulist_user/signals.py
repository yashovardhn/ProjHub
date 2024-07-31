from django.db.models.signals import post_save,post_delete
from django.contrib.auth.models import User
from .models import Profile

def create_profile(sender, instance, created, **kwargs):
    print("*************profile_saved*******************")
    if created:
        user = instance
        Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name= user.first_name,
            )

def update_user(sender, instance, created, **kwargs):
    profile= instance
    user = profile.user
    if created == False:
        user.username = profile.username
        user.email = profile.email
        user.first_name = profile.name
        user.save()

# @receiver(post_delete, sender=Profile)
def profile_deleted(sender, instance, **kwargs):
    try:
        print("*******************************profile_deleted**********************************")
        user = instance.user
        user.delete()
    except User.DoesNotExist:
        pass

post_save.connect(update_user, sender = Profile)
post_save.connect(create_profile, sender=User)
post_delete.connect(profile_deleted, sender=Profile)



# post_save.connect(profile_updated, sender=Profile)
# @receiver(post_save, sender=Profile)
# def profile_updated(sender, instance, created, **kwargs):
#     print("*************profile_saved*******************")
#     print('instance: ', instance)
#     print('created: ', created)