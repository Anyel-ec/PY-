## Title: **Email Classification Using Support Vector Machine (SVM)**

### Description

This project utilizes a Support Vector Machine (SVM) to classify emails into 'Spam' or 'Not Spam'. The model is trained using features extracted from email data, and its performance is evaluated with standard metrics. The confusion matrix is visualized to provide an intuitive understanding of the model's classification performance.

### Requirements

- Python 3.x
- pandas
- scikit-learn
- seaborn
- matplotlib

You can install the necessary dependencies using pip:

```bash
pip install pandas scikit-learn seaborn matplotlib
```

### Main Script

The main script performs the following steps:

1. **Load the Dataset**: Reads a CSV file containing email data.
2. **Select Relevant Columns**: Extracts features and labels from the dataset.
3. **Split the Data**: Divides the dataset into training and test sets (80% training, 20% test).
4. **Train the Model**: Fits a Support Vector Machine (SVM) with a linear kernel using the training data.
5. **Predict and Evaluate**: Makes predictions on the test set and calculates performance metrics such as accuracy, confusion matrix, and classification report.
6. **Visualization**: Displays a heatmap of the confusion matrix for a visual representation of the model's performance.

### How to Run the Project

1. **Place the Dataset**: Ensure the CSV file of the dataset (`emails.csv`) is in the correct path (`/content/drive/MyDrive/Datasets/emails.csv`), or update the path in the code as needed.

2. **Run the Code**: Execute the script in your Python environment to perform the email classification.

```python
python script_name.py
```

### Results

The script will print the following results to the console:

- **Accuracy**: Indicates the proportion of correct predictions.
- **Confusion Matrix**: A table showing true vs. false predictions.
- **Classification Report**: Includes precision, recall, and F1-score for each class.

Additionally, a visualization of the confusion matrix will be generated using `seaborn` and `matplotlib`.

### Example Output

```
Accuracy: 0.9594

Confusion Matrix:
 [[715  24]
 [ 18 278]]

Classification Report:
               precision    recall  f1-score   support

           0       0.98      0.97      0.97       739
           1       0.92      0.94      0.93       296

    accuracy                           0.96      1035
   macro avg       0.95      0.95      0.95      1035
weighted avg       0.96      0.96      0.96      1035
```

### Visualization

The confusion matrix is visualized in a heatmap, which helps in understanding the model’s classification results more intuitively.

### Contributions

Contributions and improvements to the project are welcome. If you would like to contribute, please open an issue or submit a pull request.

### License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the code under the terms of this license.

### Contact

For any questions or comments, you can contact the author at Anyel EC