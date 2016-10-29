# tdd_setup_python


## Requirements

You need python and a python test runner, for example [pytest](http://doc.pytest.org/en/latest/). An easy way to setup an isolated environment for your TDD project is to use the [conda](http://conda.pydata.org/docs/intro.html) package manager.

### Installation with the conda package manager
```
conda create -n tddpy pytest
```

This creates a environment with the name tddpy ready-made with python, pytest and other modules that pytest depends on. You change to this environment via

```
source activate tddpy
```

and leave it via
```
source deactivate
```

## Run tests

```
cd tdd_setup_python
pytest
```

This will run all the assertions in the functions with name pattern "test\_\*" in the files matching "test\_\*.py". You will see one failing test that you can sure fix easily by modifying [test_role_model.py](test_role_model.py) :)

## Start the TDD cycle and write awesome code
