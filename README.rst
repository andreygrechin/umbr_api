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
ever established. By delivering security from the cloud, it also provides
more effective security and simple deployment options.

**umbr_api** supports Enforcement API, Reporting API, and Management API
with some limitations. With the help of **umbr_api**, you can add new sites and
URLs to blacklists, remove or show current entries, quickly check
the latest security events, or check the status of registered computers
or networks.

Using command-line tools, like **umbr_api**, can immediately provide
information to administrators of the system without myriads of clicks
through GUI interfaces, two-factor authentications, etc.

References:
    * `Cisco Umbrella Enforcement API <https://docs.umbrella.com/developer/enforcement-api/domains2/>`__
    * `Cisco Umbrella Reporting API <https://docs.umbrella.com/umbrella-api/docs/overview/>`__
    * `Cisco Umbrella Management API <https://docs.umbrella.com/umbrella-api/v1.0/reference/>`__

**umbr_api** was created mostly for educational purposes.

Installation
------------

To install from a local folder execute at the ‘umbr_api’ root directory:

.. code:: bash

    pip3 install -e . --no-use-pep517

To install other requirements from a local folder, execute at the ‘umbr_api’
root directory:

.. code:: bash

    pip3 install -e .[dev] --no-use-pep517
    pip3 install -e .[doc] --no-use-pep517
    pip3 install -e .[dev_lint] --no-use-pep517

To install from production The Python Package Index (PyPI) https://pypi.org/
execute:

.. code:: bash

    pip3 install umbr_api

To install from GitHub:

.. code:: bash

    pip3 install git+https://github.com/kolatz/umbr_api.git

To install from a local archive:

.. code:: bash

    pip3 install filename.tar.gz

Please note that you still need to register and activate the API key from Cisco
to enable functionality.

Use of command-line utility
---------------------------

``main()`` in ``umbrella.py`` is registered as ``umbrella`` executable.
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

The API key
-----------

How to obtain the API key
^^^^^^^^^^^^^^^^^^^^^^^^^

You can sign up for a 14-day free trial here: https://signup.umbrella.com/

How to use the API key
^^^^^^^^^^^^^^^^^^^^^^

#. Provide it as an argument for the command-line utility

.. code:: bash

    umbrella del www.example.com --key YOUR-CUSTOMER-KEY-IS-HERE-0123456789

#. Provide it as part of a program call

.. code-block:: python

    from umbr_api.get import get_list
    response = get_list(key='YOUR-CUSTOMER-KEY-IS-HERE-0123456789')

#. Create ``data/enforcement.json`` file in **umbr_api** package directory.
This is an unsecured and unsupported way because of storing keys in clear text
format. To find the package directory:

.. code-block:: python

    import os
    import umbr_api
    print(os.path.abspath(umbr_api.__file__))

#. The API key can be read from a keyring for command-line execution. To save
the API key, you can use:

.. code-block:: bash

    umbrella keyring --add YOUR-CUSTOMER-KEY-IS-HERE-0123456789
    umbrella keyring --show

.. note::
    - Keyrings tested only for macOS platforms
    - By default, all python apps can read the values of the keys from a keyring
    - ``umbrella`` tries to use ``--key`` firstly, then keychain, and finally ``data/enforcement.json`` file within the **umbr_api** package directory.

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
#. Other methods for change or delete entities are not supported, and no plans to do that.

Known issues
------------

Error while accessing macOS keyring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python's binaries may not be signed, and they fail to get access to
macOS keyring. You should resign them manually to fix it. Error message::

    keyring.backends._OS_X_API.SecAuthFailure: (-25293, 'Security Auth Failure: make sure python is signed with codesign util')

