from __future__ import unicode_literals

from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class OfficeAccount(ProviderAccount):

    def to_str(self):
        name = self.account.extra_data.get('displayName')
        if name.strip() != '':
            return name
        return super(OfficeAccount, self).to_str()


class Office365Provider(OAuth2Provider):
    id = str('office365')
    name = 'Office 365'
    account_class = OfficeAccount

    def get_default_scope(self):
        """
        Doc on scopes available at
        https://developer.microsoft.com/en-us/graph/docs/concepts/permissions_reference
        """
        return ['User.Read']

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        email = data.get('mail') or data.get('userPrincipalName')
        return dict(email=email,
                    last_name=data.get('surname'),
                    first_name=data.get('givenName'))


provider_classes = [Office365Provider]
