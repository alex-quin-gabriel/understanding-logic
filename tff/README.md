# Typed First-Order Form coding

## Creating test

You can generate test scenarios for the conjectures in the `tests` folder by
editing `tests/create-test.py` to adjust the number of instances to create, and
then running `python create-test.py > test-scenario.tff` in the `tests`
directory.

To modify the tests to use the ROS 2 formalism, set `USE_ROS_FORMALISMS = True`
in `tests/create-test.py`. For an example of output see
`tests/test-scenario-ros.tff` and `tests/conj-exertable-ros.tff`.
