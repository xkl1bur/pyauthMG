<!-- markdownlint-disable MD002 MD041 -->
## Implement sign-in

1. Add the following `config` statements to the top of **settings.py**.

    ```python
    INSTALLED_APPS = [
      ...

      # Allauth Lib
      'allauth',
      'allauth.account',
      'allauth.socialaccount',

      # Your provider
      'auth.providers.office365',
      ...
    ]
    ```

    ```python
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    )
    ```

    ```python
    SITE_ID = 1

    # ALLAUTH CONFIG
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
    ACCOUNT_EMAIL_VERIFICATION = 'none'
    ```

1. Open **urls.py** and add a new `path` for the `accounts` view with the following.

    ```python
    from django.urls import path, include

    path('accounts/', include('allauth.urls')),
    ```
