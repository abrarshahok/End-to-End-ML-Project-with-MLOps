import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "mlProject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "./params.yaml",
    "./schema.yaml",
    "./main.py",
    "./app.py",
    "./Dockerfile",
    "./requirements.txt",
    "./setup.py",
    "./research/trials.ipynb",
    "./templates/index.html",
    "./test.py",
    "./.gitignore",
    "./LICENSE",
    "./README.md"
]

if __name__ == "__main__":
    for filepath in list_of_files:
        # Create the directory path if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        logging.info(f"Directory created for: {os.path.dirname(filepath)}")

        # Check if the file exists
        if os.path.exists(filepath):
            # Check if the file has content
            if os.path.getsize(filepath) > 0:
                logging.warning(f"File exists and has content, skipping creation: {filepath}")
                continue
            else:
                logging.info(f"File exists but is empty: {filepath}")
        else:
            # Create an empty file if it doesn't already exist
            with open(filepath, "w") as f:
                logging.info(f"File created: {filepath}")

    logging.info("Project structure created successfully!")