import functools
from django.shortcuts import redirect
from django.contrib import messages

def user_is_active(view_func, redirect_url="logout"):
    """
        this decorator ensures that a user is not logged in,
        if a user is logged in, the user will get redirected to 
        the url whose view name was passed to the redirect_url parameter
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_active:
            return view_func(request,*args, **kwargs)
        messages.info(request, "your account is deactived by admin")
        return redirect(redirect_url)
    return wrapper