import subprocess

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
                "error_message": stderr.strip()
            }
    except Exception as err:
        return {
            "success": False,
            "error_type": "Exception",
            "error_message": str(err)
        }
    
if __name__ == "__main__":
    user_code = input(f"Enter your Python code: \n")
    result = execute_python_code(user_code)

    if result["success"]:
        print("No errors")
        print(f"Output: {user_code}")
    else:
        print("Error Type", result["error_type"])
        print("Error Message", result["error_message"])

    if not result["success"]:
        import stack_overflow_api
        stack_overflow_api.search_stackoverflow(result["error_message"], result["error_type"])
