from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from models import InvoiceDetails
from extract_text import extract_text_from_pdf
import json


def process_invoice_text(text: str) -> InvoiceDetails:

    system_prompt = "Convert all numbers in the provided text that contain commas into a format without commas. For example, convert 6,790 to 6790. Ensure that all numbers with commas are correctly converted to their non-comma equivalents."

    parser = PydanticOutputParser(pydantic_object=InvoiceDetails)

    prompt = PromptTemplate(
        template="Answer the user query.\n{system_prompt}\n{query}\n{format_instructions}",
        input_variables=["query"],
        partial_variables={
            "system_prompt": system_prompt,
            "format_instructions": parser.get_format_instructions(),
        },
    )

    model = ChatGoogleGenerativeAI(
        model="gemini-pro", api_key="AIzaSyCWiw_TSv7HHxfpMdykrMBo6BBRCNSbd14"
    )

    chain = prompt | model | parser

    prompt = f"Extract the customer details, items, and total amount from the following invoice text:\n\n{text}\n\n"

    result = chain.invoke({"query": prompt})

    return result


def format_to_json(res: InvoiceDetails) -> str:
    customer_details = res.customer_details.model_dump()
    items = [item.model_dump() for item in res.items]
    total_amount = res.total_amount.model_dump()

    result = {
        "customer_details": customer_details,
        "items": items,
        "total_amount": total_amount,
    }

    return json.dumps(result, indent=4)
