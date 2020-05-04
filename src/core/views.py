from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import TeachingAssistantProfile
import xhtml2pdf.pisa as pisa


class PDFRenderView(View, LoginRequiredMixin):
    def get(self, request, month, year, program):
        tas = TeachingAssistantProfile.objects.filter(
            program=program, assignment__feedback__status=2,
            assignment__feedback__date_approved__month=month,
            assignment__feedback__date_approved__year=year).distinct()
        program = tas[0].get_program_display if tas else None
        now = datetime.now()
        params = {
            'tas': tas,
            'now': now,
            'department': "Electrical Engineering",
            'program': program
        }
        return self.render('pdf.html', params)

    @staticmethod
    def render(template_path, params):
        template = get_template(template_path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        return HttpResponse(response.getvalue(), content_type='application/pdf') if not pdf.err else HttpResponse(
            "Error Rendering PDF", status_code=422)
