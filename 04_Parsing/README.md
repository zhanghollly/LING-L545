Holly Zhang (zhanghol)

LING-L545

Practical 04: Train, parse and evaluate using UDPipe


Training the English Model

`./udpipe/src/udpipe --tokenizer none --tagger none --train en.udpipe < ./UD_English-ParTUT/en_partut-ud-train.conllu`


Parse testing data in the English Model

`./udpipe/src/udpipe --parse en.udpipe < ./UD_English-ParTUT/en_partut-ud-test.conllu > TESTINGOUTEN.conllu`


Evaluate parser performance

`python3 ./evaluation_script/conll17_ud_eval.py --verbose ./UD_English-ParTUT/en_partut-ud-test.conllu TESTINGOUTEN.conllu`


Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------|:---------:|----------:|----------:|-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |    100.00 |    100.00 |    100.00 |    100.00
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |    100.00 |    100.00 |    100.00 |    100.00
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |     86.77 |     86.77 |     86.77 |     86.77
LAS        |     85.18 |     85.18 |     85.18 |     85.18


Tree Inspections

1. Transport is tagged as a noun but it is actually an adjective since it is describing 'safety'.
```
# sent_id = en_partut-ud-184
# text = Transport safety has sadly been in the news recently:
1       Transport       transport       NOUN    S       Number=Sing     2       nmod    _       _
2       safety  safety  NOUN    S       Number=Sing     8       nsubj   _       3       has     have    AUX     VA      Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   8       aux     _       _
4       sadly   sadly   ADV     B       _       8       advmod  _       _
5       been    be      AUX     V       Tense=Past|VerbForm=Part        8       cop     _       _
6       in      in      ADP     E       _       8       case    _       _
7       the     the     DET     RD      Definite=Def|PronType=Art       8       det     _       _
8       news    news    NOUN    S       Number=Sing     0       root    _       _
9       recently        recently        ADV     B       _       8       advmod  _       SpaceAfter=No
10      :       :       PUNCT   FC      _       8       punct   _       _
```

2. The tree below has Comédie Humaine separated as two words and tagged with X, meaning the part of speech was undertermined. This should instead be kept together as a pronoun since it is the name of an artwork. 
```
# sent_id = en_partut-ud-1794
# text = "The artist of the Comédie Humaine," he wrote, "is half smothered by the historian.
1       "       "       PUNCT   FB      _       11      punct   _       SpaceAfter=No
2       The     the     DET     RD      Definite=Def|PronType=Art       3       det     _       _
3       artist  artist  NOUN    S       Number=Sing     11      nsubj   _       _
4       of      of      ADP     E       _       6       case    _       _
5       the     the     DET     RD      Definite=Def|PronType=Art       6       det     _       _
6       Comédie Comédie X       SW      Foreign=Yes     3       nmod    _       _
7       Humaine Humaine X       SW      Foreign=Yes     6       flat:foreign    _       SpaceAfter=No                           8       ,       ,       PUNCT   FF      _       3       punct   _       SpaceAfter=No
9       "       "       PUNCT   FB      _       11      punct   _       _
10      he      he      PRON    PE      Gender=Masc|Number=Sing|Person=3|PronType=Prs   11      nsubj   _       _               11      wrote   write   VERB    V       Mood=Ind|Person=3|Tense=Past|VerbForm=Fin       0       root    _       SpaceAfter=No
12      ,       ,       PUNCT   FF      _       11      punct   _       _
13      "       "       PUNCT   FB      _       16      punct   _       SpaceAfter=No
14      is      be      AUX     VA      Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   16      aux:pass        _       _
15      half    half    ADV     B       _       16      advmod  _       _
16      smothered       smother VERB    V       Tense=Past|VerbForm=Part        11      conj    _       _
17      by      by      ADP     E       _       19      case    _       _
18      the     the     DET     RD      Definite=Def|PronType=Art       19      det     _       _
19      historian       historian       NOUN    S       Number=Sing     16      obl     _       SpaceAfter=No
20      .       .       PUNCT   FS      _       11      punct   _       _
```

