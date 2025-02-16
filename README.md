# Software Engineering for Data Scientists

This repository demonstrates how to approach data science computations with a software engineering mindset. It covers essential software engineering principles applied to data science tasks, including code formatting, object-oriented and functional programming paradigms, error handling, logging, debugging, and testing. The project uses UV for dependency management and getting started quickly.

## Key Concepts Covered

This project illustrates the following software engineering principles in the context of data science:

- **Code Formatting & Linting:** Consistent code formatting and linting are crucial for readability and maintainability. This project demonstrates best practices for code style.
- **Object-Oriented Programming (OOP):** OOP principles are applied to structure data science code, promoting modularity, reusability, and maintainability.
- **Functional Programming (FP):** FP paradigms are used to write concise, predictable, and testable data science functions.
- **Error Handling:** Robust error handling techniques are implemented to gracefully manage potential issues during data processing and model training.
- **Logging:** Logging practices are shown to effectively track the progress of data science workflows, debug issues, and monitor performance.
- **Debugging:** Strategies for debugging data science code are demonstrated, enabling efficient identification and resolution of errors.
- **Testing:** Unit tests are implemented to ensure the correctness and reliability of data science code components.

## Getting Started

### Prerequisites

- Python 3.7+ (or specify the exact version in `.python-version`)
- UV (for dependency management - installation instructions below)

### Installation

1.  **Install UV:** UV is used for managing project dependencies. Follow the instructions for your platform from the [UV](https://docs.astral.sh/uv/getting-started/installation/).

2.  **Clone the repository:**

    ```bash
    git clone git@github.com:rubiagatra/swe-for-ds.git
    ```

3.  **Navigate to the project directory:**

    ```bash
    cd swe-for-ds
    ```

4.  **Install project dependencies using UV:**

    ```bash
    uv sync
    ```

## Usage

### Running the code

Explain how to run the different parts of the project. Provide specific commands and example usage for each module or script. For example:

```bash
uv run python [module4].py  # Run module 4
uv run pytest [module4]_test.py -v # Run unit tests for module 4 with verbose output
```
