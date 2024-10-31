from fastapi import FastAPI

app = FastAPI();

@app.api_route('/user')
def index():
    return { "data": {"Name": "Takondwa Kapyola","Age" : 23}};

@app.post('/user')
async def create_user(data):
    return {data};