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
pip install opencv-python
```

# Set Params
create params.py refering params_sample.py

## HS256 Key
```
openssl rand -hex 32
```

## RS256 Keys
* create private key
```
openssl genpkey -algorithm RSA -out private_key.pem
```
* create public key
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

# Dirs

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
