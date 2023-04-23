import importlib

class installer():
    def __init__(self):
        packages = ["numpy", "PyQt5", "matplotlib"]
        for i in packages:
            self.install(i)
    
    def install(self, package):
        try:
            importlib.import_module(package)
        except ImportError:
            import subprocess
            print("Installing " + package + "...")
            subprocess.check_call(["pip", "install", package])
