from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name='Agenda',
    version='0.0.1',
    author='Santiago Andini',
    author_email='Santiagoandini2@gmail.com',
    license='<the license you chose>',
    description='<short description for the tool>',
    url='<github url where the tool code will remain>',
    py_modules=['controlador','modelo','validacion','vista'],
    package_dir={'': 'app'},
    packages=[''],
    install_requires=[requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        agenda=app.controlador:main
    '''
)
