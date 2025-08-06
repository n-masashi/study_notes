```text
mysql> SELECT *
    -> FROM film
    -> WHERE release_year IS NULL;
+---------+------------------------+-------------------------------------------------------------------------------------------------------------------------+-------------+--------------+-----------------+-------------+--------+------------------+--------+
| film_id | title                  | description                                                                                                             | category_id | release_year | rental_duration | rental_rate | length | replacement_cost | rating |
+---------+------------------------+-------------------------------------------------------------------------------------------------------------------------+-------------+--------------+-----------------+-------------+--------+------------------+--------+
|      21 | AMERICAN CIRCUS        | A Insightful Drama of a Girl And a Astronaut who must Face a Database Administrator in A Shark Tank                     |           8 |         NULL |               3 |        4.99 |    129 |            17.99 | NULL   |
|      32 | APOCALYPSE FLAMINGOS   | A Astounding Story of a Dog And a Squirrel who must Defeat a Woman in An Abandoned Amusement Park                       |           3 |         NULL |               6 |        4.99 |    119 |            11.99 | R      |
|      36 | ARGONAUTS TOWN         | A Emotional Epistle of a Forensic Psychologist And a Butler who must Challenge a Waitress in An Abandoned Mine Shaft    |           6 |         NULL |               7 |        0.99 |    127 |            12.99 | PG-13  |
|      48 | BACKLASH UNDEFEATED    | A Stunning Character Study of a Mad Scientist And a Mad Cow who must Kill a Car in A Monastery                          |          11 |         NULL |               3 |        4.99 |    118 |            24.99 | PG-13  |
|      92 | BOWFINGER GABLES       | A Fast-Paced Yarn of a Waitress And a Composer who must Outgun a Dentist in California                                  |          11 |         NULL |               7 |        4.99 |     72 |            19.99 | NC-17  |
|      94 | BRAVEHEART HUMAN       | A Insightful Story of a Dog And a Pastry Chef who must Battle a Girl in Berlin                                          |          10 |         NULL |               7 |        2.99 |    176 |            14.99 | PG-13  |
|     111 | CADDYSHACK JEDI        | A Awe-Inspiring Epistle of a Woman And a Madman who must Fight a Robot in Soviet Georgia                                |           5 |         NULL |               3 |        0.99 |     52 |            17.99 | NULL   |
|     113 | CALIFORNIA BIRDS       | A Thrilling Yarn of a Database Administrator And a Robot who must Battle a Database Administrator in Ancient India      |           8 |         NULL |               4 |        4.99 |     75 |            19.99 | NC-17  |
|     146 | CHITTY LOCK            | A Boring Epistle of a Boat And a Database Administrator who must Kill a Sumo Wrestler in The First Manned Space Station |          15 |         NULL |               6 |        2.99 |    107 |            24.99 | G      |
|     174 | CONFIDENTIAL INTERVIEW | A Stunning Reflection of a Cat And a Woman who must Find a Astronaut in Ancient Japan                                   |           5 |         NULL |               6 |        4.99 |    180 |            13.99 | NULL   |
|     284 | ENEMY ODDS             | A Fanciful Panorama of a Mad Scientist And a Woman who must Pursue a Astronaut in Ancient India                         |          10 |         NULL |               5 |        4.99 |     77 |            23.99 | NULL   |
|     290 | EVERYONE CRAFT         | A Fateful Display of a Waitress And a Dentist who must Reach a Butler in Nigeria                                        |          13 |         NULL |               4 |        0.99 |    163 |            29.99 | PG     |
|     317 | FIREBALL PHILADELPHIA  | A Amazing Yarn of a Dentist And a A Shark who must Vanquish a Madman in An Abandoned Mine Shaft                         |           4 |         NULL |               4 |        0.99 |    148 |            25.99 | PG     |
|     320 | FLAMINGOS CONNECTICUT  | A Fast-Paced Reflection of a Composer And a Composer who must Meet a Cat in The Sahara Desert                           |           3 |         NULL |               4 |        4.99 |     80 |            28.99 | PG-13  |
|     321 | FLASH WARS             | A Astounding Saga of a Moose And a Pastry Chef who must Chase a Student in The Gulf of Mexico                           |           1 |         NULL |               3 |        4.99 |    123 |            21.99 | NULL   |
|     353 | GENTLEMEN STAGE        | A Awe-Inspiring Reflection of a Monkey And a Student who must Overcome a Dentist in The First Manned Space Station      |           6 |         NULL |               6 |        2.99 |    125 |            22.99 | NULL   |
|     363 | GO PURPLE              | A Fast-Paced Display of a Car And a Database Administrator who must Battle a Woman in A Baloon                          |          11 |         NULL |               3 |        0.99 |     54 |            12.99 | NULL   |
|     371 | GOSFORD DONNIE         | A Epic Panorama of a Mad Scientist And a Monkey who must Redeem a Secret Agent in Berlin                                |           2 |         NULL |               5 |        4.99 |    129 |            17.99 | G      |
|     374 | GRAFFITI LOVE          | A Unbelieveable Epistle of a Sumo Wrestler And a Hunter who must Build a Composer in Berlin                             |          10 |         NULL |               3 |        0.99 |    117 |            29.99 | PG     |
|     401 | HAROLD FRENCH          | A Stunning Saga of a Sumo Wrestler And a Student who must Outrace a Moose in The Sahara Desert                          |          14 |         NULL |               6 |        0.99 |    168 |            10.99 | NULL   |
|     403 | HARRY IDAHO            | A Taut Yarn of a Technical Writer And a Feminist who must Outrace a Dog in California                                   |           7 |         NULL |               5 |        4.99 |    121 |            18.99 | NULL   |
|     434 | HORROR REIGN           | A Touching Documentary of a A Shark And a Car who must Build a Husband in Nigeria                                       |           9 |         NULL |               3 |        0.99 |    139 |            25.99 | NULL   |
|     442 | HUNTING MUSKETEERS     | A Thrilling Reflection of a Pioneer And a Dentist who must Outrace a Womanizer in An Abandoned Mine Shaft               |          12 |         NULL |               6 |        2.99 |     65 |            24.99 | NC-17  |
|     456 | INCH JET               | A Fateful Saga of a Womanizer And a Student who must Defeat a Butler in A Monastery                                     |          13 |         NULL |               6 |        4.99 |    167 |            18.99 | NULL   |
+---------+------------------------+-------------------------------------------------------------------------------------------------------------------------+-------------+--------------+-----------------+-------------+--------+------------------+--------+
24 rows in set (0.00 sec)
```

