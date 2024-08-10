# Invoice PDF Extraction Tool

This project is a command-line tool designed to extract key information from invoice PDFs using advanced AI models. The extracted details include customer information, product details, and total amounts, all parsed and structured in a JSON format.

## Features
- **Customer Details Extraction**: Extracts customer name, billing address, phone number, email, and other relevant details from the invoice.
- **Product Details Extraction**: Captures product descriptions, HSN codes, quantities, rates, and amounts from the invoice.
- **Total Amount Calculation**: Retrieves and computes the total payable amount, including taxes and other charges.
- **Error Handling**: Identifies and resolves common extraction errors, such as merged fields, ensuring accurate data parsing.

## Libraries Used

### PDF Extraction
- **[pypdf](https://pypi.org/project/pypdf/)**: Utilized for parsing and extracting raw text from PDF files.

### Language Models
- **[LangChain](https://www.langchain.com/)**: Integrated for chaining LLM operations and facilitating complex prompt workflows.
- **[Google Gemini](https://cloud.google.com/gemini)**: Employed as the LLM for processing and understanding extracted text data.

### Data Validation & Processing
- **[Pydantic](https://pypi.org/project/pydantic/)**: Used for data validation and ensuring the extracted information matches predefined data models.

### Command-Line Interface
- **[Click](https://pypi.org/project/click/)**: Provides a simple and intuitive command-line interface for running the tool.

## Screenshots

Here are some screenshots demonstrating the functionality of the project:

### Screenshot 1:
![Screenshot 1](https://raw.githubusercontent.com/dishant-yadav/swipe-assignment-pdf-extraction/main/output/Sample%20Invoice%201.png)

### Screenshot 2:
![Screenshot 1](https://raw.githubusercontent.com/dishant-yadav/swipe-assignment-pdf-extraction/main/output/Sample%20Invoice%202.png)

## How to Use

1. **Installation**: Clone the repository and install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Tool**: Execute the CLI tool with the desired PDF file as input:
    ```bash
    python main.py extract --file_path <path_to_invoice_pdf>
    ```

3. **View Output**: The output will be displayed in JSON format, showing the extracted details.
