
# Bitwise Visualizer and Calculator

A Tkinter-based GUI application that demonstrates bit manipulation in an interactive way. The application converts integers into binary strings and performs bitwise operations (AND, OR, XOR, NOT, left shift, and right shift), displaying the results in both decimal and binary formats.

## Features

- **Interactive GUI:** User-friendly interface built with Tkinter.
- **Binary Conversion:** Converts integers to an 8-bit (or customizable) binary string.
- **Bitwise Operations:** Perform AND, OR, XOR, NOT, left shift, and right shift.
- **Real-Time Results:** Instantly shows results in both decimal and binary formats.
- **Error Handling:** Alerts for invalid inputs.

## Requirements

- Python 3.x
- Tkinter (usually bundled with Python)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/bitwise-visualizer.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd bitwise-visualizer
   ```

3. **Set Up a Virtual Environment (Recommended):**

   ```bash
   python -m venv venv
   ```

   - **Activate the Virtual Environment:**
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Install Dependencies:**

   If you have a `requirements.txt`, install the packages using:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application with:

```bash
python main.py
```

A window will appear where you can:
- Enter the first integer.
- Enter the second integer (or shift amount).
- Click on the desired bitwise operation button to see the result.

## Project Structure

- `main.py` — Main application file containing the Tkinter GUI and bitwise logic.
- `README.md` — Project documentation.
- `.gitignore` — Specifies files/folders to be excluded from Git.
- `requirements.txt` — Lists any additional packages needed (if applicable).

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests. If you have any issues, please open an issue to discuss.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
