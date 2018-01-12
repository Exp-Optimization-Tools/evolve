# Evolve

<!-- Badges -->

[![build-status][]][ci-server]

[build-status]: https://travis-ci.org/Kautenja/evolve.svg?branch=master
[ci-server]: https://travis-ci.org/Kautenja/evolve


<!-- Tagline description -->

Generalized genetic algorithms using NumPy.


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

# How Should I Cite `evolve`?

Please cite `evolve` if you use it in your research using the following block:

```latex
@misc{kauten2018evolve,
  author = {Christian Kauten},
  title = {evolve},
  year = {2018},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/Kautenja/evolve}},
}
```


[Makefile]: ./Makefile
[requirements.txt]: ./requirements.txt
[src]: ./src
[__main__.py]: ./__main__.py
