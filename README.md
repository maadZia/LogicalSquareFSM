# Logical Square FSM Generator

## :pushpin: Project Description
LogicalSquare IDE is an integrated development environment that enables intuitive design and implementation of state machines based on the concept of a logical square of opposition. The application allows for defining states, transitions between them, and automatically generating code in multiple formats.

## :rocket: Features
- Creating and managing logical squares
- Generating hierarchical state trees
- Assigning unique names to states
- Defining transitions between states
- Automatic code generation based on:
  - State Pattern design
  - PyQt5 framework
  - Transitions library
  - State Machine Compiler (SMC)
- Checking state disjointness using the Z3 solver
- AI-assisted generation of logical squares

---

## :heavy_check_mark: System Requirements 
- Python 3.8+
- Operating system: Windows/Linux/macOS

## :one: Installation

### 1. Clone the repository
```bash
git clone https://github.com/maadZia/LogicalSquareFSM.git
cd LogicalSquareFSM
```

### 2. Install required libraries
```bash
pip install -r requirements.txt
```
### 3. Using LLM Chat (optional)

To use the LLM Chat feature, you need to log in to [ Google AI Studio](https://aistudio.google.com), generate an API key, and insert it into components/ai_module.py:

```python
apiKey = 'PUT_YOUR_API_KEY_HERE'
```

## :two: Running the Application

After a successful installation, you can start the application with:
```bash
python main.py
```
---

## :open_file_folder: Technologies and Libraries Used 
- **PyQt5** – GUI development
- **PyQtGraph** – Data visualization
- **NetworkX** – Graph structure modeling
- **Solver Z3** – Logical state analysis
- **Google Generative AI** – AI support
- **State Machine Compiler (SMC)** – State machine code generation

## :books: Interface Structure
1. **Defining Logical Square** – The first step in modeling the state machine
2. **State Tree** – Hierarchical state tree
3. **State Machine** – Visualization of the state machine with transition definitions
4. **Assertions** – State structure analysis
5. **Expand State** – Expanding states
6. **LLM Chat** – AI-assisted logical square definition
7. **Solver** – State disjointness analysis tool
8. **Generate Code** – Automatic code generation in various formats
9. **Reset** – Restarting the project

## :arrow_forward: Example Usage
To create a state machine, the user:
1. Defines a logical square
2. Checks state disjointness
3. Creates transitions between states
4. Generates source code

## :sparkles: Planned Future Enhancements
- Expanding support for different programming languages in generated code
- Optimizing the user interface
- Enhancing AI capabilities for state analysis


