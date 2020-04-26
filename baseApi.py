import traceback
from flask import jsonify
from werkzeug.exceptions import HTTPException
from exceptions import ApiException
from flask_restful import Api

def handle_api_error(error):
    '''This method handles API error'''
    return jsonify({'error':True, 'message':error.message}), error.status_code

def handle_500_error():
    return jsonify({'error':True, 'message':'There is something wrong, please try latter'}), 500

class baseApi(Api):
    def error_router(self, original_handler, e):
        '''Override original error_router to hndle only HTTPExceptions'''
        from api import app
        app.logger.error(traceback.print_exc())
        if self._has_fr_route() and isinstance(e, ApiException):
            try:
                return handle_api_error(e)
            except Exception:
                return handle_500_error()
        elif isinstance(e, HTTPException):
            return super().error_router(original_handler, e)
        else:
            return handle_500_error()
