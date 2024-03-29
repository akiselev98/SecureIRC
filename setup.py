from setuptools import setup

setup(
    name='SecureIRC',
    packages=['secureirc'],
    include_package_data=True,
    install_requires=[
        'flask', 'flask_socketio', 'flask_session', 'flask_login', 'flask_migrate', 'flask_sqlalchemy', 'flask_sslify'
    ],
)
