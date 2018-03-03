======
README
======

.. list-table::
  :stub-columns: 1

  * - Docs
    - | |docs|
  * - Tests
    - | |build1| |requires|
      | |codacy| |codeclimate|
      | |coveralls|
  * - Package
    - | |supported-versions| |supported-implementations|
      | |dev-status| |pypi-version| |license|
  * - GitHub
    - | |gh-release| |gh-tag| |gh-issues|

.. |coveralls| image:: https://coveralls.io/repos/github/kolatz/umbr_api/badge.svg?branch=release%2F0.3
    :target: https://coveralls.io/github/kolatz/umbr_api?branch=release%2F0.3
    :alt: coveralls

.. |build1| image:: https://travis-ci.org/kolatz/umbr_api.svg?branch=master
    :target: https://travis-ci.org/kolatz/umbr_api
    :alt: Travis Build Status

.. |unused1| image:: https://scrutinizer-ci.com/g/kolatz/umbr_api/badges/build.png?b=master
    :target: https://scrutinizer-ci.com/g/kolatz/umbr_api/build-status/master
    :alt: Scrutinizer Build Status

.. |docs| image:: https://readthedocs.org/projects/umbr_api/badge/?style=flat
    :target: https://readthedocs.org/projects/umbr_api
    :alt: Documentation Status

.. |requires| image:: https://requires.io/github/kolatz/umbr_api/requirements.svg?branch=master
    :target: https://requires.io/github/kolatz/umbr_api/requirements/?branch=master
    :alt: Requirements Status

.. |unused2| image:: https://img.shields.io/scrutinizer/g/kolatz/umbr_api/master.svg
    :target: https://scrutinizer-ci.com/g/kolatz/umbr_api
    :alt: Scrutinizer Status

.. |unused3| image:: https://landscape.io/github/kolatz/umbr_api/master/landscape.svg?style=flat
    :target: https://landscape.io/github/kolatz/umbr_api/master
    :alt: Code Health

.. |unused4| image:: https://img.shields.io/badge/Cisco-Umbrella-blue.svg
    :target: https://umbrella.cisco.com

.. |dev-status| image:: https://img.shields.io/pypi/status/umbr_api.svg
    :target: https://pypi.python.org/pypi/umbr_api
    :alt: Development status

.. |pypi-version| image:: https://img.shields.io/pypi/v/umbr_api.svg
    :target: https://pypi.python.org/pypi/umbr_api
    :alt: PyPI Package

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/umbr_api.svg
    :target: https://pypi.python.org/pypi/umbr_api
    :alt: Supported implementation

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/umbr_api.svg
    :target: https://pypi.python.org/pypi/umbr_api
    :alt: Supported versions

.. |license| image:: https://img.shields.io/pypi/l/umbr_api.svg
    :target: https://pypi.python.org/pypi/umbr_api
    :alt: License

.. |unused5| image:: https://img.shields.io/pypi/format/umbr_api.svg
    :target: https://pypi.python.org/pypi/umbr_api
    :alt: Format

.. |codeclimate| image:: https://api.codeclimate.com/v1/badges/fc9257657747094f8f5b/maintainability
    :target: https://codeclimate.com/github/kolatz/umbr_api
    :alt: Maintainability

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/af8d1fa5bca74a029a3be10afc51b857
    :target: https://www.codacy.com/app/kolatz/umbr_api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kolatz/umbr_api&amp;utm_campaign=Badge_Grade
    :alt: Codacy Code Quality Status

.. |gh-release| image:: https://img.shields.io/github/release/kolatz/umbr_api.svg
    :target: https://GitHub.com/kolatz/umbr_api/releases
    :alt: GitHub release

.. |gh-tag| image:: https://img.shields.io/github/tag/kolatz/umbr_api.svg
    :target: https://GitHub.com/kolatz/umbr_api/tags
    :alt: GitHub tag

.. |gh-issues| image:: https://img.shields.io/github/issues/kolatz/umbr_api.svg
    :target: https://GitHub.com/kolatz/umbr_api/issues
    :alt: GitHub issues

