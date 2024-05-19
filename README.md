# General

The project was developed in Linux Ubuntu 22.04. The python version 3.6.15 was used and the SQLite database engine for storing data.

## Setting up dependencies

We are using venv for the python dependencies so no need to install anything. Just execute the following to you cmd:

```bash
source venv/bin/activate
```

## Running the script

For importing today's currencies run

```bash
python main.py
```

For importing currencies from 2024-01-01 to 2024-01-15

```bash
python main.py 2024-01-01 2022-01-15
```

## Implementation

I used an abstract class `DataPipeline` for a general pipeline interface. Every pipeline should implement this class behaviour and override the callback functions.
If we want to run a pipeline we should use the `PipelineManager` class given as attributes the pipeline implementation and the worker(ex. SQLite, Postgres etc.).
I could also create an abstract class for the worker behaviour but it was premature optimization which is the root of all evil.
The `PipelineManager` acts as a Factory. It is responsible for the followings:
- Run the pipeline implementation
- Execute general code for every pipeline for example saving Telemetry events and logging usefull information throught ETL stages.

I tried to seperate code functionality like wrappers(`3rd party APIs`), utils(`datetime_helpers`) and schemas(`Currency`) without making the project's directory
complicated and keeping things as simple as possible. As the project gets bigger more directories will be created and some classes may break to more abstract methods with the art of refactoring.
Till then we try to keep things as stupid(simple) as we can. No need to create complicated fancy designs.

## Crontab entry

```
45 5 * * * python path_to_project/main.py
```