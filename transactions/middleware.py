from datetime import datetime
from django.contrib import messages

class CheckSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if session is set
        if not request.session.get('financial_year'):
            today = datetime.today()
            if today.month >= 4:  # April to December
                start_year = today.year
                end_year = today.year + 1
            else:  # January to March
                start_year = today.year - 1
                end_year = today.year
            financial_year = str(start_year) + '-' + str(end_year)
            request.session['financial_year'] = financial_year
            messages.warning(request, 'Financial year set to current by default')
        
        response = self.get_response(request)
        return response
