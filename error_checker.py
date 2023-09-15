import subprocess
import stack_overflow_api

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
    
if __name__ == "__main__":
    file_name = input(f"Enter the file name containing your Python code: \n")
    try:
        with open(file_name, "r") as code_file:
            user_code = code_file.read()
    
        result = execute_python_code(file_name)

        if result["success"]:
            print("No errors")
            print(f"Output: {user_code}")
        else:
            print("Error Type", result["error_type"])
            print("Error Message", result["error_message"])
            stack_overflow_api.search_stackoverflow(result["error_type"], result["error_message"])

    except FileNotFoundError:
        print(f"File {file_name} was not found")
    except Exception as err:
        print("Error", err)

