<<<<<<< HEAD
**AirBnB clone - The console**
=======
**AirBnB clone - The console**
>>>>>>>

### Introduction

This repository contains the codebase for an AirBnB clone, including a command-line interface (CLI) for managing AirBnB objects. The project is structured around a parent class called `BaseModel` responsible for initialization, serialization, and deserialization of instances, as well as a file storage engine for persisting data.

### Features

- **BaseModel Class**: A parent class for all AirBnB objects, handling common functionality such as initialization, serialization, and deserialization.
- **Serialization and Deserialization**: Objects can be serialized to and deserialized from dictionaries, JSON strings, and files.
- **File Storage Engine**: An abstracted storage engine allows for saving objects to and loading objects from JSON files.
- **Subclasses for AirBnB Objects**: Various subclasses such as `User`, `State`, `City`, `Place`, etc., inherit from the `BaseModel` class, providing specific functionality for each type of object.

### How to Use

1. **Installation**: Clone this repository to your local machine.

   ```bash
   git clone https://github.com/Gloriaisuwa/AirBnB_clone.git
   ```

2. **Setup**: Ensure you have Python installed on your machine. Install any necessary dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. **Usage**: Run the command-line interface to interact with AirBnB objects.

   ```bash
   python console.py
   ```

4. **Commands**: Use the following commands in the CLI to manage AirBnB objects:
   - `create`: Create a new object.
   - `show`: Show details of a specific object.
   - `destroy`: Delete an object.
   - `all`: Show all objects of a certain type or all objects.
   - `update`: Update an object's attributes.

### File Structure

- **models/**: Contains all model classes for AirBnB objects.
- **engine/**: Contains the file storage engine implementation.
- **tests/**: Contains unit tests for validating classes and storage engine functionality.
- **console.py**: The main command-line interface for interacting with AirBnB objects.
- **README.md**: Documentation and instructions for the repository.

### Testing

Unit tests are provided in the `tests/` directory to ensure the correctness of all classes and the file storage engine. To run the tests, execute the following command:

```bash
pytest
```

### Contributors

- Loveday Nnabuife (@SageLovedayy)
- Gloria Isuwa (@Gloriaisuwa)

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgement\

Special thanks to the AirBnB team for inspiring this project and special thanks to ALX for providing guidance on the project structure and requirements.
