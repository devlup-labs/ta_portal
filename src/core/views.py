from django.views.generic import View
import datetime
from .render import Render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from core.models import Feedback


@method_decorator(staff_member_required, name='dispatch')
class Pdf(View, LoginRequiredMixin):

    def get(self, request, program):
        date = datetime.datetime.now().strftime("%d")
        month = datetime.datetime.now().strftime("%b")
        year = datetime.datetime.now().strftime("%Y")
        feedbacks = Feedback.objects.filter(date_submitted__month=datetime.date.today().month,
                                            status=2,
                                            assignment__teaching_assistant__program=program)
        program = feedbacks[0].assignment.teaching_assistant.get_program_display \
            if feedbacks else ""
        params = {
            'feedbacks': feedbacks,
            'date': date,
            'month': month,
            'year': year,
            'department': "Electrical Engineering",
            'program': program
        }
        return Render.render('pdf.html', params)
