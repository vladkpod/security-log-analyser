import logging
import re

def parse_logs(log_file_path):
    # Regular expression patterns for log parsing
    log_entry_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (.*)'

    # Define a list to store parsed log entries
    parsed_logs = []

    # Read the log file
    with open(log_file_path, 'r') as file:
        for line in file:
            # Extract relevant fields using regex
            match = re.search(log_entry_pattern, line)

            if match:
                ip_address = match.group(1)
                datetime = match.group(2)
                log_message = match.group(3)

                # Add the parsed log entry to the list
                parsed_logs.append({
                    'ip_address': ip_address,
                    'datetime': datetime,
                    'log_message': log_message,
                    'raw_entry': line.strip()
                })

    return parsed_logs

if __name__ == '__main__':
    # Specify the path to the log file you want to parse
    log_file_path = r'C:\Users\44788\security-log-analyzer\logs\sample.log'

    # Configure logging
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')

    # Call the log parsing function
    parsed_logs = parse_logs(log_file_path)

    # Display the parsed log entries
    for log in parsed_logs:
        logging.debug("Parsed log entry:")
        logging.debug(f"  IP Address  : {log['ip_address']}")
        logging.debug(f"  Date & Time : {log['datetime']}")
        logging.debug(f"  Log Message : {log['log_message']}")
        logging.debug(f"  Raw Entry   : {log['raw_entry']}")
        logging.debug("")  # Empty line for better readability

    # Perform additional analysis or event detection based on the parsed logs
    # Add your own logic here

    # Example: Count the number of parsed logs
    num_logs = len(parsed_logs)
    logging.info(f"\nNumber of parsed logs: {num_logs}\n")
