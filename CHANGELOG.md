# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2019-05-06

### Added

- changelog file (CHANGELOG.md)
- black formatter as a default option
- optional linters (bandit, isort, flake8, safety, check, pyroma)
- configuration files for pylint (.pylintrc) and markdownlint (.markdownlint.json)
- README description of a keyring module issue with unsigned python binaries
- a logo file
- guidelines badges

### Changed

- license headers and a copyright year to 2019
- README badges
- ci for new python builds
- sort imports

### Removed

- support for Python 3.4

### Fixed

- pytest import from a local directory
- typos
