class ResponseFormat:
    @staticmethod
    def format(status=True, code=200, data=None):
        return status, code, data
