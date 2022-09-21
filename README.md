# fastapi-ecommerce

## live demo:
[https://sunpochin.lol/docs](https://sunpochin.lol/docs)
or
[https://fastapi-pac.onrender.com/docs](https://fastapi-pac.onrender.com/docs)



## notes on aws ecs CD
https://reactdotjs.hashnode.dev/github-action-cd-to-aws-ecs-ecr-part-1
The codes are in this branch: https://github.com/sunpochin/fastapi-ecommerce/tree/ecs_fastapi

## intro
Using [FastAPI](https://fastapi.tiangolo.com/). 
The application serve as backend of my frontend project.

## Use this project locally

1.  ```sh
    git clone git@github.com:sunpochin/fastapi-ecommerce.git
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv venv && source venv/bin/activate
    ```

3. Install the requirements:

    ```sh
    (venv)$ pip3 install -r requirements.txt
    ```

4. Initialize the database:

    ```sh
    (venv)$ python3 init_db.py
    ```

5. Run the server:

    ```sh
    (venv)$ uvicorn sql_app.main:app --reload --host 0.0.0.0 --port 8000
    ```
    
 6. Navigate to [http://localhost:8000/](http://localhost:8000/) in your favorite web browser.
