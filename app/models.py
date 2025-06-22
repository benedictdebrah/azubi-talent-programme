from pydantic import BaseModel, Field

class BankClient(BaseModel):
    age: int = Field(..., description="Age of the client")
    job: str = Field(..., description="Type of job")
    marital: str = Field(..., description="Marital status")
    education: str = Field(..., description="Level of education")
    default: str = Field(..., description="Has credit in default? (yes/no)")
    balance: int = Field(..., description="Average yearly balance in euros")
    housing: str = Field(..., description="Has housing loan? (yes/no)")
    loan: str = Field(..., description="Has personal loan? (yes/no)")
    contact: str = Field(..., description="Contact communication type")
    day: int = Field(..., description="Last contact day of the month (1-31)")
    month: str = Field(..., description="Last contact month of year (e.g., jan, feb)")
    duration: int = Field(..., description="Last contact duration, in seconds")
    campaign: int = Field(..., description="Number of contacts performed during this campaign")
    pdays: int = Field(..., description="Days since client was last contacted (-1 means not previously contacted)")
    previous: int = Field(..., description="Number of contacts performed before this campaign")
    poutcome: str = Field(..., description="Outcome of the previous marketing campaign (e.g., success, failure, unknown)")
