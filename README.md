

# Alignments

This repository contains word alignments for Bibles, including both automatic alignments and manually corrected alignments.  It is meant to serve two goals:

1. Developers need a way to obtain the best available alignments for a
   given language or translation.  We want to collect the best
   alignments we can find here and provide a way to find needed
   alignments and track development of alignment. 
2. The [Scripture Burrito Working
   Group](https://docs.burrito.bible/en/latest/) is creating a
   Scripture Alignments flavor, which will be a standard for
   exchanging alignment data.  This repository reflects a
   working proposal, and as the standard develops, the data in this
   repository will be used to ensure that the standard is adequate. 

Alignment data is provided by various parties, who own the copyright
to their alignments. All alignment data is licensed under a [Creative
Commons Attribution 4.0 International License][cc-by].


[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
[![CC BY 4.0][cc-by-image]][cc-by]

All code on this repository is Copyright (c) 2024 by Biblica, Inc. and
licensed under a [MIT License](https://opensource.org/license/mit/).

## Python Quick Start

This code (but not the data) can be installed with `pip` or (preferred) `pipx`:

```
$ pipx install bible-alignments
```

Alternatively, you can clone this repository and run the code locally,
using [Poetry](https://python-poetry.org/). 

## Contributing Alignments

We're interested in collecting alignments that are useful for
the Bible translation community, especially those based on
openly-licensed texts. If you have alignments to contribute, see
[Contributing](docs/contributing.md). 
