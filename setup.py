import os
import json
from setuptools import setup, find_packages
from setuptools.command.install import install as _install


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))


def read_pip_dependencies(fname):
    lockfile = open_file(fname)
    lockjson = json.load(lockfile)
    return [dependency for dependency in lockjson.get('default')]


class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()


if __name__ == '__main__':
    setup(
        name='training_sklearn',
        version='1.0.dev0',
        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        description='A generic training_sklearn.',
        install_requires=read_pip_dependencies('Pipfile.lock'),
        license='MIT',
    )
