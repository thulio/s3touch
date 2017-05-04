s3touch
=======

s3touch is a simple script to simulate a "touch" event on S3 keys.

This is useful when you're using a AWS Lambda function monitoring S3 and you
want to (re)process a bunch of files.


Usage
-----

.. code-block:: bash

   s3touch --path s3://PATH/TO/BUCKET

Installation
------------

.. code-block:: bash

   pip install s3touch