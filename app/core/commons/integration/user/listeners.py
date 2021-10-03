from app.core.applications.auth.core.handlers import AuthHandler
from app.core.commons.integration.user.events import RegisterUserEvent, UpdateUserEvent


class RegisterUserCompany:
    def __init__(self):
        pass

    def handler(self, register_company):
        """
        register in module auth
        """
        form_data = dict(
            email=register_company.company.email,
            hashed_password=register_company.company.auth.get(
                'hashed_password')
        )
        AuthHandler.register(form_data, False)


class RegisterUserListener:
    def __init__(self):
        pass

    def handler(self, register_user: RegisterUserEvent):
        """
        register in module auth
        """
        form_data = dict(
            email=register_user.user.email,
            hashed_password=register_user.user.auth.get('hashed_password')
        )
        AuthHandler.register(form_data, False)


class UpdateUserListener:
    def __init__(self):
        pass

    def handler(self, register_user: UpdateUserEvent):
        """
        register in module auth
        """
        form_data = dict(
            email=register_user.user.email,
            hashed_password=register_user.user.auth.get('hashed_password')
        )
        AuthHandler.register(form_data, False)
