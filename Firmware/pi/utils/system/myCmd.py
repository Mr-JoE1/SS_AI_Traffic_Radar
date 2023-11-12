import subprocess






# command = "ls -l"  

        # print("Standard Output:")
        # print(completed_process.stdout)
        
        # # Print the command's standard error
        # print("\nStandard Error:")
        # print(completed_process.stderr)
        
        # # Print the return code (0 means success)
        # print("\nReturn Code:", completed_process.returncode)



def Exec(command):
    try:
        completed_process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return completed_process
    except subprocess.SubprocessError as e:
        print(str(e))
        return str(e)


