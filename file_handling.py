
# 📝 Python File Handling Cheat Sheet (with JSON)


## 1. **What is File Handling?**

* File handling means working with **files stored on disk**.
* In Python, we use the built-in **`open()` function** to read/write files.
* After work is done, we **close** the file to free memory.
* Best way = use **`with`** (auto closes file).

---

## 2. **File Modes**

| Mode   | Meaning                                  | Example                   |
| ------ | ---------------------------------------- | ------------------------- |
| `"r"`  | Read (default) → error if file not found | `open("file.txt", "r")`   |
| `"w"`  | Write → creates new file / overwrites    | `open("file.txt", "w")`   |
| `"a"`  | Append → adds content at end             | `open("file.txt", "a")`   |
| `"x"`  | Create new → error if file exists        | `open("file.txt", "x")`   |
| `"t"`  | Text mode (default)                      | `open("file.txt", "rt")`  |
| `"b"`  | Binary mode                              | `open("image.png", "rb")` |
| `"r+"` | Read + Write                             | `open("file.txt", "r+")`  |

---

## 3. **Basic Operations**

### (a) Open a File

```python
f = open("myfile.txt", "r")  # open in read mode
```

### (b) Read a File

```python
f = open("myfile.txt", "r")
print(f.read())        # Entire file
print(f.readline())    # One line
print(f.readlines())   # List of all lines
f.close()
```

### (c) Write to File

```python
f = open("myfile.txt", "w")   # Overwrites file
f.write("Hello Python!\n")
f.write("File handling is easy")
f.close()
```

### (d) Append to File

```python
f = open("myfile.txt", "a")
f.write("\nThis line is appended.")
f.close()
```

---

## 4. **Using `with` (Best Practice)**

* No need `f.close()`.
* File closes automatically.

```python
with open("myfile.txt", "r") as f:
    data = f.read()
    print(data)
```

---

## 5. **Check & Delete File**

```python
import os

if os.path.exists("myfile.txt"):
    print("File exists ✅")
    os.remove("myfile.txt")  # Delete
else:
    print("File does not exist ❌")
```

---

## 6. **File Pointer**

* `f.tell()` → get current position
* `f.seek(n)` → move pointer

```python
f = open("myfile.txt", "r")
print(f.read(5))   # Read first 5 chars
print(f.tell())    # Current position
f.seek(0)          # Move back to start
print(f.read())    # Read again
f.close()
```

---

## 7. **Binary Files**

Used for **images, audio, video**.

```python
# Copy image
with open("pic.jpg", "rb") as f1:
    with open("copy.jpg", "wb") as f2:
        f2.write(f1.read())
```

---

## 8. **JSON File Handling**

* JSON = **JavaScript Object Notation**.
* Used to store data in **key-value pairs**.
* Python has **`json` module**.

### (a) Import JSON

```python
import json
```

### (b) Convert Python → JSON (`dump`, `dumps`)

```python
import json

data = {"name": "Alice", "age": 25, "city": "Delhi"}

# Convert to JSON string
json_string = json.dumps(data)
print(json_string)

# Write JSON to file
with open("data.json", "w") as f:
    json.dump(data, f)
```

### (c) Convert JSON → Python (`load`, `loads`)

```python
# Read JSON string
json_string = '{"name": "Bob", "age": 30}'
py_data = json.loads(json_string)
print(py_data["name"])  # Bob

# Read JSON file
with open("data.json", "r") as f:
    data = json.load(f)
    print(data["city"])
```

---

## ✅ Summary (Easy Points)

* Always open file with `open(filename, mode)`.
* Modes → `"r"` read, `"w"` write, `"a"` append, `"x"` create.
* Use **with open(...)** (auto close).
* Functions → `read()`, `readline()`, `readlines()`, `write()`.
* File pointer → `tell()`, `seek()`.
* Use `os` module for checking & deleting files.
* For JSON → use `json.dump()`, `json.load()` to work with files.


