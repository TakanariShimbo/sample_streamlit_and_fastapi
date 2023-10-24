import streamlit as st

from handlers.title_handler import TitleHandler
from handlers.login_handler import LoginCheckHandler


# Set Titles
TitleHandler.set_title(icon="📄", title="Markdown")


# check login
LoginCheckHandler.early_return_if_not_logined()


# Contents
markdown_contents = """
### List
- content1
- content2
- content3

### Code
- python
```python
print("hello world")
```

- html
```html
<h1>Title</h1>
<p>this is sample.</p>
```

### LaTex
The below equation represents the motion equation.

$$
F = ma
$$

here, $F$ is force, $m$ is mass, $a$ is accelaration.
"""
st.markdown(markdown_contents)
