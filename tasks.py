
import os

from invoke import task


@task(default=True)
def run_smalls(context):
    # python_path = os.pathsep.join(["src", "src"])
    command = f"streamlit run Homepage.py"
    context.run(command, echo=True)


@task
def run_small(context):
    python_path = os.pathsep.join(["tests", "src"])
    command = f"PYTHONPATH={python_path} python3 -m unittest small -v --failfast"
    context.run(command, echo=True)

@task
def run_medium(context):
    python_path = os.pathsep.join(["tests", "src"])
    command = f"PYTHONPATH={python_path} python3 -m unittest medium -v --failfast"
    context.run(command, echo=True)

@task
def run_large(context):
    python_path = os.pathsep.join(["tests", "src"])
    command = f"PYTHONPATH={python_path} python3 -m unittest large -v --failfast"
    context.run(command, echo=True)

@task
def run_smoke(context):
    python_path = os.pathsep.join(["tests", "src"])
    command = f"PYTHONPATH={python_path} python3 -m unittest smoke -v --failfast"
    context.run(command, echo=True)