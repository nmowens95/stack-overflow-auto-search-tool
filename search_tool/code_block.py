from error_checker import ErrorChecker
from stack_overflow_api import Search

class CodeBlock():
    code_block = input(f"Paste code block here: \n")

    def code_block_check(code):
        try:
            result = ErrorChecker.execute_python_code(code)

            if result["success"]:
                print("No errors")
                print(f"Output: {code}")
            else:
                print("Error Type", result["error_type"])
                print("Error Message", result["error_message"])
                Search.stack_overflow_api.search_stackoverflow(result["error_type"], result["error_message"])

        except Exception as err:
            print("Error", err)