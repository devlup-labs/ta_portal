from django.views.generic import View
import datetime
from .render import Render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from core.models import Feedback


@method_decorator(staff_member_required, name='dispatch')
class Pdf(View, LoginRequiredMixin):

    def get(self, request):
        date = datetime.datetime.now().strftime("%d")
        month = datetime.datetime.now().strftime("%b")
        year = datetime.datetime.now().strftime("%Y")
        feedbacks = Feedback.objects.filter(date_submitted__month=datetime.date.today().month)
        params = {
            'feedbacks': feedbacks,
            'date': date,
            'month': month,
            'year': year,
            'department': "Electrical Engineering",
            'program': "M.Tech"
        }
        return Render.render('pdf.html', params)
