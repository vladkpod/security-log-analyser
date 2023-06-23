# Security Log Analyzer

This project is a security log analyzer that parses and analyzes log files in JSON format. It provides functions to filter logs, aggregate logs based on specified attributes, calculate counts and error rates, and visualize log data.

## Setup Guide

To use this security log analyzer, follow the steps below:

### Prerequisites

Make sure you have the following installed:

- Python (version 3.6 or higher)
- Matplotlib library

### Installation

1. Clone the repository or download the source code.

```bash
git clone https://github.com/your-username/security-log-analyzer.git
```

2. Change to the project directory.

```bash
cd security-log-analyzer
```

3. Install the required dependencies.

```bash
pip install matplotlib
```

### Usage

1. Import the necessary modules in your Python code.

```python
import logging
import json
import warnings
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Add this line before importing pyplot
import matplotlib.pyplot as plt
import numpy as np
```

2. Copy the code from the provided code file and paste it into your Python file.

3. Modify the code as needed for your specific use case. You can add your own logic for additional analysis or event detection based on the parsed logs.

4. Specify the path to the log file you want to parse.

```python
log_file_path = r'/path/to/your/log/file.json'
```

5. Configure the logging level and format.

```python
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
```

6. Run the code.

```bash
python your_script.py
```

7. The script will parse the log file, display the parsed log entries, perform additional analysis or event detection based on the logs, filter logs based on criteria, display filtered logs, calculate counts and error rates, and generate visualizations.

8. The visualization output will be saved as "log_visualization.png" in the current directory.

Note: Make sure to replace `/path/to/your/log/file.json` with the actual path to your log file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.