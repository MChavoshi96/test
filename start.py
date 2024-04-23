def say_hello():
    print("Hello, world!")

def install_package():
    print("Installing package...")
    import subprocess
    # pip install git+https://github.com/your_username/your_project.git
    subprocess.run(["pip", "install", "git+https://github.com/MChavoshi96/test.git"])