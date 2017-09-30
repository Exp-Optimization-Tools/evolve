# evolutionary

<!-- Badges -->

[![build-status][]][ci-server]

[build-status]: https://travis-ci.org/Kautenja/evolutionary.svg?branch=master
[ci-server]: https://travis-ci.org/Kautenja/evolutionary

<!-- Tagline description -->

Generalized forms of evolutionary algorithms using numpy.


# Usage

## Installing dependencies

[Makefile][] contains shortcuts for frequently used project commands.

Note: make sure you have [Make](https://www.gnu.org/software/make/) installed.

To install dependency Python modules in the [requirements.txt][] file:

```shel
make install
```

## Running tests

To run the test modules inside the [src][] package:

```shell
make test
```

## Starting the application

To execute the code in the [__main__.py][] script:

```shell
make start
```



[Makefile]: ./Makefile
[requirements.txt]: ./requirements.txt
[src]: ./src
[__main__.py]: ./__main__.py
