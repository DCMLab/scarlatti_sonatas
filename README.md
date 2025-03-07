# Domenico Scarlatti - Harpsichord Sonatas

The harmonic annotations come from ancient times (hence harmony_version `0.0.0`)
and have been handed down in the form of the TXT files contained in the folder
`original_annotations`. A number of manual adjustments had to be made to allow
their being written into the MuseScore files because their encoding is not very
rigorous and was never algorithmically validated.

Apart from the syntactical inconsistencies and typical careless mistakes, the
analyses look reasonable. However, since they predate last years' developments
of the DCML standard, a couple of things will need to be corrected systematically,
such as:

* all modulations are expressed in absolute rather than relative terms;
* repetition of identical labels;
* the overuse of `@none` which, in this repertoire, can in principle always be avoided;
* obvious syntax errors (e.g. `I(M7)`);
* absence of an overarching harmonic rhythm as a guideline for a consistent level of detail;
* cadence labels (for example, `QA` ('Quintabsatz') was partially used for what we would
  label as `HC`);

During the update, these points can be corrected tacitly. Individual commits with
explanatory messages should be created for changes to the actual analysis.
 
## Origin

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
|K049     |     118|   268|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, AB   |
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
