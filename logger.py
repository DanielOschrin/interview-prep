import logging

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,
    # Set the logging level
    format="%(levelname)s - %(message)s",
    # Format the log messages
)

# Create a logger
log = logging.getLogger()  # Name your logger (optional)
