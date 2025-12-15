# MLOps Git Exercise

A Python project for learning and practicing MLOps workflows with Git.

## Project Overview

This project demonstrates best practices for:
- Project structure and organization
- Python packaging and distribution
- Testing and code quality
- Documentation
- CI/CD workflows
- Git workflow management

## Installation

### Prerequisites
- Python 3.8 or higher
- pip or conda

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mlops-git-exercise.git
cd mlops-git-exercise
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install development dependencies (optional):
```bash
pip install -r requirements-dev.txt
```

## Project Structure

```
mlops-git-exercise/
├── src/                    # Main source code
├── tests/                  # Test files
├── docs/                   # Documentation
├── .github/workflows/      # GitHub Actions workflows
├── pyproject.toml          # Project configuration
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
├── README.md               # This file
└── .gitignore             # Git ignore rules
```

## Usage

```python
from src.main import main

result = main()
print(result)
```

## Testing

Run tests with pytest:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=src
```

## Code Quality

Format code with black:
```bash
black .
```

Check code style with flake8:
```bash
flake8 src/ tests/
```

Sort imports with isort:
```bash
isort .
```

Run type checking with mypy:
```bash
mypy src/
```

## Documentation

Generate Sphinx documentation:
```bash
cd docs
make html
```

## Contributing

Contributions are welcome! Please follow these guidelines:
1. Create a feature branch
2. Make your changes
3. Write tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or feedback, please open an issue on GitHub.
