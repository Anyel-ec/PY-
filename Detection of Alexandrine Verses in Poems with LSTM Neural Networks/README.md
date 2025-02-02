# Alexandrine Verse Identification in Poems with LSTM

This project uses an LSTM (Long Short-Term Memory) neural network model to identify Alexandrine verses in poems. An Alexandrine verse is a poetic line consisting of 14 syllables. The model trains on tokenized poems and predicts whether a given verse is Alexandrine or not.

## Description

The script performs the following tasks:

1. **Data Loading and Preprocessing:** Reads a CSV file with poems, tokenizes the text, and converts the poems into sequences of integers.
2. **Syllable Counting:** Implements a function to count the number of syllables in a verse.
3. **LSTM Model Training:** Builds, compiles, and trains an LSTM model to classify verses as Alexandrine or non-Alexandrine.
4. **Prediction:** Allows for the prediction of whether the verses of a new poem are Alexandrine or not.

## Required Libraries

This project requires the following libraries:

- `numpy` for numerical operations and array manipulation.
- `tensorflow` for creating and training the LSTM model.
- `pandas` for data manipulation.
- `re` for text processing with regular expressions.

### Installing Dependencies

You can install the required libraries using `pip`. Make sure `pip` is updated and run the following commands:

```bash
pip install numpy pandas tensorflow
```

## Usage

1. **Prepare the CSV File:** Ensure you have a CSV file (`poems.csv`) with a column named `content` containing the poems.

2. **Run the Script:** Execute the Python script that performs data loading, model training, and prediction.

3. **Prediction Example:** You can test the model with a new poem as shown below:

    ```python
    new_poem = "La princesa está triste… ¿qué tendrá la princesa?\nEl viento de la noche gira en el cielo y canta"
    print(predict_alexandrine(new_poem))
    ```

## Code Details

### `count_syllables(verse)`

Counts the number of syllables in a verse considering diphthongs and sinalefas.

### `is_alexandrine(syllables)`

Checks if the number of syllables in a verse equals 14.

### LSTM Model Construction

1. **Embedding Layer:** Represents words in a dense vector space.
2. **LSTM Layer:** Captures temporal dependencies in the text.
3. **Dense Layer:** Provides the final output with a sigmoid activation for binary classification.

### Model Training

The model is trained with 80% of the data for training and 20% for validation over 10 epochs.

## Contributions

If you wish to contribute to the project, please open an issue or a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.