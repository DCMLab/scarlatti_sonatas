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
 


# Overview
|file_name|measures|labels|standard|                  annotators                  |reviewers|
|---------|-------:|-----:|--------|----------------------------------------------|---------|
|K001     |      31|    89|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, JH   |
|K002     |      78|   146|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, JH   |
|K003     |      94|   198|2.3.0   |unknown (0.0.0), Davor Krkljus (2.3.0)        |DK, JH   |
|K004     |      39|   171|0.0.0   |unknown                                       |         |
|K005     |      90|   129|0.0.0   |unknown                                       |         |
|K006     |      75|    97|2.3.0   |unknown (0.0.0), Ehsan Mohagheghi Fard (2.3.0)|EMF, JH  |
|K007     |     155|   270|0.0.0   |unknown                                       |         |
|K008     |      47|   194|0.0.0   |unknown                                       |         |
|K009     |      60|   129|0.0.0   |unknown                                       |         |
|K010     |      75|   158|0.0.0   |unknown                                       |         |
|K011     |      28|   111|0.0.0   |unknown                                       |         |
|K012     |      48|   284|0.0.0   |unknown                                       |         |
|K013     |     113|   247|0.0.0   |unknown                                       |         |
|K014     |      43|   146|0.0.0   |unknown                                       |         |
|K017     |     129|   236|0.0.0   |unknown                                       |         |
|K018     |      52|   300|0.0.0   |unknown                                       |         |
|K019     |      92|   221|0.0.0   |unknown                                       |         |
|K020     |     102|   143|0.0.0   |unknown                                       |         |
|K021     |     150|   265|0.0.0   |unknown                                       |         |
|K022     |      78|   186|0.0.0   |unknown                                       |         |
|K023     |      70|   272|0.0.0   |unknown                                       |         |
|K025     |      87|   271|0.0.0   |unknown                                       |         |
|K027     |      67|   188|0.0.0   |unknown                                       |         |
|K031     |     114|   218|0.0.0   |unknown                                       |         |
|K032     |      24|    37|0.0.0   |unknown                                       |         |
|K033     |     119|   155|0.0.0   |unknown                                       |         |
|K034     |      28|    73|0.0.0   |unknown                                       |         |
|K035     |      40|   152|0.0.0   |unknown                                       |         |
|K036     |      95|   245|0.0.0   |unknown                                       |         |
|K037     |      52|   167|0.0.0   |unknown                                       |         |
|K039     |      49|   209|0.0.0   |unknown                                       |         |
|K040     |      24|    54|0.0.0   |unknown                                       |         |
|K044     |     152|   240|0.0.0   |unknown                                       |         |
|K046     |     144|   272|0.0.0   |unknown                                       |         |
|K047     |      75|   308|0.0.0   |unknown                                       |         |
|K048     |     124|   290|0.0.0   |unknown                                       |         |
|K049     |     120|   250|0.0.0   |unknown                                       |         |
|K050     |     159|    99|0.0.0   |unknown                                       |         |
|K051     |      47|   253|0.0.0   |unknown                                       |         |
|K052     |      55|   344|0.0.0   |unknown                                       |         |
|K053     |     100|   155|0.0.0   |unknown                                       |         |
|K054     |      58|   182|0.0.0   |unknown                                       |         |
|K055     |     133|   203|0.0.0   |unknown                                       |         |
|K056     |      58|   213|0.0.0   |unknown                                       |         |
|K057     |     182|   308|0.0.0   |unknown                                       |         |
|K059     |      31|    98|0.0.0   |unknown                                       |         |
|K061     |     156|   276|0.0.0   |unknown                                       |         |
|K062     |     109|   140|0.0.0   |unknown                                       |         |
|K063     |      60|   115|0.0.0   |unknown                                       |         |
|K064     |      47|    70|0.0.0   |unknown                                       |         |
|K065     |      74|   155|0.0.0   |unknown                                       |         |
|K066     |      32|   160|0.0.0   |unknown                                       |         |
|K067     |      22|    85|0.0.0   |unknown                                       |         |
|K068     |     116|   170|0.0.0   |unknown                                       |         |
|K069     |      63|   215|0.0.0   |unknown                                       |         |
|K071     |      29|   135|0.0.0   |unknown                                       |         |
|K072     |      37|   121|0.0.0   |unknown                                       |         |
|K074     |      40|    66|0.0.0   |unknown                                       |         |
|K075     |      45|   103|0.0.0   |unknown                                       |         |
|K076     |      67|   171|0.0.0   |unknown                                       |         |
|K087     |      70|   237|0.0.0   |unknown                                       |         |
|K092     |      55|   172|0.0.0   |unknown                                       |         |
|K094     |      26|    50|0.0.0   |unknown                                       |         |
|K095     |      23|    46|0.0.0   |unknown                                       |         |
|K096     |     211|   355|0.0.0   |unknown                                       |         |
|K097     |     247|   267|0.0.0   |unknown                                       |         |
|K098     |     113|   177|0.0.0   |unknown                                       |         |
|K099     |      86|   191|0.0.0   |unknown                                       |         |
|K100     |      50|   149|0.0.0   |unknown                                       |         |
