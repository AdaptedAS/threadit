### Python Threadit
###### Running functions in threads with no effort

![PyPI - Format](https://img.shields.io/pypi/format/threadit)
![PyPI - Status](https://img.shields.io/pypi/status/threadit)
![Downloads](https://pepy.tech/badge/threadit)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/threadit)

A nice package to help you run functions in threads and get their result.<br />
This is under development! So please check for changes before updating
### Installation
```
pip install threadit
```

### Usage

```python
import time
from threadit import ThreadIT


def get_company_name():
    # Do work in thread
    time.sleep(5)
    return 'Adapted'


def do_some_work():
    get_name = ThreadIT(get_company_name)

    # do stuff or run a while loop to wait for result
    
    more_thread = ThreadIT(get_company_name)

    while get_name.doing_work():
        print('Waiting for thread to finnish')

    # You can also call .result() and the main thread will wait 
    # for the thread to return your result.
    company_name = get_name.result()

    # this will timeout the thread in 1 second if its not finished
    company_name2 = more_thread.result(timeout=1)

    print(company_name) # Outputs -> Adapted
    print(company_name2) # Outputs -> None
    
```

### Main commands

```python
# Import the module
from threadit import ThreadIT

# Start your function with or without arguments
var = ThreadIT(function, args, kwargs)

# Wait for the function to finnish or get the result if its finished
var.result()
```

## Optional commands
```python
# Check if your thread is still working on the function.
# This will return True if the function is not completed.

var.doing_work()

# Terminate the thread. This will noe wait for the function to 
# finnish and will return None as result if the function is not
# done within the timelimit set

var.result(timeout=10)

```

### Testing

Use the following command to run tests.

```bash
python -m unittest threadit.tests.test_threadit
```

### Changelog:

See CHANGELOG.md
