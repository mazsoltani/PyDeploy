# FastAPI Project 

This FastAPI project demonstrates a simple API for managing items. It allows you to create, read, update, and delete items.

## Routes

### Root Endpoint

- **GET /:**
    - Description: Returns a greeting message.
    - Response:
      ```
      {"Hello": "World"}
      ```

### Get Item Endpoint

- **GET /items/{item_id}:**
    - Description: Retrieve details of a specific item by its ID.
    - Parameters:
        - `item_id` (int): ID of the item to retrieve.
        - `q` (str, optional): Additional query parameter.
    - Response:
      ```
      {"item_id": item_id, "q": q}
      ```

### Update Item Endpoint

- **PUT /items/{item_id}:**
    - Description: Update details of a specific item by its ID.
    - Parameters:
        - `item_id` (int): ID of the item to update.
        - Request Body:
            - `name` (str): Name of the item.
            - `price` (float): Price of the item.
            - `is_offer` (bool, optional): Offer status of the item.
    - Response:
      ```
      {"item_name": item.name, "item_id": item_id}
      ```

## How to Start the Server

```
uvicorn main:app --reload
```

Access the API at `http://127.0.0.1:8000` in your web browser or API client.
