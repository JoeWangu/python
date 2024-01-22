from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        # user = get_user_model()
        # try:
        #     user = user.objects.get(email=email)
        #     if user.check_password(password):
        #         return user
        # except user.DoesNotExist:
        #     return None
        usermodel = get_user_model()
        if email is None:
            email = kwargs.get(usermodel.EMAIL_FIELD)
        if email is None or password is None:
            return
        try:
            user = usermodel.objects.get(email=email)
        except usermodel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            usermodel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
