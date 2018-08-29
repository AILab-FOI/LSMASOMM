# LSMASOMM
This repository contains the modelling environment (Atom3) used to develop LSMAS organisational meta-model for ModelMMORPG[^3] project at AI Lab @ FOI, and the meta-model being developed, along with a couple of models.

How to Use the Meta-model
=========================

Prerequisites
-------------

In order to run AToM<sup>3</sup> , the following prerequisites have
to be installed:

-   python tkinter (`sudo apt-get install python-tk`)
- ZODB (`pip install zodb`)

The AToM<sup>3</sup> development team suggests the following minimum
requirements[^1] for using AToM<sup>3</sup> :

> AToM3 can and has been installed and used on Windows, Mac, and Unix
> computers. The only requirement is that Python 2.3 and Tk/tcl 8.3 or
> better be installed.
>
> A processor speed of 1 ghz or better is \*highly\* recommended.

Running AToM<sup>3</sup>
-----------------------------

The following Linux terminal commands should be run from within the
atom3 folder.

First run of AToM<sup>3</sup> will set up basic user settings and
close the program. Make sure the `atom3.sh` is executable.

    ./atom3.sh

To run AToM<sup>3</sup> and use the LSMASOMM meta-model, use the
following command:

    ./atom3.sh LSMASOMM

To run AToM<sup>3</sup> and open the TMWQDE model, which contains
the basic meta-model showcase by modelling The Quest for the Dragon Egg,
a quest developed for The Mana World[^2] MMORPG during the
ModelMMORPG[^3] project, use the following command:

    ./atom3.sh Models/TMWQDE_MDL.py

#### NB

AToM<sup>3</sup> reports some errors in terminal by default. These
errors should be ignored, as instructed by AToM<sup>3</sup> authors.
Initial setup will cause several dialogue boxes to pop up when running
AToM<sup>3</sup> for the first and second time.

[^1]: <http://atom3.cs.mcgill.ca/people/denis/files/Installation.txt>

[^2]: <https://www.themanaworld.org>

[^3]: <http://ai.foi.hr/modelmmorpg/>
