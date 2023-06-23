import logging
import json
import warnings
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Add this line before importing pyplot
import matplotlib.pyplot as plt
import numpy as np

# Disable font logging
logging.getLogger('matplotlib.font_manager').disabled = True

def parse_json_logs(log_file_path, parsed_logs):
    # Read the log file
    with open(log_file_path, 'r') as file:
        logs = json.load(file)
        parsed_logs.extend(logs)

def filter_logs(logs, filters, logical_operator="AND"):
    filtered_logs = logs

    # Apply filters
    for key, values in filters.items():
        if logical_operator.upper() == "AND":
            filtered_logs = [log for log in filtered_logs if all(log.get(key) == value for value in values)]
        elif logical_operator.upper() == "OR":
            filtered_logs = [log for log in filtered_logs if any(log.get(key) == value for value in values)]

    return filtered_logs

def aggregate_logs(logs, attribute):
    aggregated_logs = {}

    # Aggregate logs based on the specified attribute
    for log in logs:
        if log[attribute] not in aggregated_logs:
            aggregated_logs[log[attribute]] = 0
        aggregated_logs[log[attribute]] += 1

    return aggregated_logs

def calculate_count(logs, attribute):
    count = len(logs)
    return count

def calculate_error_rate(logs):
    total_logs = len(logs)
    error_logs = [log for log in logs if log.get('severity') == 'Error']
    error_count = len(error_logs)
    error_rate = (error_count / total_logs) * 100 if total_logs > 0 else 0
    return f"{error_rate:.2f}%"

if __name__ == '__main__':
    # Specify the path to the log file you want to parse
    log_file_path = r'C:\Users\44788\security-log-analyzer\logs\sample.json'

    # Configure logging
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')

    # Filter out the findfont warning
    warnings.filterwarnings('ignore', category=UserWarning)

    # Call the log parsing function based on the chosen log format
    parsed_logs = []
    parse_json_logs(log_file_path, parsed_logs)

    # Display the parsed log entries
    for log in parsed_logs:
        logging.debug("Parsed log entry:")
        logging.debug(f"  Timestamp       : {log['timestamp']}")
        logging.debug(f"  Source IP       : {log['source_ip']}")
        logging.debug(f"  Destination IP  : {log['destination_ip']}")
        logging.debug(f"  Event Type      : {log['event_type']}")
        logging.debug(f"  Severity        : {log['severity']}")
        logging.debug(f"  Log Message     : {log['log_message']}")
        logging.debug("")  # Empty line for better readability

    # Perform additional analysis or event detection based on the parsed logs
    # Add your own logic here

    # Specify filter criteria
    filters = {
        'severity': ['Error', 'Warning']
    }

    # Specify logical operator
    logical_operator = "OR"

    # Example: Filter logs based on criteria with logical operator
    filtered_logs = filter_logs(parsed_logs, filters, logical_operator)

    # Display the filtered logs
    logging.debug("Filtered logs:")
    for log in filtered_logs:
        logging.debug(f"  Timestamp       : {log['timestamp']}")
        logging.debug(f"  Source IP       : {log['source_ip']}")
        logging.debug(f"  Destination IP  : {log['destination_ip']}")
        logging.debug(f"  Event Type      : {log['event_type']}")
        logging.debug(f"  Severity        : {log['severity']}")
        logging.debug(f"  Log Message     : {log['log_message']}")
        logging.debug("")  # Empty line for better readability

    # Example: Count occurrences of each severity level
    aggregated_logs = aggregate_logs(filtered_logs, 'severity')

    # Display the severity breakdown
    logging.debug("Severity Breakdown:")
    for severity, count in aggregated_logs.items():
        logging.debug(f"Severity: {severity}  Count: {count}")

    # Calculate the total count of logs
    total_count = calculate_count(filtered_logs, 'severity')
    logging.debug(f"Total Count of Logs: {total_count}")

    # Example: Calculate error rate
    error_rate = calculate_error_rate(filtered_logs)
    logging.debug(f"Error Rate: {error_rate}")

# Example: Visualize event types
event_types = [log['event_type'] for log in parsed_logs]
event_counts = {}

# Count occurrences of each event type
for event_type in event_types:
    if event_type in event_counts:
        event_counts[event_type] += 1
    else:
        event_counts[event_type] = 1

# Set the figure size
plt.figure(figsize=(18, 15))

# Validate data before visualization
if len(event_counts) == 0 or all(count == 0 for count in event_counts.values()):
    logging.warning("No valid data for event type visualization.")