.. code-block:: bash

    $ codesign -v `which python'
    /Users/user/.virtualenvs/builings/bin/python: invalid Info.plist (plist or signature have been modified)
    In architecture: x86_64
    $ codesign -f -s - `which python`
    /Users/user/.virtualenvs/builings/bin/python: replacing existing signature

Documentation
-------------

Documentation pages based on README.rst file and docstrings. Created for educational purposes.

-  http://umbr-api.readthedocs.io/en/latest/

.. note::
    A symbolic link README.rst --> docs/README.rst was used to create ToC in Sphinx, which doesn't support relative paths for ToC.

Contribution guidelines
-----------------------

-  https://github.com/kolatz/umbr_api

Whom do I talk to
-----------------

-  https://github.com/kolatz/

Examples of output
------------------

.. code-block:: bash

    $ umbrella get
    Page: 1
    Limit: 10

    +----------+-----------------+---------------------+
    |       id | name            | lastSeenAt          |
    +==========+=================+=====================+
    |     2201 | example.com     | 2018-10-21 00:12:05 |
    +----------+-----------------+---------------------+
    | 29996557 | qqq.example.com | 2018-03-05 22:33:24 |
    +----------+-----------------+---------------------+

.. code-block:: bash

    $ umbrella networks
    +---------+------------+-------------+--------------+----------------+-------------+----------+--------------------------+
    | name    |   originId | isDynamic   | isVerified   |   prefixLength | ipAddress   | status   | createdAt                |
    +=========+============+=============+==============+================+=============+==========+==========================+
    | VPN Ams |  154312952 | True        | True         |             32 | 90.154.51.1 | CLOSED   | 2018-06-02T08:03:31.000Z |
    +---------+------------+-------------+--------------+----------------+-------------+----------+--------------------------+
    $

.. code-block:: bash

    $ umbrella -e originId,deviceId,osVersionName,appliedBundle,lastSync roamingcomputers
    +---------+----------+-----------+---------------------------------------------------------+-----------------+-----------------+
    | type    | status   | version   | osVersion                                               | name            | hasIpBlocking   |
    +=========+==========+===========+=========================================================+=================+=================+
    | roaming | Open     | 2.1.4     | NSMACHOperatingSystem (Version 10.13.6 (Build 17G6030)) | air             | False           |
    +---------+----------+-----------+---------------------------------------------------------+-----------------+-----------------+
    | roaming | Off      | 2.2.150   | Microsoft Windows [Version 10.0.15063]                  | LAPTOP-17T1KDT4 | False           |
    +---------+----------+-----------+---------------------------------------------------------+-----------------+-----------------+
    $

.. code-block:: bash

    $ umbrella internalnetworks
    +------------+-------------+----------------+--------------------------+--------------------------+----------+------------+------------+
    |   originId | ipAddress   |   prefixLength | createdAt                | modifiedAt               |   siteId | name       | siteName   |
    +============+=============+================+==========================+==========================+==========+============+============+
    |  190843164 | 192.168.1.0 |             24 | 2018-10-04T18:59:05.000Z | 2018-10-04T18:59:05.000Z |   599748 | Main LAN   |            |
    +------------+-------------+----------------+--------------------------+--------------------------+----------+------------+------------+
    |  190843328 | 172.16.0.0  |             12 | 2018-10-04T19:00:05.000Z | 2018-10-04T19:00:05.000Z |   599748 | Docker LAN |            |
    +------------+-------------+----------------+--------------------------+--------------------------+----------+------------+------------+
    $

.. code-block:: bash

    $ umbrella -e domains,queryFailureRateAcceptable,modifiedAt,state,UpdatedAt,lastSyncTime,originId,createdAt,type,externalIP,isUpgradable virtualappliances
    +---------------+------------+------------+---------------------+------------+----------+----------+-----------+
    | settings      | settings   |   settings | settings            | settings   |   siteId | health   | name      |
    | internalIPs   | hostType   |     uptime | isDnscryptEnabled   | version    |          |          |           |
    +===============+============+============+=====================+============+==========+==========+===========+
    | 192.168.1.15  | hyperv     |      15607 | False               | 2.4.4      |   599748 | okay     | umbrella2 |
    +---------------+------------+------------+---------------------+------------+----------+----------+-----------+
    | 192.168.1.14  | hyperv     |      15063 | False               | 2.4.4      |   599748 | okay     | umbrella1 |
    +---------------+------------+------------+---------------------+------------+----------+----------+-----------+
    $

.. code-block:: bash

    $ umbrella sites
    +------------+-------------+--------------+--------------------------+--------------------------+--------+------------------------+-----------+----------+
    |   originId | isDefault   | name         | modifiedAt               | createdAt                | type   |   internalNetworkCount |   vaCount |   siteId |
    +============+=============+==============+==========================+==========================+========+========================+===========+==========+
    |  117852936 | True        | Default Site | 2017-12-05T21:23:04.000Z | 2017-12-05T21:23:04.000Z | site   |                      2 |         2 |   599748 |
    +------------+-------------+--------------+--------------------------+--------------------------+--------+------------------------+-----------+----------+

.. code-block:: bash

    $ umbrella users
    +-------------+------------+--------------------+------------+----------+----------+-------------------+---------+---------------+--------------------------+
    | firstname   | lastname   | email              | role       |   roleId | status   | twoFactorEnable   |      id | timezone      | lastLoginTime            |
    +=============+============+====================+============+==========+==========+===================+=========+===============+==========================+
    | Andrey      | Grechin    | angrechi@cisco.com | Full Admin |        1 | Active   | True              | 9571796 | Europe/Moscow | 2019-05-01T08:43:57.000Z |
    +-------------+------------+--------------------+------------+----------+----------+-------------------+---------+---------------+--------------------------+

.. code-block:: bash

    $ umbrella roles
    +------------------+-------------------+----------+
    |   organizationId | label             |   roleId |
    +==================+===================+==========+
    |                0 | Full Admin        |        1 |
    +------------------+-------------------+----------+
    |                0 | Read Only         |        2 |
    +------------------+-------------------+----------+
    |                0 | Block Page Bypass |        3 |
    +------------------+-------------------+----------+
    |                0 | Reporting Only    |        4 |
    +------------------+-------------------+----------+
    $

.. code-block:: bash

    $ umbrella -e=datetime,externalIp,destination,originID activity --limit 2
    +------------+-----------------+--------------+--------------+--------+---------------+---------------+
    |   originId | originType      | internalIp   | categories   | tags   | originLabel   | actionTaken   |
    +============+=================+==============+==============+========+===============+===============+
    |  252626430 | Network Devices | 192.168.1.41 | Blogs        |        | r1-c1111      | BLOCKED       |
    |            |                 |              | Malware      |        |               |               |
    |            |                 |              | Web Hosting  |        |               |               |
    +------------+-----------------+--------------+--------------+--------+---------------+---------------+
    |  252626430 | Network Devices | 192.168.1.41 | Blogs        |        | r1-c1111      | BLOCKED       |
    |            |                 |              | Malware      |        |               |               |
    |            |                 |              | Web Hosting  |        |               |               |
    +------------+-----------------+--------------+--------------+--------+---------------+---------------+
    $

.. code-block:: bash

    $ umbrella top cisco.com
    +--------+---------------+------------------+------------+--------------------+
    |   rank | originLabel   | originType       |   originId |   numberOfRequests |
    +========+===============+==================+============+====================+
    |      1 | Main LAN      | internal_network |  190843164 |                  4 |
    +--------+---------------+------------------+------------+--------------------+
    $

.. code-block:: bash

    $ umbrella -e originId,destination,externalIp recent cisco.com --limit 2
    +--------+-----------------+--------------+---------------------+---------------+---------------+--------------------------+
    | tags   | originType      | internalIp   | categories          | originLabel   | actionTaken   | datetime                 |
    +========+=================+==============+=====================+===============+===============+==========================+
    |        | Network Devices | 192.168.1.13 | Software/Technology | r1-c1111      | ALLOWED       | 2019-05-11T19:40:25.646Z |
    |        |                 |              | Business Services   |               |               |                          |
    |        |                 |              | Allow List          |               |               |                          |
    +--------+-----------------+--------------+---------------------+---------------+---------------+--------------------------+
    |        | Network Devices | 192.168.1.13 | Software/Technology | r1-c1111      | ALLOWED       | 2019-05-11T19:40:25.633Z |
    |        |                 |              | Business Services   |               |               |                          |
    |        |                 |              | Allow List          |               |               |                          |
    |        |                 |              | Software Updates    |               |               |                          |
    +--------+-----------------+--------------+---------------------+---------------+---------------+--------------------------+
    $
