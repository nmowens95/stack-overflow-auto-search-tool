import subprocess
import search_tool.stack_overflow_api as stack_overflow_api

class ErrorChecker():
# Create a wrapper script
    def execute_python_code(user_code):
        try:  
            process = subprocess.Popen(
                ["python", "-c", user_code],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True # make sure output is in text format
            )
            stdout, stderr = process.communicate()

            if process.returncode != 0:
                return {
                    "success": False,
                    "error_type": "RunetimeError",
                    "error_message": stderr.strip()
                }
            else:
                return {
                    "success": True,
                    "error_message": stdout.strip()
                }
        except Exception as err:
            return {
                "success": False,
                "error_type": "Exception",
                "error_message": str(err)
            }