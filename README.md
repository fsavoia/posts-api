# Blog API

The Blog API is a FastAPI-based application designed to manage posts in a blog. It provides endpoints for creating, retrieving, updating, and deleting blog posts, as well as user authentication.

## Getting Started

These instructions will help you set up and run the Blog API on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x installed on your machine
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)

### Installation

1. Clone the repository:

   ```shell
   git clone <repository_url>

2. Navigate to the project directory:

   ```shell
   cd <project_directory>

3. Install the required Python packages:

   ```shell
   pip install -r requirements.txt

### Running the Application

1. Ensure your database connection is properly configured in database.py.

2. Run the application:

   ```shell
   uvicorn main:app --reload

This command starts the FastAPI development server, and your API should be accessible at [localhost:8000](http://localhost:8000)

### API Documentation

Visit http://localhost:8000/docs to access the interactive API documentation (Swagger UI) to explore and test the available endpoints.

### Configuration

The application's configuration is stored in the config.py file. You can modify settings like the application title, description, and contact information there.

### Routers

The application includes three routers: auth, posts, and users. You can find the route definitions and logic in the corresponding router files in the routers directory.

### Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: git checkout -b feature/your-feature-name.
3. Make your changes and ensure the code is properly formatted.
4. Write tests if applicable and ensure all tests pass.
5. Commit your changes with a descriptive commit message.
6. Push your changes to your fork: git push origin feature/your-feature-name.
7. Create a pull request against the main branch of the original repository.

### License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.

### Acknowledgments

FastAPI: A modern Python web framework for building APIs with automatic interactive documentation.
SQLAlchemy: A powerful and flexible SQL toolkit and Object-Relational Mapping (ORM) library for Python.
uvicorn: ASGI server for running Python web applications.

### Contact

For questions or feedback, please contact:

Name: Felipe Savoia
Email: fmsavoia@gmail.com

Thank you for using the Blog API!