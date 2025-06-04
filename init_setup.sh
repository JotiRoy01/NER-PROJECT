# echo [$(date)]: "START"
# export _VERSION_ = 3.10
# echo [$(date)]: "Creating Environment with Python $(_VERSION_)"
# conda create --prefix ./env_NER=$(_VERSION_) -y
# echo [$(date)]: "Activate Virtual Environment"
# source activate ./env_NER

# echo [$(date)]: Install All Requiremets
# pip install requirements

# Bash shell script to create the directory structure and __init__.py files

# Define the Base Directory
BASE_DIR="src/NER"
#List of Subdirectory to create
DIRECTORY=(
    "components"
    "config"
    "constants"
    "entity"
    "exception"
    "logger"
    "pipeline"
    "utils"
)

# Loop through the directory and create it along with __init__.py

for DIR in "${DIRECTORY[@]}"
    do 
        FULL_PATH="$BASE_DIR/$DIR"
        echo ["$(date)"]: Creating $FULL_PATH
        # create the directory (including parents if necessary)
        mkdir -p "$FULL_PATH"
        # create the __init__.py file
        INIT_FILE="$FULL_PATH/__init__.py"
        echo "[$(date)]: Creating __init__.py inside $FULL_PATH"

        # Add a placeholder comment to the __init__.py file
        echo "# __init__.py for $DIR" > "$INIT_FILE"

    done

