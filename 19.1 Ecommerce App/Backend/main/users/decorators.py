from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def group_required(Admin):
    def in_group(user):
        if user.is_authenticated:
            return user.groups.filter(name=Admin).exists() or user.is_superuser
        return False

    return user_passes_test(in_group, login_url='/login/', redirect_field_name=None)