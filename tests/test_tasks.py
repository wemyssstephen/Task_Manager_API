def test_create_task(client):
    # Define test task data
    task_data = {
        "title": "Test Task",
        "description": "Test Task Description",
        "is_completed": False,
    }

    # POST request
    response = client.post("/tasks/", json=task_data)

    # Assert it is correct
    assert response.status_code == 201

    # Get the created task
    created_task = response.json()

    # Verify the data
    assert created_task["title"] == task_data["title"]
    assert created_task["description"] == task_data["description"]
    assert created_task["is_completed"] == task_data["is_completed"]
    assert "id" in created_task
    assert "created_at" in created_task


def test_get_all_tasks(client):
    task1 = {
        "title": "Test Task",
        "description": "Test Task Description",
        "is_completed": False,
    }
    task2 = {
        "title": "Test Task Two",
        "description": "Test Task Two Description",
        "is_completed": False,
    }

    client.post("/tasks/", json=task1)
    client.post("/tasks/", json=task2)

    # Verify response is received correctly
    response = client.get("/tasks/")
    assert response.status_code == 200

    # Verify contents
    tasks = response.json()
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Test Task"
    assert tasks[1]["title"] == "Test Task Two"

def test_get_uncompleted_tasks(client):
    task1 = {
        "title": "Uncompleted Test Task",
        "description": "Test Task Description",
        "is_completed": False,
    }
    task2 = {
        "title": "Completed Test Task",
        "description": "Test Task Description",
        "is_completed": True,
    }

    client.post("/tasks/", json=task1)
    client.post("/tasks/", json=task2)

    response = client.get("/tasks/uncompleted/")
    assert response.status_code == 200

    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Uncompleted Test Task"

def test_get_completed_tasks(client):
    task1 = {
        "title": "Completed Test Task",
        "description": "Test Task Description",
        "is_completed": True,
    }
    task2 = {
        "title": "Uncompleted Test Task",
        "description": "Test Task Description",
        "is_completed": False,
    }

    client.post("/tasks/", json=task1)
    client.post("/tasks/", json=task2)

    response = client.get("/tasks/completed/")
    assert response.status_code == 200

    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Completed Test Task"


def test_update_task(client):
    task = {
        "title": "Test Task",
        "description": "OLD Description",
        "is_completed": False,
    }

    updated_task = {
        "title": "Updated Test Task",
        "description": "NEW Task Description",
        "is_completed": True,
    }

    response = client.post("/tasks/", json=task)
    created_task = response.json()
    task_id = created_task["id"]

    response = client.patch(f"/tasks/?task_id={task_id}", json=updated_task)
    assert response.status_code == 200

    # Verify update was successful
    response = client.get(f"/tasks/")
    tasks = response.json()
    updated_task = tasks[0]

    assert updated_task["title"] == "Updated Test Task"
    assert updated_task["description"] == "NEW Task Description"
    assert updated_task["is_completed"] == True

def test_delete_task(client):
    # TODO: should really add a 2nd task in here to verify that one is deleted.
    task = {
        "title": "Test Task",
        "description": "Test Task Description",
        "is_completed": False,
    }

    response = client.post("/tasks/", json=task)
    created_task = response.json()
    task_id = created_task["id"]
    assert response.status_code == 201

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204

