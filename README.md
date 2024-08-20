# Diabetes Prediction Web Application

This is a web application built with Flask that predicts whether a person is diabetic based on several health parameters. The application utilizes a pre-trained neural network model to make predictions.

## Table of Contents

- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)


## About The Project

This project aims to provide a user-friendly interface for predicting diabetes using a machine learning model. Users can input their health data, and the model will predict whether they are likely to have diabetes.

### Features

- User-friendly web interface built with Flask and Bootstrap.
- Input fields for various health parameters.
- Real-time prediction based on user input.

## Getting Started

### Prerequisites

To run this project, you will need to have Python and pip installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MohanKumar2002/Diabetes-Prediction
   cd diabetes_prediction_app
   ```

2. Install the required Python packages:

   ```bash
   pip install Flask numpy keras tensorflow
   ```

3. Ensure you have the model files (`model.json` and `model.weights.h5`) and the dataset (`pima-indians-diabetes.csv`) in the project directory.

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Fill in the input form with your health parameters and click "Predict" to see the result.

### Input Parameters

- Number of times pregnant
- Plasma glucose concentration
- Diastolic blood pressure (mm Hg)
- Triceps skin fold thickness (mm)
- 2-Hour serum insulin (mu U/ml)
- Body mass index (weight in kg/(height in m)^2)
- Diabetes pedigree function
- Age (years)

## Roadmap

- Add more features for data visualization.
- Improve the model's accuracy with more training data.
- Create a mobile-friendly version of the application.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

Project Link: https://github.com/MohanKumar2002/Diabetes-Prediction
