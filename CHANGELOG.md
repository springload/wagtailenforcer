# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

...

## [1.1.7] - 2018-06-24

### Added

- Fix reverse for blocklist


## [1.1.6] - 2018-06-22

### Added

- Add change password form


## [1.1.5] - 2018-06-21

### Fixed

- Issue with dotted view ref in template url

## [1.1.3] - 2018-05-17

### Fixed

- Issue with python 3.6 relative import


## [1.1.2] - 2018-04-23

### Fixed

- Crash when uploading an image (introduced in 1.1.1)

## [1.1.1] - 2018-04-23

### Fixed

- Crash when saving an image (as opposed to uploading an image)

## [1.1.0] - 2018-04-04

### Added

- Compatibility with Django 1.10 and 1.11

### Changed

- The project now depends on `django-password-policies-iplweb`, a maintained fork of the original `django-password-policies`. **Make sure to remove `django-password-policies` from your own list of requirements if you had it defined.**

## [1.0.4] - 2018-03-27

### Fixed

- ConnectionError is now catched properly and returned with a custom error message
- Return the correct network socket connection object when the unix socket connection fails

### Changed

- Do not register Calm AV signals when `CLAMAV_ACTIVE` is set to `False`

## [1.0.3] - 2016-06-16

### Added

- Compatibility with Wagtail 1.5

### Removed

- Compatibility with Wagtail prior 1.5

## [1.0.2] - 2016-05-03

## [1.0.1] - 2016-04-29

## [1.0.0] - 2016-04-19

Initial Release

[Unreleased]: https://github.com/springload/wagtailenforcer/compare/v1.1.3...HEAD
[1.1.3]: https://github.com/springload/wagtailenforcer/compare/v1.1.2...v1.1.3
[1.1.2]: https://github.com/springload/wagtailenforcer/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/springload/wagtailenforcer/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/springload/wagtailenforcer/compare/v1.0.4...v1.1.0
[1.0.4]: https://github.com/springload/wagtailenforcer/compare/v1.0.3...v1.0.4
[1.0.3]: https://github.com/springload/wagtailenforcer/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/springload/wagtailenforcer/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/springload/wagtailenforcer/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/springload/wagtailenforcer/compare/e764e0ade65afa66286ce5437a39ed93862a79b8...v1.0.0
