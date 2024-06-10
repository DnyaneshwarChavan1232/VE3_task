# Django web application for Titanic Data Analysis.

This Django web application allows users to upload CSV files containing Titanic passenger data, analyze the data, and visualize it using histograms.

## Features

- Upload CSV files containing Titanic passenger data.
- View basic statistics and information about the uploaded dataset.
- Visualize the data with histograms for Age and Fare attributes.

## Installation

1. Clone the repository:

    ```
    git clone <repository_url>
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Run the Django server:

    ```
    python manage.py runserver
    ```

4. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Visit the homepage and upload a CSV file containing Titanic passenger data.
2. Once the file is uploaded, you'll see basic statistics and information about the dataset.
3. Navigate to the visualization page to view histograms for Age and Fare attributes.

## Dependencies

- Django
- pandas
- seaborn
- matplotlib
