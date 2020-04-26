class ApiException(Exception):
    def __init__(self, message='There is something wrong, please try latter', status_code=422, *args, **kwargs):
        self.message = message
        self.status_code = status_code
        super().__init__(*args, **kwargs)



class LastValidTimestampNotFoundException(Exception):
    pass

class RemarkNotFoundException(Exception):
    pass

class ReportNotFoundException(Exception):
    pass
