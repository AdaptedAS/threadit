### Python Threadit
###### Running functions in threads with no effort

![PyPI - Format](https://img.shields.io/pypi/format/threadit)
![PyPI - Status](https://img.shields.io/pypi/status/threadit)
![Downloads](https://pepy.tech/badge/threadit)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/threadit)

A nice package to help you run functions in threads and get their result.<br />

### Installation
```
pip install threadit
```

### Usage

```python
from threadit import Threadit


def get_company_name():
    # Do work in thread
    return 'Adapted'


def do_some_work():
    get_name = Threadit(get_company_name)

    # do stuff or run a while loop to wait for result
    
    more_thread = Threadit(get_company_name)

    while get_name.doing_working():
        print('Waiting for thread to finnish')

    # You can also call .result() and the main thread will wait for the thread to return your result.

    company_name = get_name.result()
    company_name2 = more_thread.result()

    print(company_name) # Outputs -> Adapted
    print(company_name2) # Outputs -> Adapted
    
```


### Testing

Use the following command to run tests.

```bash
python -m unittest threadit.tests.test_threadit
```

### Changelog:

See CHANGELOG.md
