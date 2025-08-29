from fastapi import FastAPI, Request
from pydantic import BaseModel
import re

app = FastAPI()

# Replace with your details
FULL_NAME = "john_doe"
DOB = "17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

class DataModel(BaseModel):
    data: list

def alternating_caps(s):
    result = []
    toggle = True
    for ch in s:
        if ch.isalpha():
            result.append(ch.upper() if toggle else ch.lower())
            toggle = not toggle
        else:
            result.append(ch)
    return "".join(result)

@app.post("/bfhl")
async def bfhl_endpoint(payload: DataModel):
    try:
        data = payload.data
        odd_numbers, even_numbers, alphabets, special_chars = [], [], [], []
        num_sum = 0

        for item in data:
            if item.isdigit():
                num = int(item)
                num_sum += num
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif item.isalpha():
                alphabets.append(item.upper())
            else:
                special_chars.append(item)

        # Concatenate alphabets reversed with alternating caps
        concat_string = alternating_caps("".join(alphabets)[::-1])

        return {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum": str(num_sum),
            "concat_string": concat_string
        }

    except Exception as e:
        return {
            "is_success": False,
            "error": str(e)
        }
