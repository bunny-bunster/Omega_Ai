def format_data(data):
    """Format the input data for processing."""
    return str(data).strip()

def log_message(message):
    """Log a message to the console."""
    print(f"[LOG] {message}")

def validate_input(user_input):
    """Validate the user input for the AI."""
    return isinstance(user_input, str) and len(user_input) > 0
