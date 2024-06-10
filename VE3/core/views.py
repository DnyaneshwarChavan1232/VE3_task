import pandas as pd
from io import StringIO, BytesIO
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Titanic

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            if not uploaded_file.name.endswith('.csv'):
                return render(request, 'core/error.html', {'error_message': 'Uploaded file is not a CSV.'})
            try:
                df = pd.read_csv(uploaded_file)
                for _, row in df.iterrows():
                    titanic_instance = Titanic(
                        PassengerId=row['PassengerId'],
                        Survived=row['Survived'],
                        Pclass=row['Pclass'],
                        Name=row['Name'],
                        Sex=row['Sex'],
                        Age=row['Age'] if not pd.isna(row['Age']) else None,
                        SibSp=row['SibSp'],
                        Parch=row['Parch'],
                        Ticket=row['Ticket'],
                        Fare=row['Fare'] if not pd.isna(row['Fare']) else None,
                        Cabin=row['Cabin'] if not pd.isna(row['Cabin']) else None,
                        Embarked=row['Embarked'] if not pd.isna(row['Embarked']) else None
                    )
                    titanic_instance.save()

                request.session['df'] = df.to_json()
            except Exception as e:
                return render(request, 'core/error.html', {'error_message': f"Error reading CSV file: {e}"})

            first_few_rows = df.head().to_html()
            buffer = StringIO()
            df.info(buf=buffer)
            info = buffer.getvalue()
            numeric_df = df.select_dtypes(include='number')
           # description = numeric_df.describe().to_html()
            means = numeric_df.mean().to_frame().to_html()
            medians = numeric_df.median().to_frame().to_html()
            std_deviation = numeric_df.std().to_frame().to_html()
            missing_values = df.isnull().sum().to_frame().to_html()

            return render(request, 'core/display.html', {
                'first_few_rows': first_few_rows,
                'info': info,
                #'description': description,
                'means': means,
                'medians': medians,
                'std_deviation': std_deviation,
                'missing_values': missing_values,
            })
    else:
        form = UploadFileForm()
    return render(request, 'core/upload.html', {'form': form})

def visualize(request):
    if 'df' in request.session:
        df_json = request.session['df']
        df = pd.read_json(StringIO(df_json))

        if 'Age' in df.columns and df['Age'].isnull().any():
            df = df.dropna(subset=['Age'])
        if 'Fare' in df.columns and df['Fare'].isnull().any():
            df = df.dropna(subset=['Fare'])

        age_histogram = create_histogram(df, 'Age', 'Histogram of Age', 'Age', 'Frequency')
        fare_histogram = create_histogram(df, 'Fare', 'Histogram of Fare', 'Fare', 'Frequency')

        return render(request, 'core/visualization.html', {
            'age_histogram': age_histogram,
            'fare_histogram': fare_histogram
        })
    else:
        return render(request, 'core/error.html', {'error_message': 'No data found to visualize'})

def create_histogram(df, column, title, xlabel, ylabel):
    plt.figure()
    sns.histplot(df[column], kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    histogram = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return histogram
