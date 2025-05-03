import subprocess
import shlex

def greet(name):
    print(f"Hello, {name}!")

def run_command(cmd):
    # Memecah string command menjadi list argumen yang aman
    safe_cmd = shlex.split(cmd)
    # Menjalankan command tanpa shell=True untuk menghindari command injection
    subprocess.call(safe_cmd)

if __name__ == "__main__":
    name = input("Enter your name: ")
    greet(name)

    cmd = input("Enter a command to run: ")
    run_command(cmd)





