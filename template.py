import os
from pathlib import Path

PROJECT_NAME = "US_VISA"
LIST_OF_FILES = [
    f"{PROJECT_NAME}/__init__.py",
    f"{PROJECT_NAME}/component/__init__.py",
    f"{PROJECT_NAME}/component/data_ingestion.py",
    f"{PROJECT_NAME}/component/data_validation.py",
    f"{PROJECT_NAME}/component/data_transformation.py",
    f"{PROJECT_NAME}/component/model_trainer.py",
    f"{PROJECT_NAME}/component/model_evaluation.py",
     f"{PROJECT_NAME}/component/model_pusher.py",
     f"{PROJECT_NAME}/configuration/__init__.py",
     f"{PROJECT_NAME}/constants/__init__.py",
      f"{PROJECT_NAME}/entity/__init__.py",
      f"{PROJECT_NAME}/entity/config_entity.py",
      f"{PROJECT_NAME}/entity/artifact_entity.py",
      f"{PROJECT_NAME}/exception/__init__.py",
      f"{PROJECT_NAME}/logger/__init__.py",
      f"{PROJECT_NAME}/pipeline/__init__.py",
      f"{PROJECT_NAME}/pipeline/training_pipeline.py",
      f"{PROJECT_NAME}/pipeline/prediction_pipeline.py",
      f"{PROJECT_NAME}/utils/__init__.py",
      f"{PROJECT_NAME}/utils/main_utils.py",
      "app.py",
      "requirements.txt",
      "Dockerfile",
      ".dockerignore",
      "demo.py",
      "setup.py",
      "config/model.yaml",
      "config/schema.yaml"
]

for files in LIST_OF_FILES:
    filePath = Path(files)
    fileDir,filename = os.path.split(files)
    if fileDir!="":
        os.makedirs(fileDir,exist_ok=True)
    
    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)):
        with open(files,'w') as f:
            pass
    
    else:
        print(f"{filePath} already exists!")