3. The word 'High' is tagged as an adjective, but it is actually part of the propper noun High Contracting Parties.
```
# sent_id = en_partut-ud-950
# text = This Treaty shall be ratified by the High Contracting Parties in accordance with their respective constitutional requirements.
1       This    this    DET     DD      Number=Sing|PronType=Dem        2       det     _       _
2       Treaty  treaty  NOUN    S       Number=Sing     5       nsubj:pass      _       _
3       shall   shall   AUX     VM      Mood=Ind|Person=3|Tense=Pres|VerbForm=Fin       5       aux     _       _
4       be      be      AUX     VA      VerbForm=Inf    5       aux:pass        _       _
5       ratified        ratify  VERB    V       Tense=Past|VerbForm=Part        0       root    _       _
6       by      by      ADP     E       _       9       case    _       _
7       the     the     DET     RD      Definite=Def|PronType=Art       9       det     _       _
8       High    high    ADJ     A       Degree=Pos      9       amod    _       _
9       Contracting     Contracting     PROPN   SP      _       12      nmod    _       _
10      Parties Parties PROPN   SP      _       9       flat    _       _
11      in      in      ADP     E       _       9       case    _       _
12      accordance      accordance      NOUN    S       Number=Sing     5       obl     _       _
13      with    with    ADP     E       _       17      case    _       _
14      their   their   DET     AP      Poss=Yes|PronType=Prs   17      nmod:poss       _       _
15      respective      respective      ADJ     A       Degree=Pos      17      amod    _       _
16      constitutional  constitutional  ADJ     A       Degree=Pos      17      amod    _       _
17      requirements    requirement     NOUN    S       Number=Plur     5       obl     _       SpaceAfter=No
18      .       .       PUNCT   FS      _       5       punct   _       _
```

4. Here 'programming' should be an adjective and not a noun because it is describing the exercise.
```
# sent_id = en_partut-ud-963
# text = The last programming exercise for the pre-accession assistance referred to in paragraph 1 shall take place in the last year preceding accession.
1       The     the     DET     RD      Definite=Def|PronType=Art       4       det     _       _
2       last    last    ADJ     NO      Degree=Pos|NumType=Ord  4       amod    _       _
3       programming     programming     NOUN    S       Number=Sing     4       nmod    _       _
4       exercise        exercise        NOUN    S       Number=Sing     11      nsubj   _       _
5       for     for     ADP     E       _       10      case    _       _
6       the     the     DET     RD      Definite=Def|PronType=Art       10      det     _       _
7       pre     pre     ADJ     A       Degree=Pos      9       amod    _       SpaceAfter=No
8       -       -       PUNCT   FF      _       7       punct   _       SpaceAfter=No
9       accession       accession       NOUN    S       Number=Sing     10      nmod    _       _
10      assistance      assistance      NOUN    S       Number=Sing     4       nmod    _       _
11      referred        refer   VERB    V       Mood=Ind|Person=3|Tense=Past|VerbForm=Fin       0       root    _       _
12      to      to      ADP     E       _       14      case    _       _
13      in      in      ADP     E       _       14      case    _       _
14      paragraph       paragraph       NOUN    S       Number=Sing     11      obl     _       _
15      1       1       NUM     N       NumType=Card    14      nummod  _       _
16      shall   shall   AUX     VM      Mood=Ind|Person=3|Tense=Pres|VerbForm=Fin       17      aux     _       _
17      take    take    VERB    V       VerbForm=Inf    11      xcomp   _       _
18      place   place   NOUN    S       Number=Sing     17      obj     _       _
19      in      in      ADP     E       _       22      case    _       _
20      the     the     DET     RD      Definite=Def|PronType=Art       22      det     _       _
21      last    last    ADJ     NO      Degree=Pos|NumType=Ord  22      amod    _       _
22      year    year    NOUN    S       Number=Sing     17      obl     _       _
23      preceding       precede VERB    V       Number=Sing|Tense=Pres|VerbForm=Part    22      acl     _       _
24      accession       accession       NOUN    S       Number=Sing     23      obj     _       SpaceAfter=No
```

