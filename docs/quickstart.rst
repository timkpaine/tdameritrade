===============
Getting started
===============
.. WARNING:: tdameritrade is under active beta development, so interfaces and functionality may change

Overview
===============

TDClient object
---------------
The API works with a ``TDClient`` object:


.. code:: python3

    from tdameritrade import TDClient
    c = TDClient(<TOKEN>)
    c.accounts()

.. image:: ./img/client/accounts.png
    :scale: 100%
    :alt: accounts.png
