# PyHTML - v1.0.0

**PyHTML** is a Python package designed to simplify the process of writing HTML code using Python. With **PyHTML**, you can programmatically create and manipulate HTML elements, making it ideal for developers who need to generate dynamic HTML content.

## Features

- **Programmatic HTML Generation:** Create HTML elements and nest them easily.
- **Readable Syntax:** Write HTML in a way that feels natural in Python.
- **Styling:** [TailWindCSS](https://tailwindcss.com/) supported
- **Lightweight:** Minimal dependencies for a straightforward HTML generation tool.

## Installation

You can install **PyHTML** using these 2 methods:

- Git clone the repository and install locally

```bash
pip install -e .
```

Or install directly from the GitHub repository:

```bash
pip install git+https://github.com/locphan201/pyhtml.git
```

## Usage

Below is an example that demonstrates how to use **PyHTML** to create a simple HTML page. Each section of the code is commented to explain its purpose.

```python
from pyhtml import *

html = HTML(
    children=[
        Text('Welcome to PyHTML'),
        Column(
            children=Text('Hello World!')
        )
    ]
)
html_code = html.render()
print(html_code)
```

### Detailed Code Explanation

- **Imports:** The script starts by importing the element classes needed to build the page.
- **Element Creation:** 
  - `HTML` is used as the root container and already setup with head and body tags.
  - `Text` is used to create a header and paragraph respectively.
  - `Column` is used to align items within the class vertically.
- **Rendering:** The `render()` method converts the Python objects into valid HTML markup.
- **Output:** Finally, the generated HTML is printed, which you can then use or embed in your web application.

## Contributing

Contributions are welcome! If you have ideas, improvements, or bug fixes, please open an issue or submit a pull request on our [GitHub repository](https://github.com/locphan201/pyhtml.git).