5. Here 19th and 18th should be adjectives, but they were both separated between the number and the ending "th".
```
# sent_id = en_partut-ud-2050
# text = In the 18th and 19th centuries, his reputation also spread abroad.
1       In      in      ADP     E       _       8       case    _       _
2       the     the     DET     RD      Definite=Def|PronType=Art       8       det     _       _
3       18      18      NUM     N       NumType=Card    8       nummod  _       SpaceAfter=No
4       th      th      ADJ     A       Degree=Pos      8       amod    _       _
5       and     and     CCONJ   CC      _       6       cc      _       _
6       19      19      NUM     N       NumType=Card    4       conj    _       SpaceAfter=No
7       th      th      ADJ     A       Degree=Pos      8       amod    _       _
8       centuries       century NOUN    S       Number=Plur     13      obl     _       SpaceAfter=No
9       ,       ,       PUNCT   FF      _       8       punct   _       _
10      his     his     DET     AP      Poss=Yes|PronType=Prs   11      nmod:poss       _       _
11      reputation      reputation      NOUN    S       Number=Sing     13      nsubj   _       _
12      also    also    ADV     B       _       13      advmod  _       _
13      spread  spread  VERB    V       Mood=Ind|Person=3|Tense=Past|VerbForm=Fin       0       root    _       _
14      abroad  abroad  ADV     B       _       13      advmod  _       SpaceAfter=No
15      .       .       PUNCT   FS      _       13      punct   _       _
```

6. In this tree, both "Henry VIII" and "The Two Noble Kinsmen" should be tagged as proper nouns since they are the names of plays. However, they were split as individual words 
```
# sent_id = en_partut-ud-1939
# text = Shakespeare collaborated on two further surviving plays, Henry VIII and The Two Noble Kinsmen, probably with John Fletcher.
1       Shakespeare     Shakespeare     PROPN   SP      _       2       nsubj   _       _
2       collaborated    collaborate     VERB    V       Mood=Ind|Person=3|Tense=Past|VerbForm=Fin       0       root    _       _
3       on      on      ADP     E       _       7       case    _       _
4       two     two     NUM     N       NumType=Card    7       nummod  _       _
5       further further ADJ     A       _       7       amod    _       _
6       surviving       survive VERB    V       Number=Sing|Tense=Pres|VerbForm=Part    7       acl     _       _               7       plays   play    NOUN    S       Number=Plur     2       obl     _       SpaceAfter=No
8       ,       ,       PUNCT   FF      _       2       punct   _       _
9       Henry   Henry   PROPN   SP      _       2       nmod    _       _
10      VIII    eigth   ADJ     NO      Degree=Pos|NumType=Ord  9       flat    _       _                                       11      and     and     CCONJ   CC      _       14      cc      _       _
12      The     the     DET     RD      Definite=Def|PronType=Art       14      det     _       _
13      Two     two     NUM     N       NumType=Card    14      nummod  _       _
14      Noble   Noble   PROPN   SP      _       9       conj    _       _
15      Kinsmen Kinsmen PROPN   SP      _       14      flat    _       SpaceAfter=No
16      ,       ,       PUNCT   FF      _       14      punct   _       _                                                       17      probably        probably        ADV     B       _       19      advmod  _       _
18      with    with    ADP     E       _       19      case    _       _
19      John    John    PROPN   SP      _       9       nmod    _       _
20      Fletcher        Fletcher        PROPN   SP      _       19      flat    _       SpaceAfter=No                           21      .       .       PUNCT   FS      _       2       punct   _       _
```