**umbr_api** is Cisco Umbrella Enforcement API wrapper and command-line
utility. With help of **umbr_api** you can add new sites and URL to the
customer's blocked site list, remove or show current entries from cli in
seconds.

`Cisco Umbrella <https://umbrella.cisco.com/>`__ uses the internet’s
infrastructure to block malicious destinations before a connection is ever
established. By delivering security from the cloud, not only do you save money,
but we also provide more effective security.

Created mostly for educational purposes.

Installation
------------

To install from a local folder execute at the ‘umbr_api’ root directory:

.. code:: bash

    pip3 install -e .

To install from production https://pypi.org execute:

.. code:: bash

    pip3 install umbr_api

To install from GitHub:

.. code:: bash

    pip3 install git+https://github.com/kolatz/umbr_api.git

To install from local archive:

.. code:: bash

    pip3 install filename.tar.gz

Please note, that you still need registered and active API key from Cisco to
enable functionality.

Use of command-line utility
---------------------------

``main()`` in ``umbrella.py`` registered as ``umbrella`` executable. So, you can run it directly.

Examples:

.. code-block:: bash

    umbrella --add www.example.com http://www.example.com/images
    umbrella --remove-domain www.example.com
    umbrella --remove-id www.example.com --key YOUR-CUSTOMER-KEY-IS-HERE-0123456789
    umbrella --get-list 100
    umbrella --get-list --key YOUR-CUSTOMER-KEY-IS-HERE-0123456789

Use API wrapper
---------------
You need to import particular functions or modules from ``umbr_api``. For example:

.. code-block:: python

    from umbr_api import get
    get.get_list(key='YOUR-CUSTOMER-KEY-IS-HERE-0123456789')

    from umbr_api.add import add
    add(domain='example.com', url='example.com', key='YOUR-CUSTOMER-KEY-IS-HERE-0123456789')

There three main functions:
    - ``umbr_api.get.get_list``
    - ``umbr_api.add.add``
    - ``umbr_api.remove.remove``

The API key should be specified via CLI, if not
functions try to read it from ``customer_key.json`` within package
``data\`` folder.

API key
-------

How to obtain API key
^^^^^^^^^^^^^^^^^^^^^

You can sign up for 14 day free trial here: https://signup.umbrella.com/

How to use API key
^^^^^^^^^^^^^^^^^^

1. Provide as an argument for command-line utility

.. code:: bash

    umbrella --remove-id www.example.com --key YOUR-CUSTOMER-KEY-IS-HERE-0123456789

2. Provide it as part of a program call

.. code-block:: python

    from umbr_api.get import get_list
    response = get_list(key='YOUR-CUSTOMER-KEY-IS-HERE-0123456789')

3. Create ``data/customer_key.json`` file within **umbr_api** package directory.
This is an unsecured and unsupported way because of keeping key in clear text
format. To find package directory:

.. code-block:: python

    import os
    import umbr_api
    print(os.path.abspath(umbr_api.__file__))

4. API key can be read from a keyring for command-line execution. To save
API key you can use:

.. code-block:: bash

    umbrella --keyring-add YOUR-CUSTOMER-KEY-IS-HERE-0123456789

.. note::
    - Only MacOS platform is tested for keyrings
    - By default all python apps can read the value of the key from a keyring
    - ``umbrella`` will try to use ``--key`` firstly, then keychain, and finally ``data/customer_key.json`` file within **umbr_api** package directory.

Limitations
-----------

1. Lack of documentation
2. You heed to have an Umbrella subscription or active evaluation
3. Storing API key within json file is not secure, better to provide it to the script directly
4. Asserts will be removed with compiling to optimized byte code. This caused various protections to be removed.

Documentation
-------------

Documentation pages based on README.rst file and docstrings. Created for educational purposes.

-  http://umbr-api.readthedocs.io/en/latest/

.. note::
    A symbolic link README.rst --> docs/README.rst was used to create ToC in Sphinx, which doesn't support relative paths for ToC.

Contribution guidelines
-----------------------

-  https://github.com/kolatz/umbr_api

Who do I talk to
----------------

-  https://github.com/kolatz/
