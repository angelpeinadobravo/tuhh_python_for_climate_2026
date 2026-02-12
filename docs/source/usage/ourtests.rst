.. _ourtests:

Our Tests
=========

This project uses pytest for executing the Python tests in the ``tests/`` directory. All the tests in this directory are also run by the ``.gitlab-ci.yml``.

Testing Python Code
###################

Simply import the code you want to test (e.g. module, function, class etc.) in a script in the ``tests/`` directory called ``test_[name].py`` with a "name" of your choosing. Then write functions to test the imported code...

Once you've done that you can then run pytest on the entire tests directory or on just your tests. For example, ``pytest ./tests`` would test every test in the ``tests/`` directory, whereas ``pytest test_[name].py`` runs just the tests in ``test_[name].py``.
