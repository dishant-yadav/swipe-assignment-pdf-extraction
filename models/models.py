from pydantic import BaseModel


class CustomerDetails(BaseModel):
    name: str
    billing_address: str
    phone: str
    email: str
    enquiry_id: str
    place_of_supply: str


class Item(BaseModel):
    description: str
    hsn: str
    rate: float
    quantity: int
    amount: float


class TotalAmount(BaseModel):
    taxable_amount: float
    igst: float
    round_off: float
    tcs: float
    total: float

