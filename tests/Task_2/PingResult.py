from pydantic import BaseModel, ValidationError, Field
from datetime import datetime
from typing import Optional, List


class PingResult(BaseModel):
    """
    I assumed that `source_name` is unique, so we can fetch more data from inventory file;
    if it's required to present to the clients. In this way we can keep the Ping table light.
    """
    source_name: str = Field(..., description="The source name of the host initiating the ping")
    url: str = Field(..., description="The IP address or DNS name of the target device being pinged")
    timestamp: datetime = Field(..., description="The datetime when the ping was executed")
    status: str = Field(..., description="The result of the ping operation (success, failure)")
    latency_ms: Optional[int] = Field(None,
                                      description="The round-trip time in milliseconds (only if the ping was successful)")
    error_message: Optional[str] = Field(None,
                                         description="Descriptive text of any error encountered (only for failed pings)")



def validate_ping_data(data: List[dict]) -> List[dict]:
    validated_data = []
    for entry in data:
        try:
            validated_entry = PingResult(**entry).dict()
            validated_data.append(validated_entry)
        except ValidationError as e:
            print(f"Error validating data: {e}")
    return validated_data
