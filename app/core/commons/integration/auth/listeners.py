class RegisterUser:
    def __init__(self):
        pass

    def handler(self, register_auth):
        print(register_auth.name)

class RegisterUserSendEmail:
    def __init__(self):
        pass

    def handler(self, register_auth):
        print("Ahora envias un email")