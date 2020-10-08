# Test Automation Project

Python
Pytest
Selenium

```
Scenario: Basic DuckDuckGo Search
    Given the DuckDuckGo home page is displayed
    When the user searches for "panda"
    Then the search results title contains "panda"
    And the search result query is "panda"
    And the search result links pertain "panda"
```

# Running tests

```
$ pytest -v
============================================================== test session starts ===============================================================
platform linux -- Python 3.6.8, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /home/cesar-rayo/.virtualenvs/python3_6/bin/python3
cachedir: .pytest_cache
rootdir: /home/cesar-rayo/Documents/projects/python_selenium
collected 4 items                                                                                                                                

tests/test_fw.py::test_dummy PASSED                                                                                                        [ 25%]
tests/test_search.py::test_basic_duckduckgo_search[panda] PASSED                                                                           [ 50%]
tests/test_search.py::test_basic_duckduckgo_search[python] PASSED                                                                          [ 75%]
tests/test_search.py::test_basic_duckduckgo_search[polar bear] PASSED                                                                      [100%]

=============================================================== 4 passed in 17.87s ===============================================================
```

After installing pytest-xdist you could run in tests parallel

```
$ pytest -n 3 -v
============================================================== test session starts ===============================================================
platform linux -- Python 3.6.8, pytest-6.1.1, py-1.9.0, pluggy-0.13.1 -- /home/cesar-rayo/.virtualenvs/python3_6/bin/python3
cachedir: .pytest_cache
rootdir: /home/cesar-rayo/Documents/projects/python_selenium
plugins: forked-1.3.0, xdist-2.1.0
[gw0] linux Python 3.6.8 cwd: /home/cesar-rayo/Documents/projects/python_selenium
[gw1] linux Python 3.6.8 cwd: /home/cesar-rayo/Documents/projects/python_selenium
[gw2] linux Python 3.6.8 cwd: /home/cesar-rayo/Documents/projects/python_selenium
[gw0] Python 3.6.8 (default, Oct  7 2019, 12:59:55)  -- [GCC 8.3.0]
[gw2] Python 3.6.8 (default, Oct  7 2019, 12:59:55)  -- [GCC 8.3.0]
[gw1] Python 3.6.8 (default, Oct  7 2019, 12:59:55)  -- [GCC 8.3.0]
gw0 [4] / gw1 [4] / gw2 [4]
scheduling tests via LoadScheduling

tests/test_search.py::test_basic_duckduckgo_search[python] 
tests/test_search.py::test_basic_duckduckgo_search[panda] 
tests/test_fw.py::test_dummy 
[gw0] [ 25%] PASSED tests/test_fw.py::test_dummy 
tests/test_search.py::test_basic_duckduckgo_search[polar bear] 
[gw1] [ 50%] PASSED tests/test_search.py::test_basic_duckduckgo_search[python] 
[gw0] [ 75%] PASSED tests/test_search.py::test_basic_duckduckgo_search[polar bear] 
[gw2] [100%] PASSED tests/test_search.py::test_basic_duckduckgo_search[panda] 

=============================================================== 4 passed in 7.53s ================================================================
```
