The operation is load

The output is: 

|    |   Survived |   Pclass | Name                                               | Sex    |   Age |   Siblings/Spouses Aboard |   Parents/Children Aboard |    Fare |
|---:|-----------:|---------:|:---------------------------------------------------|:-------|------:|--------------------------:|--------------------------:|--------:|
|  0 |          0 |        3 | Mr. Owen Harris Braund                             | male   |    22 |                         1 |                         0 |  7.25   |
|  1 |          1 |        1 | Mrs. John Bradley (Florence Briggs Thayer) Cumings | female |    38 |                         1 |                         0 | 71.2833 |
|  2 |          1 |        3 | Miss. Laina Heikkinen                              | female |    26 |                         0 |                         0 |  7.925  |
|  3 |          1 |        1 | Mrs. Jacques Heath (Lily May Peel) Futrelle        | female |    35 |                         1 |                         0 | 53.1    |
|  4 |          0 |        3 | Mr. William Henry Allen                            | male   |    35 |                         0 |                         0 |  8.05   |
|  5 |          0 |        3 | Mr. James Moran                                    | male   |    27 |                         0 |                         0 |  8.4583 |
|  6 |          0 |        1 | Mr. Timothy J McCarthy                             | male   |    54 |                         0 |                         0 | 51.8625 |
|  7 |          0 |        3 | Master. Gosta Leonard Palsson                      | male   |     2 |                         3 |                         1 | 21.075  |
|  8 |          1 |        3 | Mrs. Oscar W (Elisabeth Vilhelmina Berg) Johnson   | female |    27 |                         0 |                         2 | 11.1333 |
|  9 |          1 |        2 | Mrs. Nicholas (Adele Achem) Nasser                 | female |    14 |                         1 |                         0 | 30.0708 |

The operation is summary data

The output is: 

|    | summary   |   Survived |     Pclass | Name                                                    | Sex    |      Age |   Siblings/Spouses Aboard |   Parents/Children Aboard |     Fare |
|---:|:----------|-----------:|-----------:|:--------------------------------------------------------|:-------|---------:|--------------------------:|--------------------------:|---------:|
|  0 | count     | 887        | 887        | 887                                                     | 887    | 887      |                887        |                887        | 887      |
|  1 | mean      |   0.385569 |   2.30552  |                                                         |        |  29.4714 |                  0.525366 |                  0.383315 |  32.3054 |
|  2 | stddev    |   0.487004 |   0.836662 |                                                         |        |  14.1219 |                  1.10467  |                  0.807466 |  49.782  |
|  3 | min       |   0        |   1        | Capt. Edward Gifford Crosby                             | female |   0.42   |                  0        |                  0        |   0      |
|  4 | max       |   1        |   3        | the Countess. of (Lucy Noel Martha Dyer-Edwards) Rothes | male   |  80      |                  8        |                  6        | 512.329  |

The operation is query

The query is SELECT Pclass, COUNT(*) as Count FROM TitanicData GROUP BY Pclass ORDER BY Pclass

The output is: 

|    |   Pclass |   Count |
|---:|---------:|--------:|
|  0 |        1 |     216 |
|  1 |        2 |     184 |
|  2 |        3 |     487 |

The operation is transform

The output is: 

|    |   Survived |   Pclass | Name                                               | Sex    |   Age |   Siblings/Spouses Aboard |   Parents/Children Aboard |    Fare | Age_Group   |
|---:|-----------:|---------:|:---------------------------------------------------|:-------|------:|--------------------------:|--------------------------:|--------:|:------------|
|  0 |          0 |        3 | Mr. Owen Harris Braund                             | male   |    22 |                         1 |                         0 |  7.25   | Adult       |
|  1 |          1 |        1 | Mrs. John Bradley (Florence Briggs Thayer) Cumings | female |    38 |                         1 |                         0 | 71.2833 | Adult       |
|  2 |          1 |        3 | Miss. Laina Heikkinen                              | female |    26 |                         0 |                         0 |  7.925  | Adult       |
|  3 |          1 |        1 | Mrs. Jacques Heath (Lily May Peel) Futrelle        | female |    35 |                         1 |                         0 | 53.1    | Adult       |
|  4 |          0 |        3 | Mr. William Henry Allen                            | male   |    35 |                         0 |                         0 |  8.05   | Adult       |
|  5 |          0 |        3 | Mr. James Moran                                    | male   |    27 |                         0 |                         0 |  8.4583 | Adult       |
|  6 |          0 |        1 | Mr. Timothy J McCarthy                             | male   |    54 |                         0 |                         0 | 51.8625 | Adult       |
|  7 |          0 |        3 | Master. Gosta Leonard Palsson                      | male   |     2 |                         3 |                         1 | 21.075  | Child       |
|  8 |          1 |        3 | Mrs. Oscar W (Elisabeth Vilhelmina Berg) Johnson   | female |    27 |                         0 |                         2 | 11.1333 | Adult       |
|  9 |          1 |        2 | Mrs. Nicholas (Adele Achem) Nasser                 | female |    14 |                         1 |                         0 | 30.0708 | Child       |

