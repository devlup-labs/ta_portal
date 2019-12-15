from django.views.generic import View
import datetime
from .render import Render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from core.models import Feedback
from accounts.models import TeachingAssistantProfile


@method_decorator(staff_member_required, name='dispatch')
class Pdf(View, LoginRequiredMixin):

    def get(self, request, mon, yr, program):
        date = datetime.datetime.now().strftime("%d")
        month = datetime.date(yr, mon, 1).strftime('%b')
        tas = TeachingAssistantProfile.objects.filter(
            program=program, assignment__feedback__status=2,
            assignment__feedback__date_approved__month=mon,
            assignment__feedback__date_approved__year=yr).distinct()
        program = tas[0].get_program_display if tas else None
        params = {
            'tas': tas,
            'date': date,
            'month': month,
            'year': yr,
            'department': "Electrical Engineering",
            'program': program
        }
        return Render.render('pdf.html', params)