else:
    # Create a table for event types
    ax_table = plt.subplot(2, 2, 2)
    table_data = list(event_counts.items())

    # Sort the table data by event count in descending order
    sorted_table_data = sorted(table_data, key=lambda x: x[1], reverse=True)

    table = plt.table(cellText=sorted_table_data, colLabels=['Event Type', 'Event Count'], cellLoc='center', loc='center')
    table.auto_set_font_size(False)  # Disable automatic font size adjustment
    table.set_fontsize(15)
    table.scale(1.5, 1.5)
    plt.title('Event Types')
    ax_table.axis('off')  # Hide the axis

    # Set bold font style for subheading titles
    cell_event_type = table[(0, 0)]
    cell_event_count = table[(0, 1)]
    cell_event_type.get_text().set_fontweight('bold')
    cell_event_count.get_text().set_fontweight('bold')

    # Adjust the table cell heights and column width
    table.auto_set_column_width([0, 1])
    table.scale(1, 1.5)  # Increase the cell height



# Example: Visualize source IP addresses
source_ips = [log['source_ip'] for log in parsed_logs]
unique_source_ips = list(set(source_ips))
source_ip_counts = [source_ips.count(ip) for ip in unique_source_ips]

# Sort the source IP addresses and event counts together based on event counts in descending order
sorted_data = sorted(zip(source_ip_counts, unique_source_ips), reverse=False)

# Unpack the sorted data into separate lists
sorted_source_ip_counts, sorted_unique_source_ips = zip(*sorted_data)

# Validate data before visualization
if len(sorted_unique_source_ips) == 0 or all(count == 0 for count in sorted_source_ip_counts):
    logging.warning("No valid data for source IP addresses visualization.")
else:
    # Create a subplot for source IP addresses
    plt.subplot(2, 2, 1)

    # Generate a list of colors
    num_bars = len(sorted_unique_source_ips)
    colors = plt.cm.Set1(np.linspace(0, 1, num_bars))

    # Plot the horizontal bar chart with different colors
    plt.barh(sorted_unique_source_ips, sorted_source_ip_counts, color=colors)
    plt.xlabel('Event Count')
    plt.ylabel('Source IP Address')
    plt.title('Source IP Addresses')
    plt.tight_layout()

# Example: Visualize destination IP addresses
destination_ips = [log['destination_ip'] for log in parsed_logs]
unique_destination_ips = list(set(destination_ips))
destination_ip_counts = [destination_ips.count(ip) for ip in unique_destination_ips]

# Sort the destination IP addresses and event counts together based on event counts in descending order
sorted_data = sorted(zip(destination_ip_counts, unique_destination_ips), reverse=False)

# Unpack the sorted data into separate lists
sorted_destination_ip_counts, sorted_unique_destination_ips = zip(*sorted_data)

# Validate data before visualization
if len(sorted_unique_destination_ips) == 0 or all(count == 0 for count in sorted_destination_ip_counts):
    logging.warning("No valid data for destination IP addresses visualization.")
else:
    # Create a subplot for destination IP addresses
    plt.subplot(2, 2, 3)  # Adjust subplot position to fit a 2x2 grid

    # Generate a list of colors
    num_bars = len(sorted_unique_destination_ips)
    colors = plt.cm.Set2(np.linspace(0, 1, num_bars))

    # Plot the horizontal bar chart with different colors
    plt.barh(sorted_unique_destination_ips, sorted_destination_ip_counts, color=colors)
    plt.xlabel('Event Count')
    plt.ylabel('Destination IP Address')
    plt.title('Destination IP Addresses')
    plt.subplots_adjust(left=0.08, bottom=0.05)


# Example: Visualize severity levels
severity_levels = set(log['severity'] for log in parsed_logs)
severity_counts = [parsed_logs.count(log) for log in severity_levels]

# Count occurrences of each severity level
severity_counts = {}
for log in parsed_logs:
    severity = log['severity']
    if severity in severity_counts:
        severity_counts[severity] += 1
    else:
        severity_counts[severity] = 1

# Validate data before visualization
if len(severity_counts) == 0 or all(count == 0 for count in severity_counts.values()):
    logging.warning("No valid data for severity levels visualization.")
else:
    # Create a subplot for severity levels
    plt.subplot(2, 2, 4)
    plt.pie(severity_counts.values(), labels=severity_counts.keys(), autopct='%1.1f%%')
    plt.title('Severity Levels')


# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.3, hspace=0.4)

# Save the figure with all the subplots
plt.savefig('log_visualization.png')
