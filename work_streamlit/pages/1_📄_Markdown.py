import streamlit as st

from handlers.title_handler import TitleHandler
from handlers.login_handler import LoginHandler


# Set Titles
TitleHandler.set_title(icon="📄", title="Markdown")


# check login
login_handler = LoginHandler()
if not login_handler.check_is_loggedin():
    st.error("Please login at 🏠 Home")
    st.stop()



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
