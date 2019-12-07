from django.conf.urls import url
from ussd.views import MermaidText, ValidateJourney, AfricasTalkingUssdGateway

app_name = 'ussd'
urlpatterns = [
    url(r'mermaid_text$', MermaidText.as_view(), name="mermaid_text"),
    url(r'validate_journey$', ValidateJourney.as_view()),
    url(r'africans$', AfricasTalkingUssdGateway.as_view())
]
