from src.logger import logging
import sys

def build_err_msg(err,err_info:sys):
    _,_,exc_tb = err_info.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno
    err_name = str(err)

    err_msg = (f"error occured in python script {filename}",
               f"at line no {lineno}"
               f"error name {err_name}")
    return err_msg

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.custom_error_message = build_err_msg(error_message,error_details)

    def __str__(self):
        return self.custom_error_message