from stack_overflow_api import Search

class ErrorSpecific():
    error_message = input(f"Enter error message: \n")
    error_type = input(f"Enter error type: \n")

    Search.stack_overflow_api.search_stackoverflow(error_type, error_message)