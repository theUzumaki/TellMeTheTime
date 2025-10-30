"""
Logger module for structured and colorized console output.
Provides a flexible logging function with indentation, spacing, and color support.
"""


class Colors:
    """ANSI color codes for terminal output."""
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright text colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # Reset
    RESET = '\033[0m'
    
    # Semantic colors for common use cases
    ERROR = RED
    WARNING = YELLOW
    SUCCESS = GREEN
    INFO = CYAN
    DEBUG = MAGENTA
    HEADER = BRIGHT_CYAN
    EMPHASIS = BRIGHT_YELLOW

def log(indentation_tabs=0, newline_before=0, newline_after=0, color=None, content=""):
    """
    Log a message with structured formatting, indentation, spacing, and color.
    
    Args:
        indentation_tabs (int): Number of tabs to indent the content (default: 0)
        newline_before (int): Number of newlines to print before the content (default: 0)
        newline_after (int): Number of newlines to print after the content (default: 0)
        color (str): ANSI color code from Colors class (default: None for no color)
        content (str): The message content to log
    
    Usage Examples:
        log(0, 0, 0, Colors.INFO, "Starting process...")
        log(1, 0, 1, Colors.SUCCESS, "✓ Task completed")
        log(2, 1, 0, Colors.ERROR, "✗ Error occurred")
        log(0, 0, 0, Colors.HEADER + Colors.BOLD, "=== SECTION HEADER ===")
    """
    # Print newlines before content
    if newline_before > 0:
        print('\n' * (newline_before - 1), end='')
    
    # Build indentation
    indentation = '\t' * indentation_tabs
    
    # Build the message with color if specified
    if color:
        message = f"{indentation}{color}{content}{Colors.RESET}"
    else:
        message = f"{indentation}{content}"
    
    # Print the message
    print(message, end='')
    
    # Print newlines after content
    if newline_after > 0:
        print('\n' * newline_after, end='')
    else:
        print()  # Default newline

def log_newline(count=1):
    """
    Log specified number of newlines.
    
    Args:
        count (int): Number of newlines to print (default: 1)
    """
    print('\n' * (count - 1), end='')
    print()  # Ensure at least one newline

def log_application_title(title, width=60):
    """
    Log a stylized application title with decorative borders.
    
    Args:
        title (str): Application title text
        width (int): Width of the title box (default: 60)
    
    Usage:
        log_application_title("CLOCK TIME DETECTION APPLICATION")
    """
    # Calculate padding to center the title
    title_length = len(title)
    if title_length + 2 > width - 2:  # Ensure title fits with at least 1 space on each side
        width = title_length + 4
    
    padding = (width - 2 - title_length) // 2
    padded_title = " " * padding + title + " " * (width - 2 - title_length - padding)
    
    top_border = "╔" + "═" * (width - 2) + "╗"
    middle_line = "║" + padded_title + "║"
    bottom_border = "╚" + "═" * (width - 2) + "╝"
    
    log_newline(2)
    log(0, 1, 0, Colors.BRIGHT_MAGENTA + Colors.BOLD, top_border)
    log(0, 0, 0, Colors.BRIGHT_MAGENTA + Colors.BOLD, middle_line)
    log(0, 0, 1, Colors.BRIGHT_MAGENTA + Colors.BOLD, bottom_border)
    log_newline(2)

def log_section_header(title, indentation_tabs=0):
    """
    Log a section header with consistent formatting.
    
    Args:
        title (str): Section title
        indentation_tabs (int): Indentation level
    """
    separator = "=" * 60
    log(indentation_tabs, 1, 0, Colors.HEADER + Colors.BOLD, separator)
    log(indentation_tabs, 0, 0, Colors.HEADER + Colors.BOLD, title)
    log(indentation_tabs, 0, 1, Colors.HEADER + Colors.BOLD, separator)
    log_newline()


def log_subsection(title, indentation_tabs=0):
    """
    Log a subsection header with consistent formatting.
    
    Args:
        title (str): Subsection title
        indentation_tabs (int): Indentation level
    """
    separator = "-" * 40
    log(indentation_tabs, 1, 0, Colors.BRIGHT_CYAN, separator)
    log(indentation_tabs, 0, 0, Colors.BRIGHT_CYAN, title)
    log(indentation_tabs, 0, 0, Colors.BRIGHT_CYAN, separator)
    log_newline()


