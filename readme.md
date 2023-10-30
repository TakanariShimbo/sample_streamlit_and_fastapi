# Install libs

```
pip install streamlit
pip install extra_streamlit_components
pip install plotly
pip install scipy
# numpy, pandas are installed automaticaly!

pip install fastapi
pip install uvicorn
pip install python-jose[cryptography]
pip install passlib[bcrypt]
pip install python-multipart
# pip install sqlalchemy

pip install openai
```

# Build Server

```
cd work_fastapi
uvicorn main:app --reload
```

```
cd work_streamlit
streamlit run .\1_🏠_Home.py
```

# Streamlit

- handlers  
   controllers
  helpers
- components  
   views

- pages
  routes

- schemes

- login.py
  main

# FastAPI

- handlers
  controllers
  helpers

- schemes

- main.py
  main
