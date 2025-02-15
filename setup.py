
# setup.py
from setuptools import setup
from setuptools.command.install import install
import subprocess

class CustomInstall(install):
    def run(self):
        # Kurulumdan önce çalışacak komut
        subprocess.run(["touch", "/tmp/rce-basarılı"])
        super().run()

setup(
    name="mypackage",
    version="0.1",
    cmdclass={"install": CustomInstall},
    packages=["mypackage"]
)