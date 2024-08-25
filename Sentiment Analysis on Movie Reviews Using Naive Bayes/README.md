## Title: **Sentiment Analysis on Movie Reviews Using Naive Bayes**

### Description

This project uses a Naive Bayes classifier to analyze sentiment in movie reviews from the IMDB dataset. The Bag of Words technique is employed for text representation, and the model's performance is evaluated using standard classification metrics. The confusion matrix visualization provides a clear understanding of the model's performance.

### Requirements

- Python 3.x
- pandas
- scikit-learn
- seaborn
- matplotlib

You can install the required dependencies using pip:

```bash
pip install pandas scikit-learn seaborn matplotlib
```

### Main Script

The main script performs the following steps:

1. **Load the Dataset**: Reads a CSV file containing movie reviews and their sentiments (positive/negative).
2. **Prepare the Data**: Maps the sentiments to binary values and splits the dataset into training and test sets.
3. **Text Representation**: Converts text reviews into a feature matrix using the Bag of Words technique.
4. **Train the Model**: Fits a Multinomial Naive Bayes classifier using the training data.
5. **Evaluate the Model**: Predicts sentiments for the test reviews and calculates performance metrics such as accuracy, confusion matrix, and classification report.
6. **Visualization**: Displays a confusion matrix as a heatmap for a visual interpretation of the results.

### How to Run the Project

1. **Place the Dataset**: Ensure the CSV file of the dataset (`IMDB Dataset.csv`) is in the correct path (`/content/drive/MyDrive/Datasets/IMDB Dataset.csv`), or update the path in the code as needed.

2. **Run the Code**: Execute the script in your Python environment to perform sentiment analysis.

```python
python script_name.py
```

### Results

The script will print the following results to the console:

- **Accuracy**: Measures the proportion of correct predictions.
- **Confusion Matrix**: A table showing true vs. false predictions.
- **Classification Report**: Includes precision, recall, and F1-score for each class.

Additionally, a confusion matrix visualization will be generated using `seaborn` and `matplotlib`.

### Example Output

```
Accuracy: 0.8448

Confusion Matrix:
 [[4218  743]
 [ 809 4230]]

Classification Report:
               precision    recall  f1-score   support

           0       0.84      0.85      0.84      4961
           1       0.85      0.84      0.84      5039

    accuracy                           0.84     10000
   macro avg       0.84      0.84      0.84     10000
weighted avg       0.84      0.84      0.84     10000
```

### Visualization

The confusion matrix is visualized in a heatmap, which facilitates the interpretation of the model's results.

### Contributions

Contributions and improvements to the project are welcome. If you would like to contribute, please open an issue or submit a pull request.

### License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the code under the terms of this license.

### Contact

For any questions or comments, you can contact the author at [Anyel EC](mailto:cyberdevmatrix@gmail.com).