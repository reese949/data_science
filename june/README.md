# June

A heart disease prediction model powered by machine learning.

## Overview

**June** is a heart disease prediction model powered by machine learning. At its core, June utilizes the k-nearest neighbors (KNN) algorithm to predict the user's risk for heart disease based on key biometrics.

While KNN is a relatively straightforward machine learning technique, the purpose and potential impact of this project are what truly justify giving it a name. June represents not just a technical achievement, but a critical step toward improving healthcare and saving lives. Though still in its early stages, June symbolizes the beginning of something much greater—an AI that will continue to learn, grow, and eventually play an even more vital role in healthcare.

## Features

- **User-Friendly Interface**: June asks the user for critical health information like age, gender, cholesterol levels, resting blood pressure, and more.
- **Data Processing**: The user's input is validated, transformed into a structured format, and used for predictions.
- **Heart Disease Prediction**: Based on the user's data, the model predicts if they are at risk for heart disease.
- **Machine Learning**: June uses the k-nearest neighbors algorithm and is trained on a dataset of heart disease patients.
- **Model Evaluation**: Accuracy of the model is displayed, showing how well it performs in predicting heart disease.

## Requirements (part 1)

This project requires the following:

- Python 3.7 or higher
- pandas
- scikit-learn

To install the required dependencies, you can use `pip` by running:

```bash
pip install pandas scikit-learn
```

## Requirements (part 2)

Additionally, you will need to know these specific health metrics:

- Resting Blood Pressure (e.g. 120/80 mm Hg)
- Fasting Blood Sugar levels (e.g. 105 mg/dl)
- Cholesterol levels (e.g. 200 mm/dl)
- Maximum Heart Rate During Peak Exercise (e.g. 150 bpm) (Determined from an Exercise Stress Test)
- The slope of your Peak Exercise ST segment [e.g. up, flat, down] (Refer to your Exercise Stress Test)


## How It Works

1. **Welcome Message**: June greets the user and collects their name.
2. **User Input**: June asks the user to provide personal health information such as age, gender, blood pressure, cholesterol levels, etc.
3. **Data Validation**: June ensures that the user's input is valid and falls within a reasonable range.
4. **Model Training**: The model is trained on a dataset of heart disease patients (stored in `patient_data.csv`).
5. **Prediction**: The trained model uses the user’s data to predict the risk of heart disease.
6. **Accuracy Evaluation**: The model’s accuracy is displayed, indicating how well it can predict heart disease for the general population.

## How to Install and Run June

To run June on your computer, you'll want to click on the file `june.py`. Doing so will open the file on Github. Once you've opened `june.py` on Github, click on the button with three dots, located in the top right corner of your screen. Then, click download from the drop down menu. Go ahead and follow the same process for the `patient_data.csv` file. Once you have both of these files downloaded, follow this process:

1. **Navigate to your Downloads folder**:
   - Open the terminal or command line on your system.

   **For Windows**:
   - Press `Win + R`, type `cmd`, and press Enter to open the Command Prompt.
   - Type the following command to navigate to your `Downloads` folder:
     ```bash
     cd %HOMEPATH%\Downloads
     ```

   **For macOS/Linux**:
   - Open the terminal application.
   - Type the following command to navigate to your `Downloads` folder:
     ```bash
     cd ~/Downloads
     ```

2. **Install the required dependencies**:
   Ensure that Python 3.x is installed on your system. Then, install the necessary Python packages by running:
   ```bash
   pip install pandas scikit-learn
   ```

3. **Run the program**:

    After installing the dependencies, run the program by typing the following command:
    ```python
    python june.py
    ```

**Note**: `june.py` and `patient_data.csv` must be in the same folder for `june.py` to run properly. 

## Future Improvements

- **Model Enhancement**: Experiment with other algorithms (e.g., logistic regression, decision trees) to improve the prediction accuracy.
- **User Interface**: Add a web or mobile interface for easier access and usability.
- **Additional Features**: Integrate additional biometric data, such as family history of heart disease, lifestyle factors (e.g., exercise habits, diet), and genetic data.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions could include improving the model, enhancing the user interface, or extending the dataset.

## License

This project is open-source and licensed under the MIT License.

## Data Sources

**Data Sources:**
1. Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
2. University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
3. University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
4. V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.

**Dataset Composition:**
Hungarian: 294 observations
Switzerland: 123 observations
Cleveland: 303 observations
Long Beach VA: 200 observations
Statlog (Heart) Data Set: 270 observations

**Special Comments:** [This dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) was created by combining different datasets already available independently but not combined before. In this dataset, 5 datasets are combined over 11 common features which makes it the largest publicly available dataset for heart-disease research purposes.
