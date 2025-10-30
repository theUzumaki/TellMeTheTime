# Logger Module Documentation

## Overview
The `logger.py` module provides a flexible and colorized logging system for Python applications. It offers structured logging with support for indentation, spacing, colors, and semantic message types.

## Features
- **Flexible formatting**: Control indentation, newlines before/after, and colors
- **Semantic functions**: Pre-configured functions for errors, warnings, success, info, and debug messages
- **Color support**: Full ANSI color support including text colors, bright colors, background colors, and styles
- **Pipeline logging**: Special functions for structured logging in multi-step processes
- **File operation logging**: Dedicated functions for logging file saves and detection results

## Basic Usage

### Simple Logging
```python
from logger import log, Colors

# Plain message
log(0, 0, 0, None, "Hello, World!")

# Colored message
log(0, 0, 0, Colors.GREEN, "Success message in green")

# Indented message
log(1, 0, 0, Colors.CYAN, "This is indented 1 tab")
log(2, 0, 0, Colors.YELLOW, "This is indented 2 tabs")

# Message with spacing
log(0, 2, 1, Colors.RED, "2 newlines before, 1 after")

# Combined styles
log(0, 0, 0, Colors.BOLD + Colors.BLUE, "Bold blue text")
```

## Semantic Logging Functions

### Error Messages
```python
from logger import log_error

log_error("File not found")
log_error("Connection timeout", indentation_tabs=1)
log_error("Critical failure", newline_before=1, newline_after=1)
```

### Warning Messages
```python
from logger import log_warning

log_warning("Deprecated function used")
log_warning("Low memory available", indentation_tabs=1)
```

### Success Messages
```python
from logger import log_success

log_success("Operation completed successfully")
log_success("Data processed", indentation_tabs=1)
```

### Info Messages
```python
from logger import log_info

log_info("Starting process...")
log_info("Loading configuration", indentation_tabs=1)
```

### Debug Messages
```python
from logger import log_debug

log_debug("Variable x = 42")
log_debug("Function called with args: foo, bar", indentation_tabs=1)
```

## Structured Logging

### Section Headers
```python
from logger import log_section_header, log_subsection

log_section_header("MAIN PROCESSING PIPELINE")
log_subsection("Data Loading Phase")
```

### Step-by-step Logging
```python
from logger import log_step

log_step(1, 5, "Preprocessing data")
log_step(2, 5, "Feature extraction")
log_step(3, 5, "Model training")
```

### File Operations
```python
from logger import log_file_saved

log_file_saved("output/results.png")
log_file_saved("models/trained_model.pkl", indentation_tabs=1)
```

### Detection Results
```python
from logger import log_detection_result

log_detection_result("Accuracy", "95.3%")
log_detection_result("Clock center", "(320, 240)")
```

## Color Reference

### Text Colors
- `Colors.BLACK`, `Colors.RED`, `Colors.GREEN`, `Colors.YELLOW`
- `Colors.BLUE`, `Colors.MAGENTA`, `Colors.CYAN`, `Colors.WHITE`

### Bright Text Colors
- `Colors.BRIGHT_RED`, `Colors.BRIGHT_GREEN`, `Colors.BRIGHT_YELLOW`
- `Colors.BRIGHT_BLUE`, `Colors.BRIGHT_MAGENTA`, `Colors.BRIGHT_CYAN`

### Background Colors
- `Colors.BG_BLACK`, `Colors.BG_RED`, `Colors.BG_GREEN`, `Colors.BG_YELLOW`
- `Colors.BG_BLUE`, `Colors.BG_MAGENTA`, `Colors.BG_CYAN`, `Colors.BG_WHITE`

### Text Styles
- `Colors.BOLD` - Bold text
- `Colors.DIM` - Dimmed text
- `Colors.ITALIC` - Italic text
- `Colors.UNDERLINE` - Underlined text
- `Colors.REVERSE` - Inverted colors

### Semantic Colors
- `Colors.ERROR` - Red (for errors)
- `Colors.WARNING` - Yellow (for warnings)
- `Colors.SUCCESS` - Green (for success)
- `Colors.INFO` - Cyan (for information)
- `Colors.DEBUG` - Magenta (for debug)
- `Colors.HEADER` - Bright cyan (for headers)

## Complete Pipeline Example

```python
from logger import (
    log, log_section_header, log_step, log_error, log_success,
    log_file_saved, log_detection_result, Colors
)

# Application header
log(0, 1, 0, Colors.BRIGHT_MAGENTA + Colors.BOLD, "╔═════════════════════╗")
log(0, 0, 0, Colors.BRIGHT_MAGENTA + Colors.BOLD, "║  MY APPLICATION     ║")
log(0, 0, 1, Colors.BRIGHT_MAGENTA + Colors.BOLD, "╚═════════════════════╝")

# Main pipeline
log_section_header("PROCESSING PIPELINE")

log_step(1, 3, "Data Loading")
log_file_saved("data/input.csv", indentation_tabs=1)

log_step(2, 3, "Processing")
log_detection_result("Items processed", "1000", indentation_tabs=1)

log_step(3, 3, "Saving Results")
log_file_saved("output/results.json", indentation_tabs=1)

# Final result
log(0, 1, 0, Colors.SUCCESS + Colors.BOLD, "=" * 60)
log_success("Pipeline completed successfully!", newline_after=1)
log(0, 0, 1, Colors.SUCCESS + Colors.BOLD, "=" * 60)
```

## Function Reference

### `log(indentation_tabs, newline_before, newline_after, color, content)`
The core logging function.

**Parameters:**
- `indentation_tabs` (int): Number of tabs to indent (default: 0)
- `newline_before` (int): Number of newlines before content (default: 0)
- `newline_after` (int): Number of newlines after content (default: 0)
- `color` (str): ANSI color code from Colors class (default: None)
- `content` (str): Message content to log

**Returns:** None

### Semantic Functions
All semantic functions accept:
- `message` (str): The message to log
- `indentation_tabs` (int): Indentation level (default: 0)
- `newline_before` (int): Newlines before (default: 0)
- `newline_after` (int): Newlines after (default: 0)

Functions:
- `log_error(message, ...)` - Log error with ✗ symbol
- `log_warning(message, ...)` - Log warning with ⚠ symbol
- `log_success(message, ...)` - Log success with ✓ symbol
- `log_info(message, ...)` - Log info with ℹ symbol
- `log_debug(message, ...)` - Log debug with 🔍 symbol

### Structural Functions
- `log_section_header(title, indentation_tabs=0)` - Log major section header
- `log_subsection(title, indentation_tabs=0)` - Log subsection header
- `log_step(step_number, total_steps, description, indentation_tabs=0)` - Log processing step
- `log_file_saved(filepath, indentation_tabs=1)` - Log file save with 💾 symbol
- `log_detection_result(label, value, indentation_tabs=1)` - Log detection result with 🎯 symbol

## Demo
Run the demo script to see all features in action:
```bash
python logger_demo.py
```

## Integration Example
The logger has been integrated into `main.py` to replace all print statements with structured, colorized logging. This provides:
- Clear visual separation between pipeline stages
- Consistent error and success message formatting
- Easy identification of file operations and detection results
- Professional, readable output

## Notes
- Colors use ANSI escape codes and work in most modern terminals
- Some terminals may not support all styles (italic, dim, etc.)
- Colors are automatically reset after each message to prevent bleeding
- Combine multiple color codes with `+` for compound styles
