# SQL More Queries Tasks

This repository contains scripts for various tasks related to MySQL database management and user privileges. Each task is described below along with the filename of the corresponding script.

## Task 0 - My Privileges!

**Filename:** `0-privileges.sql`

**Description:**
A script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the local server (localhost). The script attempts to grant the required privileges if they are missing.

## Task 1 - Root User

**Filename:** `1-create_user.sql`

**Description:**
A script that creates the MySQL server user `user_0d_1`. This user is granted all privileges on the MySQL server, and its password is set to `user_0d_1_pwd`. If the user `user_0d_1` already exists, the script will not fail.

## Task 2 - Read User

**Filename:** `2-create_read_user.sql`

**Description:**
A script that creates the database `hbtn_0d_2` and the user `user_0d_2`. The `user_0d_2` user is granted only the SELECT privilege on the `hbtn_0d_2` database. The password for `user_0d_2` is set to `user_0d_2_pwd`. If the database `hbtn_0d_2` or the user `user_0d_2` already exists, the script will not fail.

## Task 3 - Always a Name

**Filename:** `3-force_name.sql`

**Description:**
A script that creates the table `force_name` on the MySQL server. The `force_name` table has two columns: `id` (INT) and `name` (VARCHAR(256)), where the `name` column cannot be null. The database name is passed as an argument to the `mysql` command. If the `force_name` table already exists, the script will not fail.

## Task 4 - ID Can't be Null

**Filename:** `4-never_empty.sql`

**Description:**
A script that creates the table `id_not_null` on the MySQL server. The `id_not_null` table has two columns: `id` (INT with default value 1) and `name` (VARCHAR(256)). If the table `id_not_null` already exists, the script will not fail.

## Task 5 - Unique ID

**Filename:** `5-unique_id.sql`

**Description:**
A script that creates the table `unique_id` on the MySQL server. The `unique_id` table has two columns: `id` (INT with default value 1 and must be unique) and `name` (VARCHAR(256)). If the table `unique_id` already exists, the script will not fail.

# SQL More Queries Tasks (Continued)

This repository contains scripts for various tasks related to MySQL database management and querying. Each task is described below along with the filename of the corresponding script.

## Task 6 - States Table

**Filename:** `6-states.sql`

**Description:**
A script that creates the database `hbtn_0d_usa` and the table `states` within the database on the MySQL server. The `states` table has two columns: `id` (INT) which is unique, auto-generated, and cannot be null (it is the primary key), and `name` (VARCHAR(256)) which cannot be null. If the database `hbtn_0d_usa` or the table `states` already exists, the script will not fail.

## Task 7 - Cities Table

**Filename:** `7-cities.sql`

**Description:**
A script that creates the database `hbtn_0d_usa` and the table `cities` within the database on the MySQL server. The `cities` table has three columns: `id` (INT) which is unique, auto-generated, and cannot be null (it is the primary key), `state_id` (INT) which cannot be null and must be a FOREIGN KEY that references the `id` column of the `states` table, and `name` (VARCHAR(256)) which cannot be null. If the database `hbtn_0d_usa` or the table `cities` already exists, the script will not fail.

## Task 8 - Cities of California

**Filename:** `8-cities_of_california_subquery.sql`

**Description:**
A script that lists all the cities of California found in the database `hbtn_0d_usa`. The script uses a subquery and does not use the JOIN keyword. The results are sorted in ascending order by `cities.id`.

## Task 9 - Cities by States

**Filename:** `9-cities_by_state_join.sql`

**Description:**
A script that lists all cities contained in the database `hbtn_0d_usa` along with their corresponding state names. The script uses the JOIN keyword to retrieve information from the `cities` and `states` tables. The results are sorted in ascending order by `cities.id`.

## Task 10 - Genre ID by Show

**Filename:** `10-genre_id_by_show.sql`

**Description:**
A script that lists all shows contained in the database `hbtn_0d_tvshows` that have at least one genre linked. The script displays the TV show title and its corresponding genre ID. The results are sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`.

## Task 11 - Genre ID for all Shows

**Filename:** `11-genre_id_all_shows.sql`

**Description:**
A script that lists all shows contained in the database `hbtn_0d_tvshows`. The script displays the TV show title and its corresponding genre ID. If a show doesn’t have a genre, the genre ID is displayed as NULL. The results are sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`.

## Task 12 - No Genre

**Filename:** `12-no_genre.sql`

**Description:**
A script that lists all shows contained in the database `hbtn_0d_tvshows` without a genre linked. The script displays the TV show title and its corresponding genre ID. The results are sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`.

## Task 13 - Number of Shows by Genre

**Filename:** `13-count_shows_by_genre.sql`

**Description:**
A script that lists all genres from the database `hbtn_0d_tvshows` and displays the number of shows linked to each genre. The script displays the genre name and the number of shows linked to that genre. The results are sorted in descending order by the number of shows linked.

## Task 14 - My Genres

**Filename:** `14-my_genres.sql`

**Description:**
A script that lists all genres of the show "Dexter" from the database `hbtn_0d_tvshows`. The script displays the genre names. The results are sorted in ascending order by the genre name.

## Task 15 - Only Comedy

**Filename:** `15-comedy_only.sql`

**Description:**
A script that lists all Comedy shows in the database `hbtn_0d_tvshows`. The script displays the titles of the Comedy shows. The results are sorted in ascending order by the show title.

## Task 16 - List Shows and Genres

**Filename:** `16-shows_by_genre.sql`

**Description:**
A script that lists all shows and all genres linked to each show from the database `hbtn_0d_tvshows`. If a show doesn’t have a genre, the genre column displays NULL. The script displays the show title and its corresponding genre name. The results are sorted in ascending order by the show title and genre name.
