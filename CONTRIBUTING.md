# Contributing to University Management System

First off, thank you for considering contributing to the University Management System! It's people like you that make this project better for everyone.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (code snippets, screenshots, etc.)
- **Describe the behavior you observed** and what you expected
- **Include your environment details** (OS, Python version, Flask version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **List any alternatives you've considered**

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the code style guidelines
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Write clear commit messages**
6. **Submit a pull request**

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/University-Management-System.git
   cd University-Management-System
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Code Style Guidelines

- Follow **PEP 8** style guide for Python code
- Use **meaningful variable and function names**
- Add **comments** for complex logic
- Keep functions **small and focused**
- Write **docstrings** for classes and functions

## Commit Message Guidelines

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests when relevant

Examples:
```
Add student email validation
Fix transport queue processing bug
Update README with installation instructions
```

## Project Structure

- `app.py` - Flask application and routes
- `student.py` - Student management (Linked List implementation)
- `exam.py` - Exam management (Dynamic Array implementation)
- `fee.py` - Fee management
- `transport.py` - Transport management (Queue implementation)
- `templates/` - HTML templates
- `static/` - CSS and static assets

## Testing

Before submitting a pull request:

1. Test all CRUD operations (Create, Read, Update, Delete)
2. Verify data persistence (CSV files)
3. Check the web interface in different browsers
4. Ensure no console errors

## Questions?

Feel free to open an issue with the `question` label if you have any questions about contributing.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on what is best for the community
- Show empathy towards other community members

Thank you for contributing! 🎉