7. In this tree, "Court of Justice" is separated into three separate words and given their own tags. However, it should be a single proper noun since "Court of Justice" refers to a named entity. 
```
# sent_id = en_partut-ud-998
# text = The Court of Justice shall make such adaptations to its Rules of Procedure as are rendered necessary by accession.
1       The     the     DET     RD      Definite=Def|PronType=Art       2       det     _       _
2       Court   court   NOUN    S       Number=Sing     6       nsubj   _       _
3       of      of      ADP     E       _       4       case    _       _
4       Justice Justice PROPN   SP      _       2       nmod    _       _
5       shall   shall   AUX     VM      Mood=Ind|Person=3|Tense=Pres|VerbForm=Fin       6       aux     _       _
6       make    make    VERB    V       VerbForm=Inf    0       root    _       _
7       such    such    DET     DD      PronType=Dem    8       det     _       _
8       adaptations     adaptation      NOUN    S       Number=Plur     6       obj     _       _
9       to      to      ADP     E       _       11      case    _       _
10      its     its     DET     AP      Number=Sing|Poss=Yes|PronType=Prs       11      nmod:poss       _       _
11      Rules   rule    NOUN    S       Number=Plur     6       obl     _       _
12      of      of      ADP     E       _       13      case    _       _
13      Procedure       procedure       NOUN    S       Number=Sing     11      nmod    _       _
14      as      as      ADP     E       _       16      mark    _       _
15      are     be      AUX     VA      Mood=Ind|Number=Plur|Tense=Pres|VerbForm=Fin    16      aux:pass        _       _
16      rendered        render  VERB    V       Tense=Past|VerbForm=Part        6       advcl   _       _
17      necessary       necessary       ADJ     A       Degree=Pos      16      xcomp   _       _
18      by      by      ADP     E       _       19      case    _       _
19      accession       accession       NOUN    S       Number=Sing     17      obl     _       SpaceAfter=No
20      .       .       PUNCT   FS      _       6       punct   _       _
```

8. Here the tree tags "General Court" separately as a proper noun and noun. Instead it should be tagged as a poper noun since it is a named entity.
```
# sent_id = en_partut-ud-999
# text = The General Court, in agreement with the Court of Justice, shall make such adaptations to its Rules of Procedure as are rendered necessary by accession.
1       The     the     DET     RD      Definite=Def|PronType=Art       3       det     _       _
2       General General PROPN   SP      _       3       nmod    _       _
3       Court   court   NOUN    S       Number=Sing     14      nsubj   _       SpaceAfter=No
4       ,       ,       PUNCT   FF      _       3       punct   _       _
5       in      in      ADP     E       _       6       case    _       _                                                       6       agreement       agreement       NOUN    S       Number=Sing     3       nmod    _       _
7       with    with    ADP     E       _       9       case    _       _
8       the     the     DET     RD      Definite=Def|PronType=Art       9       det     _       _
9       Court   court   NOUN    S       Number=Sing     6       nmod    _       _
10      of      of      ADP     E       _       11      case    _       _
11      Justice Justice PROPN   SP      _       9       nmod    _       SpaceAfter=No
12      ,       ,       PUNCT   FF      _       3       punct   _       _
13      shall   shall   AUX     VM      Mood=Ind|Person=3|Tense=Pres|VerbForm=Fin       14      aux     _       _
14      make    make    VERB    V       VerbForm=Inf    0       root    _       _
15      such    such    DET     DD      PronType=Dem    16      det     _       _
16      adaptations     adaptation      NOUN    S       Number=Plur     14      obj     _       _
17      to      to      ADP     E       _       19      case    _       _
18      its     its     DET     AP      Number=Sing|Poss=Yes|PronType=Prs       19      nmod:poss       _       _
19      Rules   rule    NOUN    S       Number=Plur     14      obl     _       _
20      of      of      ADP     E       _       21      case    _       _
21      Procedure       procedure       NOUN    S       Number=Sing     19      nmod    _       _
22      as      as      ADP     E       _       24      mark    _       _
23      are     be      AUX     VA      Mood=Ind|Number=Plur|Tense=Pres|VerbForm=Fin    24      aux:pass        _       _
24      rendered        render  VERB    V       Tense=Past|VerbForm=Part        14      advcl   _       _
25      necessary       necessary       ADJ     A       Degree=Pos      24      xcomp   _       _
26      by      by      ADP     E       _       27      case    _       _
27      accession       accession       NOUN    S       Number=Sing     25      obl     _       SpaceAfter=No
28      .       .       PUNCT   FS      _       14      punct   _       _
```

