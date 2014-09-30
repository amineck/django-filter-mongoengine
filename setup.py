from setuptools import setup, find_packages

f = open('README.rst')
readme = f.read()
f.close()

setup(
    name='django-filter-mongoengine',
    version='0.1',
    description=('Django-filter-mongoengine is a reusable Django application inspired from django-filter for allowing'
                 ' mongoengine users to filter querysets dynamically.'),
    long_description=readme,
    author='Amine Chouki',
    author_email='surfeurX@gmail.com',
    url='https://github.com/surfeurX/django-filter-mongoengine/tree/master',
    packages=find_packages(exclude=['tests']),
    package_data = {
        'django_filters_mongoengine': [
            'locale/*/LC_MESSAGES/*',
        ],
    },
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
