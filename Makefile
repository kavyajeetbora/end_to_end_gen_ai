## Name of the virtual environment
VENV = venv
PYTHON = python
LOGS_DIR = logs
ARTIFACTS_DIR = artifacts

## Activate the virtual environment
ACTIVATE = . $(VENV)/bin/activate

## Locate the requirements
REQUIREMENTS = requirements.txt

setup:
	# Create the virtual environment
	$(PYTHON) -m venv $(VENV)
	@echo "Activating virtual environment..."
	@$(ACTIVATE) && pip install --upgrade pip
	@$(ACTIVATE) && pip install -r requirements.txt
	@echo "Setup complete."

	@echo "Setting up logs folder"
	@mkdir -p $(LOGS_DIR)
	
	@mkdir -p $(ARTIFACTS_DIR)
	@echo "Created Artifacts folder"

clean:
	# Remove the virtual environment and any nltk data
	rm -rf $(VENV) $(NLTK_DATA_DIR) $(ARTIFACTS_DIR) $(LOGS_DIR)
	@echo "Cleaned up the environment and nltk data."

