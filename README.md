# PAC Parse App

PAC Parse App is a Python application that parses Proxy Auto-Config (PAC) files and provides a web interface to test and evaluate proxy configurations. It utilizes the Flask web framework to serve the application and pacparser library for parsing PAC files.

## Features

- Parse and evaluate Proxy Auto-Config (PAC) files
- Test and validate proxy configurations
- Web interface for easy interaction

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker (optional)

### Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/SYNically-ACKward/pac-parse-app.git
   ```

2. Navigate to the project directory:
   ```shell
   cd pac-parse-app
   ```

3. Install the required Python dependencies:
   ```shell
   pip install -r requirements.txt
   ```

### Usage

1. Start the application:
   ```shell
   python app.py
   ```

2. Open a web browser and visit `http://localhost:5000` to access the application.

### Docker Support

Alternatively, you can run the application using Docker.

1. Build the Docker image:
   ```shell
   docker build -t pac-parse-app .
   ```

2. Run the Docker container:
   ```shell
   docker run -p 5000:5000 pac-parse-app
   ```

3. Access the application by opening a web browser and visiting `http://localhost:5000`.

### Configuration

The application provides a default configuration, but you can customize it by modifying the `config.py` file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

