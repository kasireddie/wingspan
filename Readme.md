# Data/Software Engineering Take-Home Exam

Before running the scheduler and API, you need to install some python modules that were used in the software. These are listed in the following subsection.

## Dependencies

### Schedule Library

Schedule is used to schedule a task at a particular time every day or a particular day of a week. We can also set time in 24 hours format that when a task should run. Basically, Schedule Library matches the systems time to that of scheduled time set by the user. Once the scheduled time and system time matches the job function (command function that is scheduled) is called. The module can be installed by running the following command:

```
pip install schedule
```

### Pexpect Library

Pexpect is a pure Python module for spawning child applications; controlling them; and responding to expected patterns in their output. Here, we will use it to call pg_dump and backup the PostgreSQL database. The module can be installed by running the following command:

```
pip install pexpect
```

### Bottle Library

Bottle is the micro web-framework used to create the API. It is distributed as a single file module and has no dependencies other than the Python Standard Library. The module can be installed by running the following command:

```
pip install bottle
```


