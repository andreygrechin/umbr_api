======
README
======

.. list-table::
  :stub-columns: 1

  * - Docs
    - | |docs|
  * - Tests
    - | |travis| |requires|
      | |appveyor| |coveralls|
      | |codacy| |codeclimate|
  * - Package
    - | |supported-versions| |supported-implementations|
      | |dev-status| |pypi-version| |license|
  * - GitHub
    - | |gh-tag| |gh-issues|
  * - Guidelines
    - | |code-style| |editor-config| |linter-pylint|

.. |docs| image:: https://readthedocs.org/projects/umbr-api/badge/?style=flat
    :target: https://readthedocs.org/projects/umbr_api
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/kolatz/umbr_api.svg?branch=master
    :target: https://travis-ci.org/kolatz/umbr_api
    :alt: Travis Build Status

.. |requires| image:: https://requires.io/github/kolatz/umbr_api/requirements.svg?branch=master
    :target: https://requires.io/github/kolatz/umbr_api/requirements/?branch=master
    :alt: Requirements Status

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/hptdwfa7mcsu5tla/branch/master?svg=true
    :target: https://ci.appveyor.com/project/kolatz/umbr-api/
    :alt: Appveyor Build Status

.. |coveralls| image:: https://coveralls.io/repos/github/kolatz/umbr_api/badge.svg?branch=master
    :target: https://coveralls.io/github/kolatz/umbr_api?branch=master
    :alt: coveralls

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/af8d1fa5bca74a029a3be10afc51b857
    :target: https://www.codacy.com/app/kolatz/umbr_api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kolatz/umbr_api&amp;utm_campaign=Badge_Grade
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://api.codeclimate.com/v1/badges/fc9257657747094f8f5b/maintainability
    :target: https://codeclimate.com/github/kolatz/umbr_api
    :alt: Maintainability

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/umbr_api.svg
    :target: https://pypi.python.org/pypi/umbr_api
    :alt: Supported versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/umbr_api.svg
    :target: https://pypi.python.org/pypi/umbr_api
    :alt: Supported implementation

.. |dev-status| image:: https://img.shields.io/pypi/status/umbr_api.svg
    :target: https://pypi.python.org/pypi/umbr_api
    :alt: Development status

.. |pypi-version| image:: https://img.shields.io/pypi/v/umbr_api.svg
    :target: https://pypi.python.org/pypi/umbr_api
    :alt: PyPI Package

.. |license| image:: https://img.shields.io/pypi/l/umbr_api.svg
    :target: https://pypi.python.org/pypi/umbr_api
    :alt: License

.. |gh-tag| image:: https://img.shields.io/github/tag/kolatz/umbr_api.svg
    :target: https://GitHub.com/kolatz/umbr_api/tags
    :alt: GitHub tag

.. |gh-issues| image:: https://img.shields.io/github/issues/kolatz/umbr_api.svg
    :target: https://GitHub.com/kolatz/umbr_api/issues
    :alt: GitHub issues

.. |code-style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/python/black
    :alt: Code style: black

.. |editor-config| image:: https://img.shields.io/static/v1.svg?label=&message=EditorConfig&color=blue
    :target: https://editorconfig.org
    :alt: EditorConfig

.. |linter-pylint| image:: https://img.shields.io/static/v1.svg?label=Linter&message=Pylint&color=blue
    :target: https://www.pylint.org/
    :alt: Pylint

**umbr_api** is Cisco Umbrella APIs wrapper and a command-line utility.

`Cisco Umbrella <https://umbrella.cisco.com/>`__ uses the internet’s
DNS infrastructure to block malicious destinations before a connection is
ever established. By delivering security from the cloud, it also provide
more effective security and easy deployment options.

**umbr_api** supports Enforcement API, Reporting API, and Management API
with some limitations. With help of **umbr_api** you can add new sites and
URLs to black lists, remove or show current entries, quickly check
the latest security events, or check a status of registered computers
or networks.

Using of command line tools, like **umbr_api** can immediately provide
information to administrators of the system without myriads of clicks
through GUI interfaces, two-factor authentications, etc.

References:
    * `Cisco Umbrella Enforcement API <https://docs.umbrella.com/developer/enforcement-api/domains2/>`__
    * `Cisco Umbrella Reporting API <https://docs.umbrella.com/umbrella-api/docs/overview/>`__
    * `Cisco Umbrella Management API <https://docs.umbrella.com/umbrella-api/v1.0/reference/>`__

Was created mostly for educational purposes.

Installation
------------

To install from a local folder execute at the ‘umbr_api’ root directory:

