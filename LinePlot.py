import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
import sys
sys.getdefaultencoding()
sys.stdout.reconfigure(encoding='utf-8')

subscript_1 = "\u2081" 
subscript_2 = "\u2082" 
subscript_3 = "\u2083" 
subscript_4 = "\u2084" 
subscript_5 = "\u2085" 
subscript_6 = "\u2086" 
subscript_7 = "\u2087" 
subscript_8 = "\u2088" 
subscript_9 = "\u2089"  
subscript_0 = "\u2080"  
subscript_10 = "\u2081\u2080" 
subscript_11 = "\u2081\u2081" 
subscript_12 = "\u2081\u2082"  

def plot_linear_equation(a, b, c):
    """
    Plot a linear equation in the form ax + by + c = 0.

    Parameters:
    - a, b: Coefficients of x1 and x2
    - c: Constant term
    """
    # Define the equation in slope-intercept form
    def line_equation(x):
        return (-a/b) * x - (c/b)

    # Generate x values
    x_values = np.linspace(-10, 10, 100)

    # Calculate corresponding y values
    y_values = line_equation(x_values)

    # Plot the line
    plt.plot(x_values, y_values, label=f'{a}x{subscript_1} + {b}x{subscript_2} + {c} = 0')
    
    plt.axhline(0, color='black', linewidth=2, linestyle='--', label='Center Line')
    plt.axvline(0, color='black', linewidth=2, linestyle='--')
    
    # Correctly calculate and plot x2-axis intercept
    a, b, c = 4, 6, 8
    x2_axis_intercept = -c/b
    
    # Convert x2_axis_intercept to Fraction
    x2_axis_intercept_fraction = Fraction(x2_axis_intercept).limit_denominator()

    # Print x2_axis_intercept in rational form
    print(f"x2_axis_intercept in Fraction: {x2_axis_intercept_fraction}")
    print("x2_axis_intercept: ",x2_axis_intercept)
    
    plt.scatter([0], [x2_axis_intercept], color='red', marker='o', label='x2-axis Intercept Point')

    # Add labels and title
    plt.xlabel(f'x{subscript_1}')
    plt.ylabel(f'x{subscript_2}')
    plt.title(f'Line Plot of {a}x{subscript_1} + {b}x{subscript_2} + {c} = 0')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

# Example usage:
plot_linear_equation(4, 6, 8)