```text
mysql> SELECT *
    -> FROM sales
    -> WHERE book_id = 20;
+----------+---------------------+--------+---------+----------+
| sales_id | sales_date          | amount | book_id | staff_id |
+----------+---------------------+--------+---------+----------+
|      229 | 2019-01-12 12:24:50 |  23.49 |      20 |        3 |
|      477 | 2019-01-23 17:51:33 |  23.49 |      20 |        3 |
|      945 | 2019-02-12 19:55:06 |  23.49 |      20 |        2 |
|     1001 | 2019-02-14 20:15:48 |  23.49 |      20 |        2 |
|     1102 | 2019-02-19 12:38:38 |  23.49 |      20 |        3 |
|     1422 | 2019-03-05 18:07:05 |  23.49 |      20 |        3 |
|     2137 | 2019-04-06 17:44:55 |  23.49 |      20 |        4 |
|     4193 | 2019-06-29 14:51:04 |  23.49 |      20 |        1 |
|     4614 | 2019-07-15 15:13:45 |  23.49 |      20 |        4 |
|     5220 | 2019-08-10 17:26:57 |  23.49 |      20 |        1 |
|     5609 | 2019-08-25 15:19:50 |  23.49 |      20 |        1 |
|     7935 | 2019-11-23 14:13:23 |  23.49 |      20 |        2 |
|     8161 | 2019-12-01 16:12:13 |  23.49 |      20 |        3 |
|     9892 | 2020-02-05 17:36:08 |  23.49 |      20 |        1 |
|    11874 | 2020-04-14 14:48:25 |  23.49 |      20 |        1 |
|    12446 | 2020-05-03 17:51:21 |  23.49 |      20 |        4 |
|    14403 | 2020-07-07 17:29:41 |  23.49 |      20 |        1 |
|    14946 | 2020-07-26 15:28:55 |  23.49 |      20 |        1 |
|    15116 | 2020-07-31 19:28:02 |  23.49 |      20 |        2 |
|    15619 | 2020-08-18 09:29:34 |  23.49 |      20 |        1 |
|    15646 | 2020-08-18 18:47:58 |  23.49 |      20 |        1 |
|    15947 | 2020-08-27 12:55:31 |  23.49 |      20 |        2 |
|    16257 | 2020-09-06 15:29:36 |  23.49 |      20 |        3 |
|    17443 | 2020-10-13 14:48:39 |  23.49 |      20 |        4 |
|    18410 | 2020-11-12 20:27:39 |  23.49 |      20 |        1 |
|    18950 | 2020-11-29 12:12:53 |  23.49 |      20 |        4 |
|    19789 | 2020-12-25 12:28:07 |  23.49 |      20 |        4 |
+----------+---------------------+--------+---------+----------+
27 rows in set (0.01 sec)
```
```text
mysql> SELECT *
    -> FROM film
    -> WHERE
    ->    length BETWEEN 85 AND 95
    -> LIMIT 5;
+---------+----------------------+-----------------------------------------------------------------------------------------------------------+-------------+--------------+-----------------+-------------+--------+------------------+--------+
| film_id | title                | description                                                                                               | category_id | release_year | rental_duration | rental_rate | length | replacement_cost | rating |
+---------+----------------------+-----------------------------------------------------------------------------------------------------------+-------------+--------------+-----------------+-------------+--------+------------------+--------+
|       1 | ACADEMY DINOSAUR     | A Epic Drama of a Feminist And a Mad Scientist who must Battle a Teacher in The Canadian Rockies          |           7 |         1998 |               6 |        0.99 |     86 |            20.99 | PG     |
|      14 | ALICE FANTASIA       | A Emotional Drama of a A Shark And a Database Administrator who must Vanquish a Pioneer in Soviet Georgia |           1 |         1976 |               6 |        0.99 |     94 |            23.99 | NC-17  |
|      22 | AMISTAD MIDSUMMER    | A Emotional Character Study of a Dentist And a Crocodile who must Meet a Sumo Wrestler in California      |          14 |         2005 |               6 |        2.99 |     85 |            10.99 | NULL   |
|      23 | ANACONDA CONFESSIONS | A Lacklusture Display of a Dentist And a Dentist who must Fight a Girl in Australia                       |           7 |         1999 |               3 |        0.99 |     92 |             9.99 | R      |
|      26 | ANNIE IDENTITY       | A Amazing Panorama of a Pastry Chef And a Boat who must Escape a Woman in An Abandoned Amusement Park     |           2 |         1996 |               3 |        0.99 |     86 |            15.99 | G      |
+---------+----------------------+-----------------------------------------------------------------------------------------------------------+-------------+--------------+-----------------+-------------+--------+------------------+--------+
5 rows in set (0.00 sec)
```
```text
mysql> SELECT *
    -> FROM film
    -> WHERE
    ->    length >= 85 AND length <= 95
    -> LIMIT 5;
+---------+----------------------+-----------------------------------------------------------------------------------------------------------+-------------+--------------+-----------------+-------------+--------+------------------+--------+
| film_id | title                | description                                                                                               | category_id | release_year | rental_duration | rental_rate | length | replacement_cost | rating |
+---------+----------------------+-----------------------------------------------------------------------------------------------------------+-------------+--------------+-----------------+-------------+--------+------------------+--------+
|       1 | ACADEMY DINOSAUR     | A Epic Drama of a Feminist And a Mad Scientist who must Battle a Teacher in The Canadian Rockies          |           7 |         1998 |               6 |        0.99 |     86 |            20.99 | PG     |
|      14 | ALICE FANTASIA       | A Emotional Drama of a A Shark And a Database Administrator who must Vanquish a Pioneer in Soviet Georgia |           1 |         1976 |               6 |        0.99 |     94 |            23.99 | NC-17  |
|      22 | AMISTAD MIDSUMMER    | A Emotional Character Study of a Dentist And a Crocodile who must Meet a Sumo Wrestler in California      |          14 |         2005 |               6 |        2.99 |     85 |            10.99 | NULL   |
|      23 | ANACONDA CONFESSIONS | A Lacklusture Display of a Dentist And a Dentist who must Fight a Girl in Australia                       |           7 |         1999 |               3 |        0.99 |     92 |             9.99 | R     |
|      26 | ANNIE IDENTITY       | A Amazing Panorama of a Pastry Chef And a Boat who must Escape a Woman in An Abandoned Amusement Park     |           2 |         1996 |               3 |        0.99 |     86 |            15.99 | G     |
+---------+----------------------+-----------------------------------------------------------------------------------------------------------+-------------+--------------+-----------------+-------------+--------+------------------+--------+
5 rows in set (0.00 sec)
```
```text
mysql> SELECT *
    -> FROM film
    -> WHERE
    ->     NOT (rating = 'NC-17' OR rating IS NULL)
    -> LIMIT 5;
+---------+------------------+-----------------------------------------------------------------------------------------------------------------------+-------------+--------------+-----------------+-------------+--------+------------------+--------+
| film_id | title            | description                                                                                                           | category_id | release_year | rental_duration | rental_rate | length | replacement_cost | rating |
+---------+------------------+-----------------------------------------------------------------------------------------------------------------------+-------------+--------------+-----------------+-------------+--------+------------------+--------+
|       1 | ACADEMY DINOSAUR | A Epic Drama of a Feminist And a Mad Scientist who must Battle a Teacher in The Canadian Rockies                      |           7 |         1998 |               6 |        0.99 |     86 |            20.99 | PG     |
|       2 | ACE GOLDFINGER   | A Astounding Epistle of a Database Administrator And a Explorer who must Find a Car in Ancient China                  |           3 |         2001 |               3 |        4.99 |     48 |            12.99 | G      |
|       4 | AFFAIR PREJUDICE | A Fanciful Documentary of a Frisbee And a Lumberjack who must Chase a Monkey in A Shark Tank                          |        NULL |         1990 |               5 |        2.99 |    117 |            26.99 | G      |
|       5 | AFRICAN EGG      | A Fast-Paced Documentary of a Pastry Chef And a Dentist who must Pursue a Forensic Psychologist in The Gulf of Mexico |           4 |         1996 |               6 |        2.99 |    130 |            22.99 | G      |
|       6 | AGENT TRUMAN     | A Intrepid Panorama of a Robot And a Boy who must Escape a Sumo Wrestler in Ancient China                             |          10 |         2002 |               3 |        2.99 |    169 |            17.99 | PG     |
+---------+------------------+-----------------------------------------------------------------------------------------------------------------------+-------------+--------------+-----------------+-------------+--------+------------------+--------+
5 rows in set (0.00 sec)
```