def log_error(message, indentation_tabs=0, newline_before=0, newline_after=0):
    """
    Log an error message with consistent formatting.
    
    Args:
        message (str): Error message
        indentation_tabs (int): Indentation level
        newline_before (int): Newlines before
        newline_after (int): Newlines after
    """
    log(indentation_tabs, newline_before, newline_after, 
        Colors.ERROR + Colors.BOLD, f"✗ ERROR: {message}")


def log_warning(message, indentation_tabs=0, newline_before=0, newline_after=0):
    """
    Log a warning message with consistent formatting.
    
    Args:
        message (str): Warning message
        indentation_tabs (int): Indentation level
        newline_before (int): Newlines before
        newline_after (int): Newlines after
    """
    log(indentation_tabs, newline_before, newline_after, 
        Colors.WARNING + Colors.BOLD, f"⚠ WARNING: {message}")


def log_success(message, indentation_tabs=0, newline_before=0, newline_after=0):
    """
    Log a success message with consistent formatting.
    
    Args:
        message (str): Success message
        indentation_tabs (int): Indentation level
        newline_before (int): Newlines before
        newline_after (int): Newlines after
    """
    log(indentation_tabs, newline_before, newline_after, 
        Colors.SUCCESS + Colors.BOLD, f"✓ {message}")


def log_info(message, indentation_tabs=0, newline_before=0, newline_after=0):
    """
    Log an info message with consistent formatting.
    
    Args:
        message (str): Info message
        indentation_tabs (int): Indentation level
        newline_before (int): Newlines before
        newline_after (int): Newlines after
    """
    log(indentation_tabs, newline_before, newline_after, 
        Colors.INFO, f"ℹ {message}")


def log_debug(message, indentation_tabs=0, newline_before=0, newline_after=0):
    """
    Log a debug message with consistent formatting.
    
    Args:
        message (str): Debug message
        indentation_tabs (int): Indentation level
        newline_before (int): Newlines before
        newline_after (int): Newlines after
    """
    log(indentation_tabs, newline_before, newline_after, 
        Colors.DEBUG + Colors.DIM, f"🔍 DEBUG: {message}")


def log_step(step_number, total_steps, description, indentation_tabs=0):
    """
    Log a step in a process with consistent formatting.
    
    Args:
        step_number (int): Current step number
        total_steps (int): Total number of steps
        description (str): Step description
        indentation_tabs (int): Indentation level
    """
    log_newline()
    log(indentation_tabs, 1, 0, Colors.BRIGHT_BLUE + Colors.BOLD, 
        f"[Step {step_number}/{total_steps}] {description}")
    log_newline()


def log_file_saved(filepath, indentation_tabs=1):
    """
    Log a file save operation with consistent formatting.
    
    Args:
        filepath (str): Path to saved file
        indentation_tabs (int): Indentation level
    """
    log(indentation_tabs, 0, 0, Colors.SUCCESS, 
        f"💾 Saved: {filepath}")


def log_detection_result(label, value, indentation_tabs=1):
    """
    Log a detection result with consistent formatting.
    
    Args:
        label (str): Label for the detected value
        value: Detected value
        indentation_tabs (int): Indentation level
    """
    log(indentation_tabs, 0, 0, Colors.BRIGHT_GREEN, 
        f"🎯 {label}: {value}")


def log_final_result(success, message, width=60):
    """
    Log a final result with decorative formatting.
    
    Args:
        success (bool): Whether the operation was successful
        message (str): Result message to display
        width (int): Width of the result box (default: 60)
    
    Usage:
        log_final_result(True, "DETECTED TIME: 03:30")
        log_final_result(False, "Failed to detect time from the clock image")
    """
    color = Colors.SUCCESS + Colors.BOLD if success else Colors.ERROR + Colors.BOLD
    separator = "=" * width
    
    log_newline(2)
    log(0, 1, 0, color, separator)
    if success:
        log_success(message, newline_after=1)
    else:
        log_error(message, newline_after=1)
    log(0, 0, 1, color, separator)
    log_newline(2)
