from functools import wraps

from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from courses.models import Course


def course_enrollment_check(test_func):
    """
    Checks if the user is enrolled in the requested course.
    Code based on the native 'user_passes_test' django decorator.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            pk = kwargs["pk"]
            course_object = get_object_or_404(Course, pk=pk)
            user = request.user

            if user not in course_object.students.all():
                raise PermissionDenied("Access denied. User not enrolled in course.")
            else:
                return view_func(request, *args, **kwargs)
            # if test_func(request.user):
            #     return view_func(request, *args, **kwargs)
            # path = request.build_absolute_uri()
            # resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
            # # If the login url is the same scheme and net location then just
            # # use the path as the "next" url.
            # login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            # current_scheme, current_netloc = urlparse(path)[:2]
            # if (not login_scheme or login_scheme == current_scheme) and (
            #     not login_netloc or login_netloc == current_netloc
            # ):
            #     path = request.get_full_path()
            # from django.contrib.auth.views import redirect_to_login

            # return redirect_to_login(path, resolved_login_url, redirect_field_name)

        return _wrapped_view

    return decorator
    # if user not in course.students.all():
    #     return PermissionDenied("Access denied!")
    # else return
    # return user in course.students.all()


# def subject_test(f, subject):
#     def test_user_for_subject(request, subject, *args, **kwargs):
#         if not UserSubject.objects.filter(user=request.user, subject=subject).exists():
#             retun HttpResponseForbidden('Access denied!')
#         else:
#             return f(request, *args, **kwargs)
#     return test_user_for_subject