9. This tree has "Court of Auditors" slipt into three tokens with their corresponding tags. This should be one token tagged as a proper noun since it is a named entity.
```
# sent_id = en_partut-ud-1001
# text = A national of each new Member State shall be appointed to the Court of Auditors as from the date of accession for a term of office of six years.
1       A       a       DET     RI      Definite=Ind|Number=Sing|PronType=Art   2       det     _       _
2       national        national        NOUN    S       Number=Sing     10      nsubj:pass      _       _
3       of      of      ADP     E       _       7       case    _       _
4       each    each    DET     DI      Number=Sing|PronType=Ind        7       det     _       _
5       new     new     ADJ     A       Degree=Pos      6       amod    _       _
6       Member  member  NOUN    S       Number=Sing     7       compound        _       _
7       State   state   NOUN    S       Number=Sing     2       nmod    _       _
8       shall   shall   AUX     VM      Mood=Ind|Person=3|Tense=Pres|VerbForm=Fin       10      aux     _       _
9       be      be      AUX     VA      VerbForm=Inf    10      aux:pass        _       _
10      appointed       appoint VERB    V       Tense=Past|VerbForm=Part        0       root    _       _
11      to      to      ADP     E       _       13      case    _       _
12      the     the     DET     RD      Definite=Def|PronType=Art       13      det     _       _
13      Court   court   NOUN    S       Number=Sing     10      obl     _       _
14      of      of      ADP     E       _       15      case    _       _
15      Auditors        auditor NOUN    S       Number=Plur     13      nmod    _       _
16      as      as      ADP     E       _       19      case    _       _
17      from    from    ADP     E       _       16      fixed   _       _
18      the     the     DET     RD      Definite=Def|PronType=Art       19      det     _       _
19      date    date    NOUN    S       Number=Sing     10      obl     _       _
20      of      of      ADP     E       _       21      case    _       _
21      accession       accession       NOUN    S       Number=Sing     19      nmod    _       _
22      for     for     ADP     E       _       24      case    _       _
23      a       a       DET     RI      Definite=Ind|Number=Sing|PronType=Art   24      det     _       _
24      term    term    NOUN    S       Number=Sing     21      nmod    _       _
25      of      of      ADP     E       _       26      case    _       _
26      office  office  NOUN    S       Number=Sing     24      nmod    _       _
27      of      of      ADP     E       _       29      case    _       _
28      six     six     NUM     N       NumType=Card    29      nummod  _       _
29      years   year    NOUN    S       Number=Plur     26      nmod    _       SpaceAfter=No
30      .       .       PUNCT   FS      _       10      punct   _       _
```

10. This tree should have "Council" tagged as a proper noun since it is a named entitiy. However, it was tagged as a noun. 
```
# sent_id = en_partut-ud-1000
# text = The Rules of Procedure as adapted shall require the consent of the Council.
1       The     the     DET     RD      Definite=Def|PronType=Art       2       det     _       _
2       Rules   rule    NOUN    S       Number=Plur     8       nsubj   _       _                                               3       of      of      ADP     E       _       4       case    _       _
4       Procedure       procedure       NOUN    S       Number=Sing     2       nmod    _       _
5       as      as      ADP     E       _       6       mark    _       _
6       adapted adapt   VERB    V       Mood=Ind|Person=3|Tense=Past|VerbForm=Fin       2       acl     _       _
7       shall   shall   AUX     VM      Mood=Ind|Person=3|Tense=Pres|VerbForm=Fin       8       aux     _       _               8       require require VERB    V       VerbForm=Inf    0       root    _       _                                               9       the     the     DET     RD      Definite=Def|PronType=Art       10      det     _       _                               10      consent consent NOUN    S       Number=Sing     8       obj     _       _
11      of      of      ADP     E       _       13      case    _       _                                                       12      the     the     DET     RD      Definite=Def|PronType=Art       13      det     _       _
13      Council Council NOUN    S       Number=Sing     10      nmod    _       SpaceAfter=No
14      .       .       PUNCT   FS      _       8       punct   _       _
```