.. code:: bash

    pip3 install -e . --no-use-pep517

To install extra requirements from a local folder execute at the ‘umbr_api’
root directory:

.. code:: bash

    pip3 install -e .[dev] --no-use-pep517
    pip3 install -e .[doc] --no-use-pep517
    pip3 install -e .[dev_lint] --no-use-pep517

To install from production The Python Package Index (PyPI) https://pypi.org
execute:

.. code:: bash

    pip3 install umbr_api

To install from GitHub:

.. code:: bash

    pip3 install git+https://github.com/kolatz/umbr_api.git

To install from a local archive:

.. code:: bash

    pip3 install filename.tar.gz

Please note, that you still need to register and activate API key from Cisco
to enable functionality.

Use of command-line utility
---------------------------

``main()`` in ``umbrella.py`` will be registered as ``umbrella`` executable.
So, you can run it directly.

Examples (Enforcement API):

.. code-block:: bash

    umbrella add www.example.com http://www.example.com/images
    umbrella add example.com example.com --force
    umbrella del www.example.com
    umbrella del 555XXXXX --key YOUR-CUSTOMER-KEY-IS-HERE-0123456789
    umbrella get 100
    umbrella get --key YOUR-CUSTOMER-KEY-IS-HERE-0123456789

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

The API key should be specified via CLI, or it could be read it from
``enforcement.json`` within package ``data\`` folder.

API key
-------

How to obtain API key
^^^^^^^^^^^^^^^^^^^^^

You can sign up for 14 day free trial here: https://signup.umbrella.com/

How to use API key
^^^^^^^^^^^^^^^^^^

#. Provide it as an argument for command-line utility

.. code:: bash

    umbrella del www.example.com --key YOUR-CUSTOMER-KEY-IS-HERE-0123456789

#. Provide it as part of a program call

.. code-block:: python

    from umbr_api.get import get_list
    response = get_list(key='YOUR-CUSTOMER-KEY-IS-HERE-0123456789')

#. Create ``data/enforcement.json`` file in **umbr_api** package directory.
This is an unsecured and unsupported way because of storing key in clear text
format. To find package directory:

.. code-block:: python

    import os
    import umbr_api
    print(os.path.abspath(umbr_api.__file__))

#. API key can be read from a keyring for command-line execution. To save
API key you can use:

.. code-block:: bash

    umbrella keyring --add YOUR-CUSTOMER-KEY-IS-HERE-0123456789
    umbrella keyring --show

.. note::
    - Only macOS platform is tested for keyrings
    - By default all python apps can read the values of the keys from a keyring
    - ``umbrella`` will try to use ``--key`` firstly, then keychain, and finally ``data/enforcement.json`` file within **umbr_api** package directory.

Supported methods
-----------------

Enforcement API
^^^^^^^^^^^^^^^
#. Add (POST)
#. Get (GET)
#. Remove (DELETE)

Management API
^^^^^^^^^^^^^^
#. Networks (GET)
#. Roaming Computers (GET)
#. Internal Networks (GET)
#. Virtual Appliances (GET)
#. Sites (GET)
#. Users (GET)
#. Roles (GET)

Reporting API
^^^^^^^^^^^^^
#. Security Activity Report (GET)
#. Destinations: Top Identities (GET)
#. Destinations: Most recent requests (GET)

Limitations
-----------

#. Lack of documentation
#. You heed to have an active subscription or evaluation
#. Asserts will be removed with compiling to optimized byte code. This caused various protections to be removed.
#. Other methods for change or delete entities are not supported and no plans to do that

Known issues
------------

Error while accessing macOS keyring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python's binaries may not be signed and they will fail to get an access to
macOS keyring. You should resign them manually to fix it. Error message::

    keyring.backends._OS_X_API.SecAuthFailure: (-25293, 'Security Auth Failure: make sure python is signed with codesign util')

.. code-block:: bash

    $ codesign -v `which python`
    /Users/user/.virtualenvs/builings/bin/python: invalid Info.plist (plist or signature have been modified)
    In architecture: x86_64
    $ codesign -f -s - `which python`
    /Users/user/.virtualenvs/builings/bin/python: replacing existing signature

Documentation
-------------

Documentation pages based on README.rst file and docstrings.

-  http://umbr-api.readthedocs.io/en/latest/

.. note::
    - A symbolic link README.rst --> docs/README.rst was used to create ToC in Sphinx, which doesn't support relative paths for ToC.

Contribution guidelines
-----------------------

-  https://github.com/kolatz/umbr_api/blob/master/docs/CONTRIBUTING.md

Who do I talk to
----------------

-  https://github.com/kolatz/
