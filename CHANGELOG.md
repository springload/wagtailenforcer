# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

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

[Unreleased]: https://github.com/springload/wagtailenforcer/compare/0.3...HEAD
[1.0.3]: https://github.com/springload/wagtailenforcer/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/springload/wagtailenforcer/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/springload/wagtailenforcer/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/springload/wagtailenforcer/compare/e764e0ade65afa66286ce5437a39ed93862a79b8...v1.0.0
