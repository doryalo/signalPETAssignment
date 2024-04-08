# Animal X-Ray Management System
## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher is installed on your system.
- Pip is installed for managing Python packages.
- Virtualenv is installed for creating isolated Python environments.
## Setup

To set up the project, follow these steps:

1. **Clone the repository:**

```bash
git clone git@github.com:doryalo/signalPETAssignment.git
```

2. **Create and activate a virtual environment (optional):**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install the required dependencies:**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
   
Create a `.env` file in the root directory of your project and add your configuration variables, such as the AWS S3 bucket name and credentials if necessary.

```env
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
BUCKET_NAME=your-s3-bucket-name
```


## Running the Application

To run the application, execute:

```bash
python run.py
```

This will start a development server on `http://127.0.0.1:5000`.

## Testing
Example requests are included in the `tests.json`.
You can import them into Postman.
