from gptdriver_client import GptDriver

if __name__ == "__main__":
    gptd = GptDriver(api_key="<YOUR_API_KEY>", platform="Android")

    gptd.execute("Navigate to the app home screen")
    # ... other actions ...
    gptd.set_session_status("success")
