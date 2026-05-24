
"""
Laboratory work No. 4
Task: 4 (Geometric figures)
Variant: 24
Description: Build an isosceles trapezoid by base 'a', side 'b' and angle 'Y' (in degrees)
between the base and the side. Use abstract class, inheritance, super(), properties,
getters/setters, magic methods, mixin, draw the figure with matplotlib, save to file.

Developer: Student
Date: 2026-05-14
Version: 1.0
"""

import math
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from typing import Optional, Tuple



class ShapeColor:
    """Class to store the color of a geometric figure."""

    def __init__(self, color):
        """Initialize color."""
        self._color = color

    @property
    def color(self):
        """Getter for color."""
        return self._color

    @color.setter
    def color(self, value):
        """Setter for color with validation."""
        if isinstance(value, str) and value.strip():
            self._color = value.strip()
        else:
            raise ValueError("Color must be a non-empty string.")

    def __str__(self):
        return self._color


class GeometricShape(ABC):
    """Abstract base class for all geometric figures."""

    _instance_count = 0

    def __init__(self, name):
        """Initialize the shape with a name."""
        self._name = name
        GeometricShape._instance_count += 1

    @abstractmethod
    def area(self):
        """Abstract method to compute the area of the figure."""
        pass

    @classmethod
    def get_instance_count(cls):
        """Return the number of created instances (static method demo)."""
        return cls._instance_count

    @staticmethod
    def is_valid_positive(value, param_name):
        """Static helper to validate positive numbers."""
        if value <= 0:
            raise ValueError(f"{param_name} must be positive.")
        return value

class IsoscelesTrapezoid(GeometricShape):
    """
    Class representing an isosceles trapezoid.
    Parameters: base a, side b, angle Y (degrees) between base a and side b.
    """

    def __init__(self, a, b, angle_deg, color):
        """
        Constructor: creates a trapezoid and a ShapeColor object.
        Uses super() to call parent constructor.
        """
        super().__init__("Isosceles Trapezoid")

        self._a = GeometricShape.is_valid_positive(a, "Base 'a'")
        self._b = GeometricShape.is_valid_positive(b, "Side 'b'")
        self._angle_deg = angle_deg
        if not (0 < angle_deg < 180):
            raise ValueError("Angle must be between 0 and 180 degrees.")

        self._color_obj = ShapeColor(color)

        angle_rad = math.radians(self._angle_deg)
        self._height = self._b * math.sin(angle_rad)
        self._projection = self._b * math.cos(angle_rad)  

        self._c = self._a - 2 * self._projection
        if self._c <= 0:
            raise ValueError(
                f"Invalid dimensions: upper base (c = {self._c}) <= 0. "
                f"Angle too large or side too long."
            )

    @property
    def a(self):
        """Getter for lower base."""
        return self._a

    @a.setter
    def a(self, value):
        """Setter for lower base with recomputation."""
        value = GeometricShape.is_valid_positive(value, "Base 'a'")
        self._a = value
        #Recompute upper base
        self._c = self._a - 2 * self._projection
        if self._c <= 0:
            raise ValueError("After changing base, the trapezoid becomes invalid.")

    @property
    def b(self):
        """Getter for side."""
        return self._b

    @b.setter
    def b(self, value):
        """Setter for side with recomputation."""
        value = GeometricShape.is_valid_positive(value, "Side 'b'")
        self._b = value
        angle_rad = math.radians(self._angle_deg)
        self._height = self._b * math.sin(angle_rad)
        self._projection = self._b * math.cos(angle_rad)
        self._c = self._a - 2 * self._projection
        if self._c <= 0:
            raise ValueError("After changing side, the trapezoid becomes invalid.")

    @property
    def angle_deg(self):
        """Getter for angle in degrees."""
        return self._angle_deg

    @angle_deg.setter
    def angle_deg(self, value):
        """Setter for angle with recomputation."""
        if not (0 < value < 180):
            raise ValueError("Angle must be between 0 and 180.")
        self._angle_deg = value
        angle_rad = math.radians(self._angle_deg)
        self._height = self._b * math.sin(angle_rad)
        self._projection = self._b * math.cos(angle_rad)
        self._c = self._a - 2 * self._projection
        if self._c <= 0:
            raise ValueError("After changing angle, the trapezoid becomes invalid.")

    @property
    def color(self):
        """Property that returns the color (delegates to ShapeColor)."""
        return self._color_obj.color

    @color.setter
    def color(self, new_color):
        """Set a new color for the shape."""
        self._color_obj.color = new_color

    @classmethod
    def get_shape_name(cls):
        """Return the name of the shape (class method)."""
        return "Isosceles Trapezoid"

    def area(self):
        """Compute and return the area of the trapezoid."""
        return (self._a + self._c) / 2 * self._height

    def __str__(self) -> str:
        """Return formatted string with parameters, color and area."""
        return (
            f"Shape: {self.get_shape_name()}\n"
            f"Lower base (a): {self._a:.2f}\n"
            f"Upper base (c): {self._c:.2f}\n"
            f"Side (b): {self._b:.2f}\n"
            f"Angle (Y): {self._angle_deg:.2f}°\n"
            f"Height: {self._height:.2f}\n"
            f"Color: {self.color}\n"
            f"Area: {self.area():.2f}"
        )

    def get_info_string(self):
        """Return a short string using .format() as required."""
        info = (
            "Figure: {name} | a={a:.2f} | b={b:.2f} | angle={ang:.2f}° | "
            "color={col} | area={area:.2f}"
        )
        return info.format(
            name=self.get_shape_name(),
            a=self._a,
            b=self._b,
            ang=self._angle_deg,
            col=self.color,
            area=self.area()
        )

    #draw the trapezoid using matplotlib
    def draw(self, text_label = ""):
        """
        Build and fill the trapezoid with the chosen color.
        Add a text label (subtitle). Display the figure on screen.
        """
        x_left_bottom = 0.0
        y_left_bottom = 0.0
        x_right_bottom = self._a
        y_right_bottom = 0.0

        x_left_top = self._projection
        y_left_top = self._height
        x_right_top = self._a - self._projection
        y_right_top = self._height

        vertices_x = [x_left_bottom, x_right_bottom, x_right_top, x_left_top]
        vertices_y = [y_left_bottom, y_right_bottom, y_right_top, y_left_top]

        plt.figure(figsize=(6, 5))
        polygon = plt.Polygon(
            list(zip(vertices_x, vertices_y)), #coordinati
            closed=True, #zamknut
            color=self.color,
            alpha=0.6,
            edgecolor="black",
            linewidth=2
        )
        plt.gca().add_patch(polygon) #otrisovat osi i na nih poligon

        #Set limits and aspect
        margin = max(self._a, self._height) * 0.2 
        plt.xlim(-margin, self._a + margin)
        plt.ylim(-margin, self._height + margin)
        plt.gca().set_aspect('equal') #dlya rovnosty coordinat
        plt.grid(True, linestyle='--', alpha=0.5) 
        plt.title(f"{self.get_shape_name()}\n{text_label}", fontsize=12)

        plt.xlabel("X coordinate")
        plt.ylabel("Y coordinate")
        plt.savefig("MyPlot.png", dpi=300)
        plt.show()

    # Additional method to get vertices for file export
    def get_vertices(self):
        """Return x and y lists of vertices."""
        x_left_bottom = 0.0
        x_right_bottom = self._a
        x_left_top = self._projection
        x_right_top = self._a - self._projection
        y_bottom = 0.0
        y_top = self._height
        vertices_x = [x_left_bottom, x_right_bottom, x_right_top, x_left_top]
        vertices_y = [y_bottom, y_bottom, y_top, y_top]
        return vertices_x, vertices_y


