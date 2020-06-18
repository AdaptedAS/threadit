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
from threadit import Threadit, thredit_result


@thredit_result
def get_company_name():
    # Do work in thread
    return 'Adapted'


def do_some_work():
    get_name = Threadit(get_company_name)
    # do stuff or run a while loop to wait for result
    while get_name.doing_working():
        print('Waiting for thread to finnish')
    
    # You can also call .get() and the system will wait for the thread to return your result.

    company_name = get_name.get()
    print(company_name) # Outputs -> Adapted
    
```

Remember to add the @thredit_result decorator to the function you want to run in a thread, else you get back a SyntaxWarning.

### Testing

Use the following command to run tests.

```bash
python -m unittest threadit.tests.test_threadit
```

### Changelog:

See CHANGELOG.md
