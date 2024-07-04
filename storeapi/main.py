from fastapi import FastAPI
import uvicorn
from routers.post import router as post_router

app = FastAPI()


app.include_router(post_router)



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)