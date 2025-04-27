![Version](https://img.shields.io/github/v/release/DCMLab/scarlatti_sonatas?display_name=tag)
[![DOI](https://zenodo.org/badge/467122531.svg)](https://doi.org/10.5281/zenodo.14992884)
![GitHub repo size](https://img.shields.io/github/repo-size/DCMLab/scarlatti_sonatas)
![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-9cf)


This is a README file for a data repository originating from the [DCML corpus initiative](https://github.com/DCMLab/dcml_corpora)
and serves as welcome page for both 

* the GitHub repo [https://github.com/DCMLab/scarlatti_sonatas](https://github.com/DCMLab/scarlatti_sonatas) and the corresponding
* documentation page [https://dcmlab.github.io/scarlatti_sonatas](https://dcmlab.github.io/scarlatti_sonatas)

For information on how to obtain and use the dataset, please refer to [this documentation page](https://dcmlab.github.io/scarlatti_sonatas/introduction).

When you use (parts of) this dataset in your work, please read and cite the accompanying data report:

_Hentschel, J., Rammos, Y., Neuwirth, M., & Rohrmeier, M. (2025). A corpus and a modular infrastructure for the 
empirical study of (an)notated music. Scientific Data, 12(1), 685. https://doi.org/10.1038/s41597-025-04976-z_

# Domenico Scarlatti – Keyboard Sonatas (A corpus of annotated scores)

This corpus of annotated [MuseScore](https://musescore.org) files has been created within  
the [DCML corpus initiative](https://github.com/DCMLab/dcml_corpora) and employs  
the [DCML harmony annotation standard](https://github.com/DCMLab/standards).  

While Italian-Spanish composer Domenico Scarlatti enjoyed generous royal patronage  
throughout his career, his compositions were not widely circulated during his own lifetime.  
He is best known today for 555 concise, one-movement keyboard sonatas, admired for  
their stylistic breadth and variety, for their theatrical dramatic charge, and for their prophetic  
formal innovations.

This corpus consists of 69 sonatas selected from the first 100 in Ralph Kirkpatrick's  
chronological ordering. These earlier works display a comparatively restrained degree  
of keyboard virtuosity and a considerable influence from the sequence-driven harmonic  
rhetoric of Vivaldi and Corelli. Taken alongside [our Corelli repository](https://github.com/DCMLab/corelli), these data will  
provide rich material for study of the Italian Baroque precedents of sonata-allegro form.

## Getting the data

* download repository as a [ZIP file](https://github.com/DCMLab/scarlatti_sonatas/archive/main.zip)
* download a [Frictionless Datapackage](https://specs.frictionlessdata.io/data-package/) that includes concatenations
  of the TSV files in the four folders (`measures`, `notes`, `chords`, and `harmonies`) and a JSON descriptor:
  * [scarlatti_sonatas.zip](https://github.com/DCMLab/scarlatti_sonatas/releases/latest/download/scarlatti_sonatas.zip)
  * [scarlatti_sonatas.datapackage.json](https://github.com/DCMLab/scarlatti_sonatas/releases/latest/download/scarlatti_sonatas.datapackage.json)
* clone the repo: `git clone https://github.com/DCMLab/scarlatti_sonatas.git` 


## Data Formats

Each piece in this corpus is represented by five files with identical name prefixes, each in its own folder. 
For example, the *Sonata K.1* has the following files:

* `MS3/K001.mscx`: Uncompressed MuseScore 3.6.2 file including the music and annotation labels.
* `notes/K001.notes.tsv`: A table of all note heads contained in the score and their relevant features (not each of them represents an onset, some are tied together)
* `measures/K001.measures.tsv`: A table with relevant information about the measures in the score.
* `chords/K001.chords.tsv`: A table containing layer-wise unique onset positions with the musical markup (such as dynamics, articulation, lyrics, figured bass, etc.).
* `harmonies/K001.harmonies.tsv`: A table of the included harmony labels (including cadences and phrases) with their positions in the score.

Each TSV file comes with its own JSON descriptor that describes the meanings and datatypes of the columns ("fields") it contains,
follows the [Frictionless specification](https://specs.frictionlessdata.io/tabular-data-resource/),
and can be used to validate and correctly load the described file. 

### Opening Scores

After navigating to your local copy, you can open the scores in the folder `MS3` with the free and open source score
editor [MuseScore](https://musescore.org). Please note that the scores have been edited, annotated and tested with
[MuseScore 3.6.2](https://github.com/musescore/MuseScore/releases/tag/v3.6.2). 
MuseScore 4 has since been released which renders them correctly but cannot store them back in the same format.

### Opening TSV files in a spreadsheet

Tab-separated value (TSV) files are like Comma-separated value (CSV) files and can be opened with most modern text
editors. However, for correctly displaying the columns, you might want to use a spreadsheet or an addon for your
favourite text editor. When you use a spreadsheet such as Excel, it might annoy you by interpreting fractions as
dates. This can be circumvented by using `Data --> From Text/CSV` or the free alternative
[LibreOffice Calc](https://www.libreoffice.org/download/download/). Other than that, TSV data can be loaded with
every modern programming language.

### Loading TSV files in Python

Since the TSV files contain null values, lists, fractions, and numbers that are to be treated as strings, you may want
to use this code to load any TSV files related to this repository (provided you're doing it in Python). After a quick
`pip install -U ms3` (requires Python 3.10 or later) you'll be able to load any TSV like this:

```python
import ms3

labels = ms3.load_tsv("harmonies/K001.harmonies.tsv")
notes = ms3.load_tsv("notes/K001.notes.tsv")
```


## Version history

See the [GitHub releases](https://github.com/DCMLab/scarlatti_sonatas/releases).

## Questions, Suggestions, Corrections, Bug Reports

Please [create an issue](https://github.com/DCMLab/scarlatti_sonatas/issues) and/or feel free to fork and submit pull requests.

## Cite as

> Hentschel, J., Rammos, Y., Neuwirth, M., & Rohrmeier, M. (2025). A corpus and a modular infrastructure for the empirical study of (an)notated music. Scientific Data, 12(1), 685. https://doi.org/10.1038/s41597-025-04976-z

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)).

![cc-by-nc-sa-image](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)

## Scores

The following sonatas have been typeset by Tom Schreyer: K003, K004, K005, K006, K007, K008, K009, K010, K011, K012, K013, K014, K017, K018, K019, K020, K021, K022, K025, K027, K031, K033, K037, K039, K040, K044, K046, K047, K049, K051, K052, K053, K054, K056, K057, K059, K061, K062, K065, K066, K067, K068, K069, K071, K072, K074, K075, K092, K094, K095, K096, K097, K099, K100

## Overview
|file_name|measures|labels|standard|                  annotators                  |reviewers|
|---------|-------:|-----:|--------|----------------------------------------------|---------|
|K001     |      31|    89|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, JH   |
|K002     |      78|   146|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, JH   |
|K003     |      94|   198|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, JH   |
|K004     |      39|   208|2.3.0   |unknown (0.0.0), Ehsan Mohagheghi Fard (2.3.0)|EMF, JH  |
|K005     |      90|   126|2.3.0   |unknown (0.0.0), Sylvie Tran (2.3.0)          |ST, JH   |
|K006     |      75|    97|2.3.0   |unknown (0.0.0), Ehsan Mohagheghi Fard (2.3.0)|EMF, JH  |
|K007     |     155|   270|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K008     |      47|   183|2.3.0   |unknown, Sylvie Tran (2.3.0)                  |ST, AB   |
|K009     |      60|   142|2.3.0   |unknown (0.0.0), Sylvie Tran (2.3.0)          |ST, JH   |
|K010     |      75|   165|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, ST   |
|K011     |      28|   101|2.3.0   |unknown, Adrian Nagel (2.3.0)                 |DK       |
|K012     |      48|   281|2.3.0   |unknown, Adrian Nagel (2.3.0)                 |DK       |
|K013     |     113|   240|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K014     |      43|   146|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, ST   |
|K017     |     129|   198|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K018     |      51|   272|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, ST   |
|K019     |      92|   227|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K020     |     102|   146|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, ST   |
|K021     |     150|   270|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, ST   |
|K022     |      78|   207|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, ST   |
|K023     |      70|   267|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, ST   |
|K025     |      87|   278|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, ST   |
|K027     |      67|   204|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, ST   |
|K031     |     114|   192|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, ST   |
|K032     |      24|    39|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K033     |     119|   117|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K034     |      28|    67|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K035     |      40|   147|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K036     |      95|   193|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K037     |      52|   179|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K039     |      49|   217|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K040     |      24|    53|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K044     |     152|   208|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K046     |     144|   321|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K047     |      75|   309|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K048     |     124|   234|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K049     |     118|   270|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K050     |     159|   246|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K051     |      47|   257|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K052     |      55|   378|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K053     |     100|   135|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K054     |      57|   202|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K055     |     133|   197|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K056     |      58|   222|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K057     |     182|   311|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K059     |      31|    97|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K061     |     156|   268|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K062     |     109|   128|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K063     |      60|   118|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K064     |      47|    72|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K065     |      74|   137|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K066     |      32|   182|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K067     |      22|    88|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K068     |     116|   157|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K069     |      63|   170|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K071     |      29|   133|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K072     |      37|   135|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K074     |      40|    60|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K075     |      45|    98|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K076     |      67|   162|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K087     |      70|   201|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K092     |      55|   178|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K094     |      26|    56|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K095     |      23|    47|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K096     |     211|   357|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K097     |     247|   207|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K098     |     113|   165|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
|K099     |      86|   175|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |
|K100     |      50|   144|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK       |


*Overview table automatically updated using [ms3](https://ms3.readthedocs.io/).*
