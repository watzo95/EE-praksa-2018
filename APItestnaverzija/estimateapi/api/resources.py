# api/resources.py

from tastypie.resources import ModelResource
from api.models import Survey
from tastypie.authorization import Authorization

class SurveyResource(ModelResource):
    class Meta:
        queryset = Survey.objects.all()
        resource_name = 'surv'
        authorization = Authorization()
        fields = ['trajanje', 'stroski', 'mail', 'ustvarjeno']
