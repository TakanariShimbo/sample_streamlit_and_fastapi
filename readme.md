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

# Set Params

## Create RS256 Keys
* private
```
openssl genpkey -algorithm RSA -out private_key.pem
```
* public
```
openssl rsa -pubout -in private_key.pem -out public_key.pem
```

# Build Server

## Streamlit

```
cd work_fastapi
uvicorn main:app --reload
```

## FastAIP

```
cd work_streamlit
streamlit run .\1_🏠_Home.py
```

# Directorys

## Streamlit

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

## FastAPI

- handlers
  controllers
  helpers

- schemes

- main.py
  main
