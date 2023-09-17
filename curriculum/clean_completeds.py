from .models import CourseCompleted
from django.utils import timezone
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)

def clean_completeds():
    course_completeds = CourseCompleted.objects.all()
    courses_cleaned = 0
    for course in course_completeds:
        if int((timezone.now() - course.date) / timedelta(days=1)) >= 365:
            course.delete()
            courses_cleaned += 1
    logger.debug(f'{courses_cleaned} courses were cleaned.')