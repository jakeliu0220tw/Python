from typing import List
from pydantic import BaseModel, ValidationError, validator
import json

class Employee(BaseModel):
    name: str
    username: str
    salary: int
    habits: List[str]

if __name__ == '__main__':
    e1 = Employee(name='jake', username='jake', salary=10000, habits=['reading', 'tennis'])
    e2 = Employee(name='jake2', username='jake2', salary='10000', habits=[])
    # convert pydantic obj to dict
    print(type(e1.dict()))
    print(f"e1.dict() = {e1.dict()}")

    # covnert pydantic obj to json string
    print(type(e2.json()))
    print(f"e2.json() = {e2.json()}")

    # convert json string to pydantic obj
    json_string = '{"name":"jake3", "username":"jake3", "salary":10000, "habits":[]}'
    json_dict = json.loads(json_string)
    print(type(json_dict))
    e3 = Employee(**json_dict)
    print(f"e3.dict() = {e3.dict()}")