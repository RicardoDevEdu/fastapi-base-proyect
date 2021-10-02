from app.core.applications.auth.core.handlers import AuthHandler

class RegisterUserCompany:
    def __init__(self):
        pass

    def handler(self, register_company):
        """
        register in module auth
        """
        form_data = dict(
            email = register_company.company.email,
            hashed_password = register_company.company.auth.get('hashed_password')
        )
        AuthHandler.register(form_data)

