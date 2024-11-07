# Random Number Generator

A modern, user-friendly GUI application built with Python and Tkinter that generates random numbers based on user specifications. The application features a clean, dark-themed interface and allows users to generate, sort, and save random numbers to a file.

## Features

- **Customizable Number Generation**: 
  - Specify the quantity of numbers to generate
  - Set the maximum value for generated numbers
  - Optional sorting capability
- **Modern Dark Theme**: Built with ttkthemes for a sleek, modern appearance
- **File Export**: Automatically saves generated numbers to a text file
- **User-Friendly Interface**: Clean and intuitive design with clear input fields
- **Error Handling**: Robust validation of user inputs

## Prerequisites

Before running this application, ensure you have the following installed:
- Python 3.x
- tkinter (usually comes with Python)
- ttkthemes

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ruturajsolanki/RandomNumGen.git
   cd RandomNumGen
   ```

2. **Install required packages**:
   ```bash
   pip install ttkthemes
   ```

## Usage

1. **Run the application**:
   ```bash
   python RandomGen.py
   ```

2. **Using the Interface**:
   - Enter the desired number of random numbers in "How many numbers?"
   - Specify the maximum possible value in "Maximum number?"
   - (Optional) Check "Sort numbers?" to sort the output
   - Click "Generate Numbers" to create and save the numbers

3. **Output**:
   - Numbers are saved to a text file named `[count].txt`
   - Each number is on a new line
   - The file is created in the same directory as the script

## Code Structure

The application is built using:
- `tkinter`: For the basic GUI framework
- `ttk`: For themed widgets
- `ttkthemes`: For the modern dark theme
- `random`: For number generation

Key components:
```python
def generate_numbers():
    # Main function for number generation and file saving
    # Handles user input validation and file operations
```

## Interface Components

- Title Banner
- Number Count Input Field
- Maximum Number Input Field
- Sort Option Checkbox
- Generate Button
- Result Status Label

## Customization

The interface uses the "equilux" theme from ttkthemes, but you can modify this by changing:
```python
root.set_theme("equilux")  # Change to any available theme
```

Available themes can be viewed using:
```python
root.get_themes()
```

## Error Handling

The application includes error handling for:
- Invalid numeric inputs
- File operation errors
- Value conversion errors

## Future Enhancements

Potential improvements could include:
- Minimum value specification
- Custom file naming
- Multiple output file formats
- Range-based generation
- Duplicate number handling options
- Preview of generated numbers
- Copy to clipboard functionality

## Contributing

Feel free to fork the repository and submit pull requests. You can also:
1. Report bugs
2. Suggest new features
3. Improve documentation

## License

This project is open source and available under the MIT License.

## Author

Ruturaj Solanki

## Contact

- Email: ruturajsolanki43@gmail.com
- GitHub: [@ruturajsolanki](https://github.com/ruturajsolanki)

## Acknowledgments

- ttkthemes for the modern GUI themes
- Python tkinter community for documentation and examples

---

*Note: This is a basic random number generator intended for educational and utility purposes.*
