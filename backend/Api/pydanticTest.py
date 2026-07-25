from datetime import datetime
from pydantic import BaseModel

# 1. Define a Data Model
# By inheriting from BaseModel, you tell Pydantic that 'User' is a schema.
# It defines exactly what a "User" should look like in your application.
class User(BaseModel):
    id: int                          # Required: Must be an integer
    name: str = "John Doe"           # Optional: Defaults to "John Doe" if not provided
    signup_ts: datetime | None = None # Optional: Can be a datetime object or None
    friends: list[int] = []          # Optional: A list that must contain integers

# 2. Raw External Data
# Notice that this data is "messy":
# - 'id' is a string "123" instead of an int 123
# - 'signup_ts' is a string instead of a datetime object
# - 'friends' contains a string "2" and bytes b"3"
external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

# 3. Data Parsing and Validation
# This is where the magic happens. When you pass the dictionary to User(...), 
# Pydantic performs "Type Coercion" (converting types to match the model).
user = User(**external_data)

# 4. Accessing Data
# After validation, 'user' is a real Python object. 
# You get autocompletion in your editor for all the fields.
print(user)
# Output shows everything was converted correctly:
# User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]

print(user.id)
# Returns the integer 123, not the string "123".