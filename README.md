# FakeBot Buster Project Documentation

## Tools and Technologies

- **Transformers Library**:
  - Helps us load pre-trained models and tokenizers from Hugging Face, making it easy to use advanced machine learning models.
  
- **Streamlit**:
  - This is a framework that allows us to create an interactive web application, providing a user-friendly interface for our project.
  
- **PyTorch**:
  - This is the backend framework we use for running the model and making predictions.
  
- **Hugging Face Hub**:
  - This is an online repository where we get our pre-trained models and tokenizers.
  
- **Bootstrap**:
  - This is used to style the Streamlit UI, ensuring it looks clean and professional.
  
- **Python**:
  - This is the main programming language we use to develop the application.
  
- **VS Code**:
  - This is an Integrated Development Environment (IDE) we use for writing, editing, and debugging our code.

![Blank diagram](https://github.com/SaiKrishnaKoduri/FakeBot-Busters/assets/54131260/efc4a1d8-47d1-41a8-9497-0269d6962d9f)


## Project Flow

1. **User Input**:
   - Users enter the text they want to verify.

2. **Chatbot Web Interface**:
   - Displays the user input text on a Streamlit-based web interface.

3. **Model Selection**:
   - Users choose between different models: BERT, ALBERT, or RoBERTa.

4. **Text Tokenization**:
   - The input text is broken down into smaller tokens for processing.

5. **Model Inference**:
   - The tokenized text is analyzed by the selected model to predict if the input is true or fake.

6. **Prediction, Confidence Scores, and Processing Time**:
   - The system generates a prediction along with confidence scores and processing time.

7. **Output Formatting**:
   - The prediction and confidence scores are formatted into a readable response.

8. **Display Response**:
   - The final formatted response is shown to the user on the web interface.

## References

- [Transformers Library Documentation](https://huggingface.co/transformers/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [Hugging Face Hub](https://huggingface.co/hub/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- [Python Documentation](https://docs.python.org/3/)
- [VS Code Documentation](https://code.visualstudio.com/docs)
