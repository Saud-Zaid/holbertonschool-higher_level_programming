# Python - Object-relational mapping

This project introduces Object-Relational Mapping (ORM) and connecting Python scripts to MySQL databases using `MySQLdb` and `SQLAlchemy`.

## Tasks

| File | Description |
| ---- | ----------- |
| [0-select_states.py](./0-select_states.py) | Lists all states from the database `hbtn_0e_0_usa`, sorted by `states.id` in ascending order. |
| [1-filter_states.py](./1-filter_states.py) | Lists all states with a name starting with `N` (upper N) from `hbtn_0e_0_usa`. |
| [2-my_filter_states.py](./2-my_filter_states.py) | Displays all values in the `states` table where `name` matches the argument using string formatting. |
| [3-my_safe_filter_states.py](./3-my_safe_filter_states.py) | Displays all values in the `states` table matching the argument, safe from MySQL injection. |
| [4-cities_by_state.py](./4-cities_by_state.py) | Lists all cities from `hbtn_0e_4_usa` with their corresponding state names using a single `execute()`. |
| [5-filter_cities.py](./5-filter_cities.py) | Lists all cities of a given state from `hbtn_0e_4_usa`, safe from SQL injection. |
| [model_state.py](./model_state.py) | Contains class definition of `State` and instance `Base = declarative_base()`. |
| [7-model_state_fetch_all.py](./7-model_state_fetch_all.py) | Lists all `State` objects from `hbtn_0e_6_usa` via SQLAlchemy. |
| [8-model_state_fetch_first.py](./8-model_state_fetch_first.py) | Prints the first `State` object from `hbtn_0e_6_usa` via SQLAlchemy. |
| [9-model_state_filter_a.py](./9-model_state_filter_a.py) | Lists all `State` objects that contain the letter `a` from `hbtn_0e_6_usa`. |
| [10-model_state_my_get.py](./10-model_state_my_get.py) | Prints the `State` object with the name passed as argument from `hbtn_0e_6_usa`. |
| [11-model_state_insert.py](./11-model_state_insert.py) | Adds the `State` object "Louisiana" to `hbtn_0e_6_usa` and prints its `id`. |
| [12-model_state_update_id_2.py](./12-model_state_update_id_2.py) | Changes the name of the `State` object where `id = 2` to "New Mexico". |
| [13-model_state_delete_a.py](./13-model_state_delete_a.py) | Deletes all `State` objects with a name containing the letter `a`. |
| [model_city.py](./model_city.py) | Contains class definition of `City` linking to `cities` table with foreign key to `states.id`. |
| [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py) | Prints all `City` objects from `hbtn_0e_14_usa` ordered by `cities.id`. |
