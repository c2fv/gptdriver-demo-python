# gptdriver-demo-python
A demonstration repo of the GptDriver Python SDK usage

# Setup
Install the GptDriver SDK
```bash
pip install gptdriver-client
``` 

# Usage
Simple example of how to use the GptDriver SDK in Python:
```python
from gptdriver_client import GptDriver

gptd = GptDriver(...)

gptd.execute("Navigate to the app home screen")
# ... other actions ...
gptd.set_session_status("success")
```