#helper function
def input_positive_float(prompt):
    """Read a positive float from user with error handling."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: value must be positive. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def input_angle(prompt):
    """Read an angle in degrees (0..180 exclusive) with validation."""
    while True:
        try:
            angle = float(input(prompt))
            if angle <= 0 or angle >= 180:
                print("Angle must be between 0 and 180 degrees (exclusive).")
                continue
            return angle
        except ValueError:
            print("Invalid input. Please enter a number.")


def input_color(prompt):
    """Read a color string (matplotlib recognized name or hex)."""
    while True:
        color = input(prompt).strip()
        if color:
            return color
        print("Color cannot be empty.")


def task4_run():
    """Main program loop."""

    while True:
        try:
            print("\nEnter trapezoid parameters ")
            a = input_positive_float("Lower base (a) > 0: ")
            b = input_positive_float("Side (b) > 0: ")
            angle = input_angle("Angle between base and side (0<Y<180): ")
            color = input_color("Fill color (e.g., 'blue', 'red', '#00FF00'): ")
            label = input("Text label to display on the figure: ").strip()

            # Create trapezoid object
            trap = IsoscelesTrapezoid(a, b, angle, color)

            # Display information
            print("\n" + "=" * 40)
            print(trap)                     # uses __str__
            print("Short info: " + trap.get_info_string())
            print("=" * 40)

            # Draw the figure
            trap.draw(text_label=label if label else "Trapezoid")

            # Repeat?
            again = input("\nCreate another trapezoid? (y/n): ").strip().lower()
            if again != 'y':
                print("Exiting program.")
                break

        except ValueError as ve:
            print(f"Value error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")


