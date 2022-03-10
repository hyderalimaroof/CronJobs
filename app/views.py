from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from .tasks import mail

from .models import Student


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@api_view(['GET'])
def student(request):

    return HttpResponse(Student.objects.all())


def AddStudent(request):
    student = Student.objects.create(
        first_name='hyder',
        last_name="ali maroof",
        email='hyder@gmail.com',
        password='hyder',
        gander='Male'
    )
    return Response(student)


@api_view(['GET'])
def student_in_cache(request):
    if 'student' in cache:
        students = cache.get('student')
        return Response(
            students,
            status=status.HTTP_201_CREATED
        )

    else:
        students = Student.objects.all()
        cache.set(
            student, students,
            timeout=CACHE_TTL
        )
        return HttpResponse(
            students,
            status=status.HTTP_201_CREATED
        )


def send_email(request):
    try:
        mail()
        return JsonResponse({
            'message': 'email send successfully'
        },
            status=status.HTTP_200_OK
        )
    except:
        return Response({
            'message': 'something went wrong'
        },
            status=status.HTTP_400_BAD_REQUEST
        )
