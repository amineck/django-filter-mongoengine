Django Filter Monogoengine
===========================

Django-filter-mongoengine is a reusable Django application for allowing users to filter
`mongoengine querysets`_ dynamically.

Full documentation on `read the docs`_.

.. image:: https://secure.travis-ci.org/alex/django-filter.png?branch=master
   :target: http://travis-ci.org/alex/django-filter

Requirements
------------

* Python 2.6+
* Django 1.4.5+

Installation
------------

Install using pip::

    pip install django-filter-mongoengine

Or clone the repo and add to your PYTHONPATH::

    git clone git@github.com:surfeurX/django-filter-mongoengine.git

Usage
-----

::

    import django_filters_mongoengine

    class ProductFilter(django_filters_mongoengine.FilterSet):
        class Meta:
            model = Product
            fields = ['name', 'price', 'manufacturer']


And then in your view you could do::

    def product_list(request):
        filter = ProductFilter(request.GET, queryset=Product.objects.all())
        return render_to_response('my_app/template.html', {'filter': filter})


.. _`mongoengine querysets`: http://mongoengine-odm.readthedocs.org/apireference.html#module-mongoengine.queryset
.. _`read the docs`: https://django-filter.readthedocs.org/en/latest/

