from __future__ import unicode_literals
import requests
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)
from django.shortcuts import get_object_or_404

from .provider import Office365Provider


class OfficeOAuth2Adapter(OAuth2Adapter):
    provider_id = Office365Provider.id

    def __init__(self, request):
        super(OfficeOAuth2Adapter, self).__init__(request)

        """
        ***Get the configuration domain in your office365 App***

        if you have saved settings about Office 365 app in DataBase use this line
        --tenant = self.get_tenant() or 'common'

        if you have saved the settings in the Office 365 app in the config file
        --provider = self.get_provider()
        --tenant = provider.get_settings().get('tenant') or 'common'
        """
        
         # for this example
        provider = self.get_provider()
        tenant = provider.get_settings().get('tenant') or 'common'

        base_url = 'https://login.microsoftonline.com/{0}'.format(tenant)
        self.access_token_url = '{0}/oauth2/v2.0/token'.format(base_url)
        self.authorize_url = '{0}/oauth2/v2.0/authorize'.format(base_url)
        self.profile_url = 'https://graph.microsoft.com/v1.0/me/'

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)

    @staticmethod
    def get_tenant():
        """
        Get settings about Office 365 app in DataBase and retunr your Domain
        # Setting Model
        config_object = get_object_or_404(GeneralConfigurations) 
        return: config_object.token_office_365
        """
        pass

oauth2_login = OAuth2LoginView.adapter_view(OfficeOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(OfficeOAuth2Adapter)
