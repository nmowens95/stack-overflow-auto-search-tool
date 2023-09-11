import subprocess

# Create a wrapper script
def python_code(user_code):
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