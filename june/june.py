from datetime import datetime
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

def welcome():
    # Welcome message
    print("\nHello, my name is June. I'm a heart disease prediction model powered by machine learning.")
    username = input("What is your name? ")

    # Process time
    current_time = datetime.now()
    hour = current_time.hour

    # Determine greeting based on hour
    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    # Display greeting
    print(f"\n{greeting}, {username}!")
    print("I'm going to ask you for some very specific health information in order to generate a heart disease prediction for you.\n")

    # Ask user to continue or exit program
    while True:
        try:
            answer = input("Are you ready to proceed? If yes, then type yes. If no, type no: ").strip().lower()
            if answer == "yes":
                print("\nWonderful!", end="")
                break
            elif answer == "no":
                sys.exit("Closing June at user request.")
            else:
                print(f"\nPlease enter yes or no.\n")
        except Exception as e:
            print(f"Error: {e}. Please try again.")
        except EOFError:
            sys.exit("Exiting June. CTRL+D was pressed.")


def get_biometrics():

    """
    Collects and validates user input, creates a DataFrame from the input data.
    """


    # Helper function for validating user input
    def validate_input(prompt, data_type, condition):
        while True:
            try:
                response = input(prompt)
                converted_response = data_type(response)
                if condition(converted_response) == True:
                    return converted_response
                print("Invalid input. Please try again.")
            except ValueError:
                print(f"Please enter a valid input.")


    # Collect user data
    user_age = validate_input("\nFirst off, what is your age? (If you're 25, simply input 25): \n", int, lambda x: 0 <= x <= 115)
    user_sex = (validate_input("\nWhat is your gender? (Input M for Male and F for Female): \n", str, lambda x: x.upper() in ['M', 'F'])).upper()
    user_resting_bp = validate_input("\nWhat is your resting blood pressure? (Only include the systolic value. For example, if your blood pressure is 120/80, then only include 120): \n", int, lambda x: 90 <= x <= 225)
    user_cholesterol = validate_input("\nWhat is your cholesterol level? (serum cholesterol [mm/dl] e.g., 200): \n", float, lambda x: 50 <= x <= 750)
    user_fasting_bs = validate_input("\nIs your fasting blood sugar greater than 120 mg/dl? Input 1 for Yes, or 0 for No: \n", int, lambda x: x in [0, 1])
    user_max_hr = validate_input("\nWhat is your maximum heart rate during peak exercise? (e.g., 150 bpm. Refer to your Exercise ECG): \n", int, lambda x: 40 <= x <= 202)
    user_angina = (validate_input("\nDo you have chest pain while exercising? (Input Y for Yes, or N for No): \n", str, lambda x: x.upper() in ['Y','N'])).upper()
    user_st_slope = validate_input("\nWhat is your ST Slope? Write either Up, Down, or Flat. (Refer to your Exercise ECG): \n", str, lambda x: x.capitalize() in ['Up','Down','Flat']).capitalize()

    # Create a dictionary from user inputs
    user_data = {
    "Age": user_age,
    "Sex": user_sex,
    "RestingBP": user_resting_bp,
    "Cholesterol": user_cholesterol,
    "FastingBS": user_fasting_bs,
    "MaxHR": user_max_hr,
    "ExerciseAngina": user_angina,
    "ST_Slope": user_st_slope}


    # Create a DataFrame from the user data dictionary
    user_df = pd.DataFrame([user_data])


    # Convert categorical columns to dummies
    user_dummies = pd.get_dummies(user_df, columns=['Sex','ExerciseAngina','ST_Slope'])


    return user_dummies


# This function prepares the patient dataset for machine learning
def prep_dataset(user_df):

    """
    prep_dataset() loads the patient dataset, handles missing values, drops unnecessary columns,
    and prepares the patient dataframe to match the structure of the user dataframe.
    """

    # Load the patient dataset into a DataFrame
    hd = pd.read_csv('patient_data.csv')


    # To be user-friendly, we are dropping these columns from our model to avoid having to ask the user these metrics.
    hd = hd.drop(columns=['ChestPainType','RestingECG'])


    # Subtitute the median for the zero values in cholesterol column
    def fix_cholesterol(value):
        if value == 0 or pd.isna(value):
            return hd['Cholesterol'].median()
        else:
            return value

    hd['Cholesterol'] = hd['Cholesterol'].apply(fix_cholesterol)


    # Drop rows with a resting blood pressure of zero
    hd = hd[hd['RestingBP'] != 0]

    # Cleaning Complete


    # Create Dummy Variables
    patient_df = pd.get_dummies(hd, columns=['Sex','ExerciseAngina','ST_Slope'])

    # Use column names from user_df to filter patient_df
    desired_cols = user_df.columns.tolist() + ['HeartDisease']

    # Filter the patient df with the desired cols list
    patient_df = patient_df[desired_cols]

    return patient_df


# This function takes the patient_df and uses the target variables to train a KNN model
def deploy_classifier(patient_df, user_df):

    """
    The deploy_classifier() function isolates patient biometrics into X, while isolating
    the target variable (diagnosis) into y.

    Then, train_test_split() is called, which splits the training features 80/20 and
    stores them in X. Finally, the target variable, HeartDisease column, is split 80/20 and stored in y.

    A quick overview of the output from train_test_split():

    X_train = Features (biometrics) for training the model.
    y_train = Target variable (diagnosis) for training the model.

    X_test = Features (biometrics) for testing the model by making predictions.
    y_test = Actual target values (diagnosis) for evaluating the predictions.

    """

    # # Separate features (X) and target (y)
    X = patient_df.drop('HeartDisease', axis=1)
    y = patient_df['HeartDisease']

    # Split data into training and testing sets (80%/20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalize features using MinMaxScaler
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    user_df_scaled = scaler.transform(user_df)

    # Train KNN classifier
    knn = KNeighborsClassifier(n_neighbors=25)
    knn.fit(X_train_scaled, y_train)

    # Evaluate model with accuracy score
    predictions = knn.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, predictions)
    accuracy = int(round(accuracy, 2) * 100)

    # Predict user's heart disease risk
    user_prediction = knn.predict(user_df_scaled)

    if user_prediction == 0:
        print("\nBased on the model’s prediction and your input, you are not at risk for heart disease! Hooray!")
    else:
        print("\nBased on the model’s prediction and your input, you are at risk for heart disease!")

    print(f"This machine learning model has an accuracy of: {accuracy}%")
    print("\nPlease consult with a healthcare professional for a more detailed analysis.\n")



# Main function
def main():
    # Clear terminal for better user experience
    os.system('cls' if os.name == 'nt' else 'clear')

    # Welcome the user
    welcome()

    # Create dataframe from user biometrics
    user_df = get_biometrics()

    # Clear terminal for better user experience after the user has answered the final question
    os.system('cls' if os.name == 'nt' else 'clear')

    # Ensure the heart disease dataframe matches the user dataframe
    patient_df = prep_dataset(user_df)

    # Deploy and train a classifier with patient_df, then use the classifier to make a prediction for the user
    deploy_classifier(patient_df, user_df)


if __name__ == "__main__":
    main()
