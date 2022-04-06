### The folder above contain a todo list built with django. It functionalities are follows
 1. It can create a todo
 2. Delete the todo
 3. Create list for specific todo
 4. delete the list for any todo
 5. changes are after auto refresh
    The database used for this application was postgresql.
    
### The database foreign key was used as a varchar instead of the default which is int. This is also because the database was built at first using sqlite3 and the way the todo connects to the list is by the todo name. Changing it to get by id would require extra working.