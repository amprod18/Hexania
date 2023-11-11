import numpy as np

shapez_list = ["Circle", "Diamond", "Rectangle", "Regular Polygon", "Rhomboid", "Square", "Triangle"]

class Circle:
    def __init__(self, surface=None, perimeter=None, radius=None, diameter=None, angle=None, length=None, sector=None,
                 n=4):
        self.surface = surface
        self.perimeter = perimeter
        self.angle = angle
        self.n = n
        self.length = length
        self.sector = sector
        self.radius = radius
        self.diameter = diameter
        self.name = "Circle"

    def get_radius(self):
        if self.radius is not None:
            return (self.radius, "{}")
        elif self.perimeter is not None:
            value = float(self.perimeter)/(2*np.pi)
            latex = "r = \\frac {P} {2\\pi}"
            self.radius = value
            return (value, latex)
        elif self.surface is not None:
            value = (float(self.surface)/np.pi)**(1/2)
            latex = "r = \\sqrt{\\frac {S} {\\pi}}"
            self.radius = value
            return (value, latex)
        elif self.diameter is not None:
            value = float(self.diameter)/2
            latex = "r = \\frac {D} {2}"
            self.radius = value
            return (value, latex)
        elif self.angle is not None and self.sector is not None:
            value = ((float(self.sector)*360)/(float(self.angle)*np.pi))**(1/2)
            latex = "r = \\sqrt{\\frac {\\sigma·360} {'\\alpha\\pi}}"
            self.radius = value
            return (value, latex)
        elif self.angle is not None and self.length is not None:
            value = (float(self.length)*360)/(float(self.angle)*np.pi*2)
            latex = "r = \\frac {P·360} {'2\\alpha\\pi}"
            self.radius = value
            return (value, latex)
        elif self.length is not None and self.sector is not None:
            value = 2*float(self.sector)/float(self.length)
            latex = "r = \\frac {2\\sigma} {l}"
            self.radius = value
            return (value, latex)
        else:
            return ("Not enough information about the polygon!", "{}")

    def get_diameter(self):
        if self.diameter is not None:
            return (self.diameter, "{}")
        else:
            try:
                if type(self.get_radius()[0]) == type(0.1):
                    radius, latex1 = self.get_radius()
                    value = 2*float(radius)
                    latex = latex1 + " \\to d = 2r"
                    self.diameter = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_perimeter(self):
        if self.perimeter is not None:
            return (self.perimeter, "{}")
        else:
            try:
                if type(self.get_radius()[0]) == type(0.1):
                    radius, latex1 = self.get_radius()
                    value = 2*float(radius)*np.pi
                    latex = latex1 + " \\to P = 2\\pi r"
                    self.perimeter = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_surface(self):
        if self.surface is not None:
            return (self.surface, "{}")
        else:
            try:
                if type(self.get_radius()[0]) == type(0.1):
                    radius, latex1 = self.get_radius()
                    value = np.pi*(float(radius))**2
                    latex = latex1 + " \\to S = \\pi r^{2}"
                    self.surface = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_length(self):
        if self.length is not None:
            return (self.length, "{}")
        else:
            try:
                if type(0.1) == type(self.get_radius()[0]):
                    angle, angle_l = self.get_angle()
                    radius, latex1 = self.get_radius()
                    value = 2*np.pi*float(radius)*angle/360
                    if angle_l is not None:
                        latex = angle_l + " \\to " + latex1 + " \\to l = \\frac {2\\pi r\\alpha} {360}"
                    else:
                        latex = "l = \\frac {2\\pi r\\alpha} {360}"
                        self.length = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_sector(self):
        if self.sector is not None:
            return (self.sector, "{}")
        else:
            try:
                if type(self.get_radius()[0]) == type(0.1):
                    angle, angle_l = self.get_angle()
                    radius, latex1 = self.get_radius()
                    value = float(angle)*np.pi*((float(radius))**2)/360
                    latex = angle_l + " \\to " + latex1 + " \\to s = \\frac{\\alpha \\pi r^{2}} {360}"
                    self.sector = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_angle(self):
        if self.angle is not None:
            return (self.angle, "{}")
        else:
            try:
                radius, latex1 = self.get_radius()
                if self.sector is not None:
                    value = float(self.sector)*360/(np.pi*radius**2)
                    latex = "\\alpha = \\frac {360s} {\\pi r^{2}}"
                    self.angle = value
                    return (value, latex)
                elif self.length is not None:
                    value = float(self.length)*360/(np.pi*radius*2)
                    latex = "\\alpha = \\frac {360l} {2 \\pi r}"
                    self.angle = value
                    return (value, latex)
                else:
                    self.angle = 360.0
                    return (360.0, "{}") 
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_parameters(self):
        circle_value = []
        circle_latex = []
        try:
            circle_info = [self.get_radius(), self.get_diameter(), self.get_perimeter(), self.get_surface(), self.get_angle(), self.get_length(), self.get_sector()]
            circle_info = [(float(i[0]), i[1]) for i in circle_info]
            for i in circle_info:    
                if type(i[0]) == type(0.1):
                    circle_value.append(round(i[0], self.n))
                    circle_latex.append(i[1])
                    continue
                else:
                    return ("Not enough information about the polygon!", "{}")
            return (circle_value, circle_latex)
        except TypeError:
            return ("Not enough information about the polygon!", "{}")

class Diamond:
    def __init__(self, side=None, surface=None, perimeter=None, diagonal1=None, diagonal2=None, n=4):
        self.side = side
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.perimeter = perimeter
        self.surface = surface
        self.n = n
        self.name = "Diamond"

    def get_side(self):
        if self.side is not None:
            return (self.side, "{}")
        elif self.diagonal1 is not None and self.diagonal2 is not None:
            value = float(np.sqrt((float(self.diagonal1)**2 + float(self.diagonal2)**2)/4))
            latex = "a = \\sqrt{\\frac {{D_{1}}^{2} + {D_{2}}^{2}} {4}}"
            self.side = value
            return (value, latex)
        elif self.perimeter is not None:
            value = float(self.perimeter)/4
            latex = "a = \\frac {P} {4}"
            self.side = value
            return (value, latex)
        elif self.surface is not None and (self.diagonal1 is not None or self.diagonal2 is not None):
            try:
                value = float(np.sqrt(((float(self.diagonal1)**2 + (2*float(self.surface)/float(self.diagonal1))**2))/4)) # type: ignore
                latex = "a = \\sqrt{\\frac {{D_{1}}^{2} + {\\frac {2S} {D_{1}}}^{2}} {4}}"
                self.side = value
                return (value, latex)
            except TypeError:
                value = float(np.sqrt(((float(self.diagonal2)**2 + (2*float(self.surface)/float(self.diagonal2))**2))/4)) # type: ignore
                latex = "a = \\sqrt{\\frac {{D_{2}}^{2} + {\\frac {2S} {D_{2}}}^{2}} {4}}"
                self.side = value
                return (value, latex)
        else:
            return ("Not enough information about the polygon!", "{}")

    def get_diagonal1(self):
        if self.diagonal1 is not None:
            return (self.diagonal1, "{}")
        elif self.side is not None and self.diagonal2 is not None:
            value = float(np.sqrt(float(self.side)**2 - (float(self.diagonal2)**2)/4))
            latex = "D_{1} = \\sqrt{a^{2} - \\frac {{D_{2}}^{2}} {4}}"
            self.diagonal1 = value
            return (value, latex)
        elif self.perimeter is not None and self.diagonal2 is not None:
            value = float(np.sqrt((float(self.perimeter)/4)**2 - (float(self.diagonal2)**2)/4))
            latex = "D_{1} = \\sqrt {{\\frac {P} {4}}^{2} + \\frac {{D_{2}}^{2}} {4}}"
            self.diagonal1 = value
            return (value, latex)
        elif self.surface is not None and self.diagonal2 is not None:
            value = 2*float(self.surface)/float(self.diagonal2)
            latex = "D_{1} = \\frac {2S} {D_{1}}"
            self.diagonal1 = value
            return (value, latex)
        elif ((self.perimeter is not None) or (self.side is not None)) and self.surface is not None:
            side, latex1 = self.get_side()
            s = float(self.surface)

            b1 = float(np.sqrt(2 * (side**2 + np.sqrt(side ** 4 - s ** 2))))
            b2 = float(np.sqrt(2 * (side**2 - np.sqrt(side ** 4 - s ** 2))))

            if (b1 > 0) and (self.diagonal2 is None):
                value = b1
                latex = latex1 + " \\to D = \\sqrt {2({c}^{2} + \\sqrt {{c}^{4} - {s}^{2}})}"
                self.diagonal1 = value
                return (value, latex)
            elif b2 > 0:
                value = b2
                latex = latex1 + " \\to D = \\sqrt {2({c}^{2} - \\sqrt {{c}^{4} - {s}^{2}})}"
                self.diagonal1 = value
                return (value, latex)
            return ("Impossible polygon!", "{}")
        else:
            return ("Not enough information about the polygon!", "{}")
        
    def get_diagonal2(self):
        if self.diagonal2 is not None:
            return (self.diagonal2, "{}")
        else:
            try:
                side, latex1 = self.get_side()
                diagonal1, latex2 = self.get_diagonal1()
                if (type(side) == type(0.1)) and (type(diagonal1) == type(0.1)):
                    value = float(np.sqrt(4 * float(side)**2 - (float(diagonal1)**2)))
                    latex = latex1 + " \\to " + latex2 + " \\to D_{2} = \\sqrt {4{a}^{2} - {D_{2}}^{2}}"
                    self.diagonal2 = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")
    

    def get_surface(self):
        if self.surface is not None:
            return (self.surface, "{}")
        else:
            try:
                side, latex1 = self.get_side()
                diagonal1, latex2 = self.get_diagonal1()
                if (type(side) == type(0.1)) and (type(diagonal1) == type(0.1)):
                    value = float(np.sqrt(float(side)**2 - (float(diagonal1)**2)/4)*(float(diagonal1)/2))
                    latex = latex1 + " \\to " + latex2 + " \\to S = \\frac {D_{1}(\\sqrt {a^{2} - \\frac {{D_{1}}^{2})} {4}}} {2}"
                    self.surface = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")
        
    def get_perimeter(self):
        if self.perimeter is not None:
            return (self.perimeter, "{}")
        else:
            try:
                side, latex1 = self.get_side()
                value = side*4 
                latex = latex1 + " \\to P = 4c"
                self.perimeter = value
                return (value, latex)
            except TypeError:
                return ("Not enough information about the  polygon!", "{}")

    def get_parameters(self):
        diamond_value = []
        diamond_latex = []
        try:
            diamond_info = [self.get_side(),  self.get_diagonal1(), self.get_diagonal2(), self.get_perimeter(), self.get_surface()]
            diamond_info = [(float(i[0]), i[1]) for i in diamond_info]
            for i in diamond_info:    
                if type(i[0]) == type(0.1):
                    diamond_value.append(round(i[0], self.n))
                    diamond_latex.append(i[1])
                    continue
                else:
                    return ("Not enough information about the polygon!", "{}")    
            return (diamond_value, diamond_latex)
        except TypeError:
            return ("Not enough information about the polygon!", "{}")

class Rectangle:
    def __init__(self, length=None, height=None, surface=None, perimeter=None, diagonal=None, n=4):
        self.length = length
        self.height = height
        self.surface = surface
        self.perimeter = perimeter
        self.diagonal = diagonal
        self.n = n
        self.name = "Rectangle"

    def get_length(self):
        if self.length is not None:
            return (self.length, "{}")
        elif self.perimeter is not None and self.height is not None:
            value = (float(self.perimeter) - 2*float(self.height))/2
            latex = "l = \\frac {P-2h} {2}"
            self.length = value
            return (value, latex)
        elif self.diagonal is not None and self.height is not None:
            value = np.sqrt(float(self.diagonal)**2 - float(self.height)**2)
            latex = "l = \\sqrt {D^{2} - h^{2}}"
            self.length = value
            return (value, latex)
        elif self.surface is not None and self.height is not None:
            value = float(self.surface) / float(self.height)
            latex = "l = \\frac {S} {h}"
            self.length = value
            return (value, latex)
        elif self.perimeter is not None and self.diagonal is not None:
            p = float(self.perimeter)
            d = float(self.diagonal)
            b1 = (p + np.sqrt(p**2 / 2 + 2*d**2))/2
            b2 = (p - np.sqrt(p**2 / 2 + 2*d**2))/2
            if self.height is None:
                value = b1
                latex = "l = \\frac {P + \\sqrt {\\frac {P^{2}} {2} + 2{D}^{2}} {2}"
                self.length = value
                return (value, latex)
            else:
                if not np.isclose(b1, self.height):
                    value = b1
                    latex = "l = \\frac {P + \\sqrt {\\frac {P^{2}} {2} + 2{D}^{2}} {2}"
                    self.length = value
                    return (value, latex)
                else:
                    value = b2
                    latex = "l = \\frac {P - \\sqrt {\\frac {P^{2}} {2} + 2{D}^{2}} {2}"
                    self.length = value
                    return (value, latex)
        elif self.surface is not None and self.diagonal is not None:
            s = float(self.surface)
            d = float(self.diagonal)
            b1 = np.sqrt((d**2 + np.sqrt(d**4 - 4*s**2))/2)
            b2 = np.sqrt((d**2 - np.sqrt(d**4 - 4*s**2))/2)
            if self.height is None:
                value = b1
                latex = "l = \\sqrt {\\frac {D^{2} + \\sqrt {D^{4} - 4S^{2}} {2}}"
                self.length = value
                return (value, latex)
            else:
                if not np.isclose(b1, self.height):
                    value = b1
                    latex = "l = \\sqrt {\\frac {D^{2} + \\sqrt {D^{4} - 4S^{2}} {2}}"
                    self.length = value
                    return (value, latex)
                else:
                    value = b2
                    latex = "l = \\sqrt {\\frac {D^{2} - \\sqrt {D^{4} - 4S^{2}} {2}}"
                    self.length = value
                    return (value, latex)
        elif self.surface is not None and self.perimeter is not None:
            p = float(self.perimeter)
            s = float(self.surface)
            b1 = (p + np.sqrt(p**2 - 16*s))/4
            b2 = (p - np.sqrt(p**2 - 16*s))/4
            if self.height is None:
                value = b1
                latex = "l = \\frac {P + \\sqrt {P^{2} - 16{S}} {4}"
                self.length = value
                return (value, latex)
            else:
                if not np.isclose(b1, self.height):
                    value = b1
                    latex = "l = \\frac {P + \\sqrt {P^{2} - 16{S}} {4}"
                    self.length = value
                    return (value, latex)
                else:
                    value = b2
                    latex = "l = \\frac {P - \\sqrt {P^{2} - 16{S}} {4}"
                    self.length = value
                    return (value, latex)
        else:
            return ("Not enough information about the polygon!\n", "{}")

    def get_height(self):
        if self.height is not None:
            return (self.height, "{}")
        elif self.perimeter is not None and self.length is not None:
            value = (float(self.perimeter) - 2*float(self.length))/2
            latex = "h = \\frac {P-2l} {2}"
            self.height = value
            return (value, latex)
        elif self.diagonal is not None and self.length is not None:
            value = float(np.sqrt(float(self.diagonal)**2 - float(self.length)**2))
            latex = "h = \\sqrt {D^{2} - l^{2}}"
            self.height = value
            return (value, latex)
        elif self.surface is not None and self.length is not None:
            value = float(self.surface) / float(self.length)
            latex = "h = \\frac {S} {l}"
            self.height = value
            return (value, latex)
        elif self.perimeter is not None and self.diagonal is not None:
            p = float(self.perimeter)
            d = float(self.diagonal)
            b1 = float((p + np.sqrt(p**2 / 2 + 2*d**2))/2)
            b2 = float((p - np.sqrt(p**2 / 2 + 2*d**2))/2)
            if self.length is None:
                value = b1
                latex = "h = \\frac {P + \\sqrt {\\frac {P^{2}} {2} + 2{D}^{2}} {2}"
                self.height = value
                return (value, latex)
            else:
                if not np.isclose(b1, self.length):
                    value = b1
                    latex = "h = \\frac {P + \\sqrt {\\frac {P^{2}} {2} + 2{D}^{2}} {2}"
                    self.height = value
                    return (value, latex)
                else:
                    value = b2
                    latex = "h = \\frac {P - \\sqrt {\\frac {P^{2}} {2} + 2{D}^{2}} {2}"
                    self.height = value
                    return (value, latex)
        elif self.surface is not None and self.diagonal is not None:
            s = float(self.surface)
            d = float(self.diagonal)
            b1 = float(np.sqrt((d**2 + np.sqrt(d**4 - 4*s**2))/2))
            b2 = float(np.sqrt((d**2 - np.sqrt(d**4 - 4*s**2))/2))
            if self.length is None:
                value = b1
                latex = "h = \\sqrt {\\frac {D^{2} + \\sqrt {D^{4} - 4S^{2}} {2}}"
                self.height = value
                return (value, latex)
            else:
                if not np.isclose(b1, self.length):
                    value = b1
                    latex = "h = \\sqrt {\\frac {D^{2} + \\sqrt {D^{4} - 4S^{2}} {2}}"
                    self.height = value
                    return (value, latex)
                else:
                    value = b2
                    latex = "h = \\sqrt {\\frac {D^{2} - \\sqrt {D^{4} - 4S^{2}} {2}}"
                    self.height = value
                    return (value, latex)
        elif self.surface is not None and self.perimeter is not None:
            p = float(self.perimeter)
            s = float(self.surface)
            b1 = float((p + np.sqrt(p**2 - 16*s))/4)
            b2 = float((p - np.sqrt(p**2 - 16*s))/4)
            if self.length is None:
                value = b1
                latex = "h = \\frac {P + \\sqrt {P^{2} - 16S} {4}"
                self.height = value
                return (value, latex)
            else:
                if not np.isclose(b1, self.length):
                    value = b1
                    latex = "h = \\frac {P + \\sqrt {P^{2} - 16S} {4}"
                    self.height = value
                    return (value, latex)
                else:
                    value = b2
                    latex = "h = \\frac {P - \\sqrt {P^{2} - 16S} {4}"
                    self.height = value
                    return (value, latex)
        else:
            return ("Not enough information about the polygon!\n", "{}")
        
    def get_perimeter(self):
        if self.perimeter is not None:
            return (self.perimeter, "{}")
        else:
            try:
                length, latex1 = self.get_length()
                height, latex2 = self.get_height()
                if (type(length) == type(0.1)) and (type(height) == type(0.1)):
                    value = 2*float(length) + 2*float(height)
                    latex = latex1 + " \\to " + latex2 + " \\to P = 2l + 2h"
                    self.perimeter = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_surface(self):
        if self.surface is not None:
            return (self.surface, "{}")
        else:
            try:
                length, latex1 = self.get_length()
                height, latex2 = self.get_height()
                if (type(length) == type(0.1)) and (type(height) == type(0.1)):
                    value = float(length)*float(height)
                    latex = latex1 + " \\to " + latex2 + " \\to S = h·l" 
                    self.surface = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_diagonal(self):
        if self.diagonal is not None:
            return (self.diagonal, "{}")
        else:
            try:
                length, latex1 = self.get_length()
                height, latex2 = self.get_height()
                if (type(length) == type(0.1)) and (type(height) == type(0.1)):
                    value = float(np.sqrt(float(length)**2 + float(height)**2))
                    latex = latex1 + " \\to " + latex2 + " \\to D = \\sqrt {l^{2} + h^{2}}"
                    self.diagonal = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_parameters(self):
        rectangle_value = []
        rectangle_latex = []
        try:
            rectangle_info = [self.get_length(), self.get_height(), self.get_diagonal(), self.get_perimeter(), self.get_surface()]
            rectangle_info = [(float(i[0]), i[1]) for i in rectangle_info]
            for i in rectangle_info: 
                if type(i[0]) == type(0.1):
                    rectangle_value.append(round(i[0], self.n))
                    rectangle_latex.append(i[1])
                    continue
                else:
                    return ("Not enough information about the polygon!", "{}")    
            return (rectangle_value, rectangle_latex)
        except TypeError:
            return ("Not enough information about the polygon!", "{}")

class RegularPolygon:
    def __init__(self, side=None, apothem=None, radius=None, perimeter=None, surface=None, n_sides=5, n=4):
        self.pi2 = float(n_sides * np.sin(np.pi/n_sides))
        self.side = side
        self.apothem = apothem
        self.radius = radius
        self.perimeter = perimeter
        self.surface = surface
        self.n_sides = int(n_sides)
        self.n = n
        self.angle = ((float(self.n_sides) - 2)*180)/float(self.n_sides)
        self.name = "RegularPolygon"

    def get_radius(self):
        if self.radius is not None:
            return (self.radius, "{}")
        elif self.perimeter is not None:
            value = float(self.perimeter)/(2*self.pi2)
            latex = "r = \\frac {P} {2\\beta}"
            self.radius = float(value)
            return (float(value), latex)
        elif self.surface is not None:
            value = (float(self.surface)/self.pi2)**(1/2)
            latex = "r = \\sqrt{\\frac {S} {\\beta}}"
            self.radius = float(value)
            return (float(value), latex)
        elif self.apothem is not None:
            value = float(self.apothem) / np.sin(self.angle*np.pi/360)
            latex = "r = \\frac {a} {\\sin(\\frac {\\alpha} {2})}"
            self.radius = float(value)
            return (float(value), latex)
        elif self.side is not None:
            value = float(self.side) / (2 * np.cos(self.angle*np.pi/360))
            latex = "r = \\frac {c} {\\cos(\\frac {\\alpha} {2})}"
            self.radius = float(value)
            return (float(value), latex)
        else:
            return ("Not enough information about the polygon!", "{}")

    def get_perimeter(self):
        if self.perimeter is not None:
            return (self.perimeter, "{}")
        else:
            try:
                radius, latex1 = self.get_radius()
                if type(radius) == type(0.1):
                    value = float(2*radius*self.pi2)
                    latex = latex1 + " \\to P = 2\\beta r"
                    self.perimeter = float(value)
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_surface(self):
        if self.surface is not None:
            return (self.surface, "{}")
        else:
            try:
                radius, latex1 = self.get_radius()
                if type(radius) == type(0.1):
                    value = float(self.pi2*(radius)**2)
                    latex = latex1 + " \\to S = \\beta r^{2}"
                    self.surface = float(value)
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_apothem(self):
        if self.apothem is not None:
            return (self.apothem, "{}")
        else:
            try:
                radius, latex1 = self.get_radius()
                if type(radius) == type(0.1):
                    value = float(radius * np.sin(self.angle*np.pi/360))
                    latex = latex1 + " \\to a = r·\\sin(frac {\\alpha} {2})"
                    self.apothem = float(value)
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")
    
    def get_side(self):
        if self.side is not None:
            return (self.side, "{}")
        else:
            try:
                radius, latex1 = self.get_radius()
                if type(radius) == type(0.1):
                    value = float(2 * radius * np.cos(self.angle*np.pi/360))
                    latex = latex1 + " \\to c = r·\\cos(frac {\\alpha} {2})"
                    self.side = float(value)
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_parameters(self):
        regular_polygon_value = []
        regular_polygon_latex = []

        try:
            regular_polygon_info = [(self.pi2, "n\\sin(\\frac {\\pi} {n})"), self.get_side(), self.get_radius(), self.get_apothem(), self.get_perimeter(), self.get_surface(), (self.n_sides, "{}"), (self.angle, "{}")]
            regular_polygon_info = [(float(i[0]), i[1]) for i in regular_polygon_info]
            for i in regular_polygon_info:    
                if type(float(i[0])) == type(0.1):
                    regular_polygon_value.append(round(i[0], self.n))
                    regular_polygon_latex.append(i[1])
                    continue
                else:
                    return ("Not enough information about the polygon!", "{}")    
            return (regular_polygon_value, regular_polygon_latex)
        except TypeError:
            return ("Not enough information about the polygon!", "{}")

class Rhomboid: 
    def __init__(self, length=None, height=None, side=None, perimeter=None, surface=None, diagonal=None, skew=None, n=4):
        self.length = length
        self.height = height
        self.side = side
        self.perimeter = perimeter
        self.surface = surface
        self.diagonal = diagonal
        self.skew = skew
        self.n = n
        self.name = "Rhomboid"

    def get_side(self):
        if self.side is not None:
            return (self.side, "{}")
        elif self.perimeter is not None and self.length is not None:
            value = (float(self.perimeter) - 2*float(self.length))/2
            latex = "c = \\frac {P - 2l} {2}"
            self.side = value
            return (value, latex)
        elif self.perimeter is not None and self.surface is not None and self.height is not None:
            value = float(self.perimeter)/2 - float(self.surface)/float(self.height)
            latex = "c = \\frac {P} {2} - \\frac {S} {h}"
            self.side = value
            return (value, latex)
        elif self.perimeter is not None and self.surface is not None and self.skew is not None:
            b1 = (float(self.perimeter) + np.sqrt(float(self.perimeter)**2 - 16*float(self.surface)/np.sin(float(self.skew) * np.pi/180))) / 4
            b2 = (float(self.perimeter) - np.sqrt(float(self.perimeter)**2 - 16*float(self.surface)/np.sin(float(self.skew) * np.pi/180))) / 4
            if self.length is None:
                value = b1
                latex = "c = \\frac {P + \\sqrt {P^{2} - \\frac {16S} {\\sin(\\alpha)}}} {4} "
                self.side = value
                return (value, latex)
            else:
                if not np.isclose(b1, self.length):
                    value = b1
                    latex = "c = \\frac {P + \\sqrt {P^{2} - \\frac {16S} {\\sin(\\alpha)}}} {4} "
                    self.side = value
                    return (value, latex)
                else:
                    value = b2
                    latex = "c = \\frac {P - \\sqrt {P^{2} - \\frac {16S} {\\sin(\\alpha)}}} {4} "
                    self.side = value
                    return (value, latex)
        elif self.height is not None and self.skew is not None:
            value = float(float(self.height) / np.sin(float(self.skew) * np.pi/180))
            latex = "c = \\frac {h} {\\sin(\\alpha)}"
            self.side = value
            return (value, latex)
        else:
            return ("Not enough information about the polygon!", "{}")

    def get_length(self):
        if self.length is not None:
            return (self.length, "{}")
        elif self.perimeter is not None and self.side is not None:
            value = float(self.perimeter)/2 - float(self.side)
            latex = "l = \\frac {P - 2c} {2}"
            self.length = value
            return (value, latex)
        elif self.surface is not None and self.height is not None:
            value = float(self.surface)/float(self.height)
            latex = "l = \\frac {S} {h}"
            self.length = value
            return (value, latex)
        elif self.surface is not None and self.side is not None and self.skew is not None:
            value = float(float(self.surface)/(float(self.side)*np.sin(float(self.skew)*np.pi/180)))
            latex = "l = \\frac {S} {c \\sin(\\alpha)}"
            self.length = value
            return (value, latex)
        elif self.perimeter is not None and self.surface is not None and self.skew is not None:
            b1 = (float(self.perimeter) + np.sqrt(float(self.perimeter)**2 - 16*float(self.surface)/np.sin(float(self.skew) * np.pi/180))) / 4
            b2 = (float(self.perimeter) - np.sqrt(float(self.perimeter)**2 - 16*float(self.surface)/np.sin(float(self.skew) * np.pi/180))) / 4
            if self.side is None:
                value = b1
                latex = "l = \\frac {P + \\sqrt {P^{2} - \\frac {16S} {\\sin(\\alpha)}}} {4} "
                self.side = value
                return (value, latex)
            else:
                if not np.isclose(b1, self.side):
                    value = b1
                    latex = "l = \\frac {P + \\sqrt {P^{2} - \\frac {16S} {\\sin(\\alpha)}}} {4} "
                    self.side = value
                    return (value, latex)
                else:
                    value = b2
                    latex = "l = \\frac {P - \\sqrt {P^{2} - \\frac {16S} {\\sin(\\alpha)}}} {4} "
                    self.side = value
                    return (value, latex)
        else:
            return ("Not enough information about the polygon!", "{}")

    def get_height(self):
        if self.height is not None:
            return (self.height, "{}")
        elif self.side is not None and self.skew is not None:
            value = float(float(self.side) * np.sin(float(self.skew) * np.pi/180))
            latex = "h = c \\sin(\\alpha)"
            self.height = value
            return (value, latex)
        elif self.perimeter is not None and self.side is not None and self.surface is not None:
            value = (2*float(self.surface))/(2*float(self.side) - float(self.perimeter))
            latex = "h = \\frac {2S} {2a - P}"
            self.height = value
            return (value, latex)
        elif self.surface is not None and self.length is not None:
            value = float(self.surface)/float(self.length)
            latex = "h = \\frac {S} {l}"
            self.height = value
            return (value, latex)
        else:
            return ("Not enough information about the polygon!", "{}")

    def get_perimeter(self):
        if self.perimeter is not None:
            return (self.perimeter, "{}")
        else:
            try:
                length, latex1 = self.get_length()
                side, latex2 = self.get_side()
                if (type(length) == type(0.1)) and (type(side) == type(0.1)):
                    value = 2*float(length) + 2*float(side)
                    latex = latex1 + " \\to " + latex2 + " \\to P = 2l + 2c" # type: ignore
                    self.perimeter = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_surface(self):
        if self.surface is not None:
            return (self.surface, "{}")
        else:
            try:
                length, latex1 = self.get_length()
                height, latex2 = self.get_height()
                if (type(length) == type(0.1)) and (type(height) == type(0.1)):
                    value = float(length)*float(height)
                    latex = latex1 + " \\to " + latex2 + " \\to S = lh"
                    self.surface = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_diagonal(self):
        if self.diagonal is not None:
            return (self.diagonal, "{}")
        else:
            try:
                length, latex1 = self.get_length()
                side, latex3 = self.get_side()
                skew, latex4 = self.get_skew()
                if (type(length) == type(0.1)) and (type(side) == type(0.1)):
                    value = float(np.sqrt(length**2 + side**2 + 2*side*length*np.cos(skew*np.pi/180))) # type: ignore
                    latex = latex1 + " \\to " + latex3 + " \\to " + latex4 + " \\to D = \\sqrt {l^{2} + c^{2} + 2lc·\\cos(\\alpha)}" # type: ignore
                    self.diagonal = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_skew(self):
        if self.skew is not None:
            return (self.skew, "{}")
        else:
            try:
                height, latex1 = self.get_height()
                side, latex2 = self.get_side()
                if (type(height) == type(0.1)) and (type(side) == type(0.1)):
                    value = float(np.arcsin(height/side)*180/np.pi)
                    latex = latex1 + " \\to " + latex2 + " \\to \\alpha = \\arcsin(\\frac {h} {c})"
                    self.skew = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_parameters(self):
        rhomboid_value = []
        rhomboid_latex = []
        try:
            rhomboid_info = [self.get_length(), self.get_height(), self.get_side(), self.get_skew(), self.get_perimeter(), self.get_surface(), self.get_diagonal()]
            rhomboid_info = [(float(i[0]), i[1]) for i in rhomboid_info]
            for i in rhomboid_info:    
                if type(i[0]) == type(0.1):
                    rhomboid_value.append(round(i[0], self.n))
                    rhomboid_latex.append(i[1])
                    continue
                else:
                    return ("Not enough information about the polygon!", "{}")    
            return (rhomboid_value, rhomboid_latex)
        except TypeError:
            return ("Not enough information about the polygon!", "{}")

class Square:
    def __init__(self, side=None, surface=None, perimeter=None, diagonal=None, n=4):
        self.side = side
        self.surface = surface
        self.perimeter = perimeter
        self.diagonal = diagonal
        self.n = n
        self.name = "Square"


    def get_side(self):
        if self.side is not None:
            return (self.side, "{}")
        elif self.perimeter is not None:
            value = float(self.perimeter)/4
            latex = "a = \\frac {P} {4}"
            self.side = value
            return (value, latex)
        elif self.surface is not None:
            value = float(self.surface)**(1/2)
            latex = "a = \\sqrt{S}"
            self.side = value
            return (value, latex)
        elif self.diagonal is not None:
            value = float(self.diagonal)/(2**(1/2))
            latex = "a = \\frac {D} {\\sqrt{2}}"
            self.side = value
            return (value, latex)
        else:
            return ("Not enough information about the polygon!", "{}")
        
    def get_perimeter(self):
        if self.perimeter is not None:
            return (self.perimeter, "{}")
        else:
            try:
                if type(self.get_side()[0]) == type(0.1):
                    side, latex1 = self.get_side()
                    value = 4*float(side)
                    latex = latex1 + " \\to P = 4c" # type: ignore
                    self.perimeter = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_surface(self):
        if self.surface is not None:
            return (self.surface, "{}")
        else:
            try:
                if type(self.get_side()[0]) == type(0.1):
                    side, latex1 = self.get_side()
                    value = float(side)**2
                    latex = latex1 + " \\to S = c^{2}"
                    self.surface = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_diagonal(self):
        if self.diagonal is not None:
            return (self.diagonal, "{}")
        else:
            try:
                if type(self.get_side()[0]) == type(0.1):
                    side, latex1 = self.get_side()
                    value = float(side)**np.sqrt(2)
                    latex = latex1 + " \\to D = c \\sqrt{2}"
                    self.diagonal = value
                    return (value, latex)
                else:
                    return ("Something went wrong...", "{}")
            except TypeError:
                return ("Not enough information about the polygon!", "{}")

    def get_parameters(self):
        square_value = []
        square_latex = []
        try:
            square_info = [self.get_side(), self.get_diagonal(), self.get_perimeter(), self.get_surface()]
            square_info = [(float(i[0]), i[1]) for i in square_info]
            for i in square_info:    
                if type(i[0]) == type(0.1):
                    square_value.append(round(i[0], self.n))
                    square_latex.append(i[1])
                    continue
                else:
                    return ("Not enough information about the polygon!", "{}")
            return (square_value, square_latex)
        except TypeError:
            return ("Not enough information about the polygon!", "{}")

class Triangle:
    def __init__(self, angle1=None, angle2=None, angle3=None, side1=None, side2=None, side3=None, perimeter=None,
                 surface=None, n=2):
        self.name = "Triangle"
        self.n = n
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.perimeter = perimeter
        self.surface = surface

    def check(self):
        if float(self.angle1) is not None and float(self.angle2) is not None and float(self.angle3) is not None: # type: ignore
            angle = float(self.angle1) + float(self.angle2) + float(self.angle3) # type: ignore
            if np.isclose(angle, 180.0):
                return ("Valid", "{}")
            else:
                return ("Enter valid angle values! (must sum 180º)", "{}")
        else:
            return (None, "{}")

    def get_side1(self):
        if self.side1 is not None:
            return (self.side1, "{}")
        elif self.side2 is not None and self.side3 is not None and self.angle1 is not None:
            value = np.sqrt(float(self.side3)**2 + float(self.side2)**2 - 2*float(self.side3) * float(self.side2) * np.cos(float(self.angle1)*np.pi/180))
            latex = "a_{1} = \\sqrt {{a_{3}}^{2} + {a_{2}}^{2} - 2{a}_{3}{a}_{2} \\cos({\\alpha}_{1})}"
            self.side1 = value
            return (value, latex)
        elif self.side2 is not None and self.side3 is not None and self.angle2 is not None:
            angle3 = float(np.arcsin(float(self.side3)*np.sin(float(self.angle2)*np.pi/180)/float(self.side2))*180/np.pi)
            self.angle3 = angle3
            angle1 = float(180 - float(self.angle2) - angle3)
            self.angle1 = angle1
            value = np.sqrt(float(self.side3)**2 + float(self.side2)**2 - 2*float(self.side3)*float(self.side2) * (np.cos(angle1*np.pi/180)))
            latex = "{\\alpha}_{3} = \\arcsin(\\frac {a_{3} \\sin({\\alpha}_{2})} {a_{2}}) \\to {\\alpha}_{1} = 180 - {\\alpha}_{2} - {\\alpha}_{3} \\to a_{1} = \\sqrt{{a_{3}}^{2} + {a_{2}}^{2} - 2{a}_{3}{a}_{2} \\cos({\\alpha}_{1})}"
            self.side1 = value
            return (value, latex)
        elif self.side2 is not None and self.side3 is not None and self.angle3 is not None:
            angle2 = np.arcsin(float(self.side2)*np.sin(float(self.angle3)*np.pi/180)/float(self.side3))*180/np.pi
            self.angle2 = angle2
            angle1 = float(180 - float(self.angle3) - angle2)
            self.angle1 = angle1
            value = np.sqrt(float(self.side3)**2 + float(self.side2)**2 - 2*float(self.side3)*float(self.side2) * (np.cos(angle1*np.pi/180)))
            latex = "{\\alpha}_{2} = \\arcsin(\\frac {a_{2} \\sin({\\alpha}_{3})} {a_{3}}) \\to {\\alpha}_{1} = 180 - {\\alpha}_{2} - {\\alpha}_{3} \\to a_{1} = \\sqrt{{a_{3}}^{2} + {a_{2}}^{2} - 2{a}_{3}{a}_{2} \\cos({\\alpha}_{1})}"
            self.side1 = value
            return (value, latex)
        elif self.angle2 is not None and self.angle3 is not None and self.side2 is not None:
            angle1 = float(180 - float(self.angle2) - float(self.angle3))
            self.angle1 = angle1
            value = float(self.side2)*np.sin(angle1*np.pi/180)/np.sin(float(self.angle2)*np.pi/180)
            latex = "{\\alpha}_{1} = 180 - {\\alpha}_{3} - {\\alpha}_{2} \\to a_{1} = \\frac {a_{2} \\sin({\\alpha}_{1})} {\\sin({\\alpha}_{2})}"
            self.side1 = value
            return (value, latex)
        elif self.angle2 is not None and self.angle3 is not None and self.side3 is not None:
            angle1 = float(180 - float(self.angle2) - float(self.angle3))
            self.angle1 = angle1
            value = float(self.side3)*np.sin(angle1*np.pi/180)/np.sin(float(self.angle3)*np.pi/180)
            latex = "{\\alpha}_{1} = 180 - {\\alpha}_{3} - {\\alpha}_{2} \\to a_{1} = \\frac {a_{3} \\sin({\\alpha}_{1})} {\\sin({\\alpha}_{3})}"
            self.side1 = value
            return (value, latex)
        elif self.angle1 is not None and self.angle3 is not None and self.side3 is not None:
            value = float(self.side3)*np.sin(float(self.angle1)*np.pi/180)/np.sin(float(self.angle3)*np.pi/180)
            latex = "a_{1} = \\frac {a_{3} \\sin({\\alpha}_{1})} {\\sin({\\alpha}_{3})}"
            self.side1 = value
            return (value, latex)
        elif self.angle1 is not None and self.angle2 is not None and self.side2 is not None:
            value = float(self.side2)*np.sin(float(self.angle1)*np.pi/180)/np.sin(float(self.angle2)*np.pi/180)
            latex = "a_{1} = \\frac {a_{2} \\sin({\\alpha}_{1})} {\\sin({\\alpha}_{2})}"
            self.side1 = value
            return (value, latex)
        elif self.angle1 is not None and self.angle2 is not None and self.side3 is not None:
            angle3 = float(180 - float(self.angle1) - float(self.angle2))
            self.angle3 = angle3
            value = float(self.side3)*np.sin(float(self.angle1)*np.pi/180)/np.sin(angle3*np.pi/180)
            latex = "{\\alpha}_{3} = 180 - {\\alpha}_{1} - {\\alpha}_{2} \\to a_{1} = \\frac {a_{3} \\sin({\\alpha}_{1})} {\\sin({\\alpha}_{3})}"
            self.side1 = value
            return (value, latex)
        elif self.angle1 is not None and self.angle3 is not None and self.side2 is not None:
            angle2 = float(180 - float(self.angle1) - float(self.angle3))
            self.angle2 = angle2
            value = float(self.side2)*np.sin(float(self.angle1)*np.pi/180)/np.sin(angle2*np.pi/180)
            latex = "{\\alpha}_{2} = 180 - {\\alpha}_{1} - {\\alpha}_{3} \\to a_{1} = \\frac {a_{2} \\sin({\\alpha}_{1})} {\\sin({\\alpha}_{2})}"
            self.side1 = value
            return (value, latex)
        elif self.perimeter is not None and self.side2 is not None and self.side3 is not None:
            value = float(self.perimeter) - float(self.side2) - float(self.side3)
            latex = "a_{1} = P - a_{2} - a_{3}"
            self.side1 = value
            return (value, latex)
        elif self.perimeter is not None and self.angle1 is not None and self.angle2 is not None:
            angle3 = float(180 - float(self.angle1) - float(self.angle2))
            self.angle3 = angle3
            value = (float(self.perimeter) * np.sin(float(self.angle1)*np.pi/180) / (4*np.cos(float(self.angle1)*np.pi/180)*np.cos(float(self.angle2)*np.pi/180)*np.cos(angle3*np.pi/180)))
            latex = "{\\alpha}_{3} = 180 - {\\alpha}_{1} - {\\alpha}_{2} \\to a_{1} = \\frac {P \\sin({\\alpha}_{1})} {4\\cos(\\frac {{\\alpha}_{1}} {2})\\cos(\\frac {{\\alpha}_{2}} {2})\\cos(\\frac {{\\alpha}_{3}} {2})}"
            self.side1 = value
            return (value, latex)
        elif self.perimeter is not None and self.angle1 is not None and self.angle3 is not None:
            angle2 = float(180 - float(self.angle1) - float(self.angle3))
            self.angle2 = angle2
            value = (float(self.perimeter) * np.sin(float(self.angle1)*np.pi/180) / (4*np.cos(float(self.angle1)*np.pi/180)*np.cos(angle2*np.pi/180)*np.cos(float(self.angle3)*np.pi/180)))
            latex = "{\\alpha}_{2} = 180 - {\\alpha}_{1} - {\\alpha}_{3} \\to a_{1} = \\frac {P \\sin({\\alpha}_{1})} {4\\cos(\\frac {{\\alpha}_{1}} {2})\\cos(\\frac {{\\alpha}_{2}} {2})\\cos(\\frac {{\\alpha}_{3}} {2})}"
            self.side1 = value
            return (value, latex)  
        elif self.perimeter is not None and self.angle2 is not None and self.angle3 is not None:
            angle1 = float(180 - float(self.angle2) - float(self.angle3))
            self.angle1 = angle1
            value = (float(self.perimeter) * np.sin(angle1*np.pi/180) / (4*np.cos(angle1*np.pi/180)*np.cos(float(self.angle2)*np.pi/180)*np.cos(float(self.angle3)*np.pi/180)))
            latex = "{\\alpha}_{1} = 180 - {\\alpha}_{2} - {\\alpha}_{3} \\to a_{1} = frac {P \\sin({\\alpha}_{1})} {4\\cos(\\frac {{\\alpha}_{1}} {2})\\cos(\\frac {{\\alpha}_{2}} {2})\\cos(\\frac {{\\alpha}_{3}} {2})}"
            self.side1 = value
            return (value, latex)
        elif self.perimeter is not None and self.side2 is not None and self.angle2 is not None:
            angle1 = float(np.arcsin(np.sin(float(self.angle2)*np.pi/180)*(float(self.perimeter)/float(self.side2) - 1)/(2 * np.cos(float(self.angle2)*np.pi/360)))*180/np.pi - float(self.angle2)/2)
            self.angle1 = angle1
            value = float(self.side2) * np.sin(angle1*np.pi/180)/np.sin(float(self.angle2)*np.pi/180)
            latex = "{\\alpha}_{1} = \\arcsin(\\frac {\\sin({\\alpha}_{2})} {2\\cos(\\frac {{\\alpha}_{2}} {2})} (\\frac {P} {a_{2}} - 1)) - \\frac {{\\alpha}_{2}} {2} \\to a_{1} = \\frac {a_{2} \\sin({\\alpha}_{1}})} {\\sin({\\alpha}_{2})}"
            self.side1 = value
            return (value, latex)
        elif self.perimeter is not None and self.side3 is not None and self.angle3 is not None:
            angle1 = float(np.arcsin(np.sin(float(self.angle3)*np.pi/180)*(float(self.perimeter)/float(self.side3) - 1)/(2 * np.cos(float(self.angle3)*np.pi/360)))*180/np.pi - float(self.angle3)/2)
            self.angle1 = angle1
            value = float(self.side3) * np.sin(angle1*np.pi/180)/np.sin(float(self.angle3)*np.pi/180)
            latex = "{\\alpha}_{1} = \\arcsin(\\frac {\\sin({\\alpha}_{3})} {2\\cos(\\frac {{\\alpha}_{3}} {2})} (\\frac {P} {a_{3}} - 1)) - \\frac {{\\alpha}_{3}} {2} \\to a_{1} = \\frac {a_{3} \\sin({\\alpha}_{1}})} {\\sin({\\alpha}_{3})}"
            self.side1 = value
            return (value, latex)
        elif self.perimeter is not None and self.side2 is not None and self.angle1 is not None:
            value = -(2*float(self.side2)*(float(self.side2) + (float(self.side2) - float(self.perimeter))*np.cos(float(self.angle1)*np.pi/180) - float(self.perimeter)) + float(self.perimeter)**2)/(2*(float(self.side2)*np.cos(float(self.angle1)*np.pi/180) + float(self.side2) - float(self.perimeter)))
            latex = "a_{1} = \\frac {2a_{2}(a_{2} + (a_{2} - P)\\cos({\\alpha}_{1}) - P) + {P}^{2}} {2(a_{2}\\cos({\\alpha}_{1}) + a_{2} - P)}"
            self.side1 = value
            return (value, latex)
        elif self.perimeter is not None and self.side3 is not None and self.angle1 is not None:
            value = -(2*float(self.side3)*(float(self.side3) + (float(self.side3) - float(self.perimeter))*np.cos(float(self.angle1)*np.pi/180) - float(self.perimeter)) + float(self.perimeter)**2)/(2*(float(self.side3)*np.cos(float(self.angle1)*np.pi/180) + float(self.side3) - float(self.perimeter)))
            latex = "a_{1} = \\frac {2a_{3}(a_{3} + (a_{3} - P)\\cos({\\alpha}_{1}) - P) + {P}^{2}} {2(a_{3}\\cos({\\alpha}_{1}) + a_{3} - P)}"
            self.side1 = value
            return (value, latex)
        elif self.perimeter is not None and self.side3 is not None and self.angle2 is not None:
            value = (float(self.perimeter)*(2*float(self.side3) - float(self.perimeter)))/(2*(float(self.side3)*np.cos(float(self.angle2)*np.pi/180) + float(self.side3) - float(self.perimeter)))
            latex = "a_{1} = \\frac {P(2a_{3} - P)} {2(a_{3}\\cos({\\alpha}_{2}) + a_{3} - P)}}"
            self.side1 = value
            return (value, latex)
        elif self.perimeter is not None and self.side2 is not None and self.angle3 is not None:
            value = (float(self.perimeter)*(2*float(self.side2) - float(self.perimeter)))/(2*(float(self.side2)*np.cos(float(self.angle3)*np.pi/180) + float(self.side2) - float(self.perimeter)))
            latex = "a_{1} = \\frac {P(2a_{2} - P)} {2(a_{2}\\cos({\\alpha}_{3}) + a_{2} - P)}}"
            self.side1 = value
            return (value, latex)
        elif self.surface is not None and self.side2 is not None and self.angle3 is not None:
            value = 2*float(self.surface)/(float(self.side2)*np.sin(float(self.angle3)*np.pi/180))
            latex = "a_{1} = \\frac {2S} {a_{2} \\sin({\\alpha}_{3})}"
            self.side1 = value
            return (value, latex)
        elif self.surface is not None and self.side3 is not None and self.angle2 is not None:
            value = 2*float(self.surface)/(float(self.side3)*np.sin(float(self.angle2)*np.pi/180))
            latex = "a_{1} = \\frac {2S} {a_{3} \\sin({\\alpha}_{2})}"
            self.side1 = value
            return (value, latex)
        elif self.surface is not None and self.angle1 is not None and self.angle2 is not None:
            angle3 = 180 - float(self.angle1) - float(self.angle2)
            self.angle3 = angle3
            value = np.sqrt(2*float(self.surface)*np.sin(float(self.angle1)*np.pi/180)/(np.sin(angle3*np.pi/180)*np.sin(float(self.angle2)*np.pi/180)))
            latex = "{\\alpha}_{3} = 180 - {\\alpha}_{1} - {\\alpha}_{2} \\to a_{1} = \\sqrt{\\frac {2S\\sin({\\alpha}_{1})} {\\sin({\\alpha}_{2}) \\sin({\\alpha}_{3})}}"
            self.side1 = value
            return (value, latex)
        elif self.surface is not None and self.angle1 is not None and self.angle3 is not None:
            angle2 = 180 - float(self.angle1) - float(self.angle3)
            self.angle2 = angle2
            value = np.sqrt(2*float(self.surface)*np.sin(float(self.angle1)*np.pi/180)/(np.sin(float(self.angle3)*np.pi/180)*np.sin(angle2*np.pi/180)))
            latex = "{\\alpha}_{2} = 180 - {\\alpha}_{1} - {\\alpha}_{3} \\to a_{1} = \\sqrt{\\frac {2S\\sin({\\alpha}_{1})} {\\sin({\\alpha}_{2}) \\sin({\\alpha}_{3})}}"
            self.side1 = value
            return (value, latex)
        elif self.surface is not None and self.angle2 is not None and self.angle3 is not None:
            angle1 = 180 - float(self.angle2) - float(self.angle3)
            self.angle1 = angle1
            value = np.sqrt(2*float(self.surface)*np.sin(angle1*np.pi/180)/(np.sin(float(self.angle3)*np.pi/180)*np.sin(float(self.angle2)*np.pi/180)))
            latex = "{\\alpha}_{1} = 180 - {\\alpha}_{2} - {\\alpha}_{3} \\to a_{1} = \\sqrt{\\frac {2S\\sin({\\alpha}_{1})} {\\sin({\\alpha}_{2}) \\sin({\\alpha}_{3})}}"
            self.side1 = value
            return (value, latex)
        elif self.surface is not None and self.side2 is not None and self.angle1 is not None:
            value = np.sqrt(float(self.side2)**4 - 4*float(self.side2)**2*float(self.surface)/(np.tan(float(self.angle1)*np.pi/180)) + 4*float(self.surface)**2/((np.sin(float(self.angle1)*np.pi/180)**2)))/float(self.side2)
            latex = "a_{1} = \\frac {\\sqrt{{a_{2}}^{4} - 4{a_{2}}^{2}S \\cot({\\alpha}_{1}) + 4S^{2} {\\csc({\\alpha}_{1})}^{2}}} {a_{2}}"
            self.side1 = value
            return (value, latex)
        elif self.surface is not None and self.side3 is not None and self.angle1 is not None:
            value = np.sqrt(float(self.side3)**4 - 4*float(self.side3)**2*float(self.surface)/(np.tan(float(self.angle1)*np.pi/180)) + 4*float(self.surface)**2/((np.sin(float(self.angle1)*np.pi/180)**2)))/float(self.side3)
            latex = "a_{1} = \\frac {\\sqrt{{a_{3}}^{4} - 4{a_{3}}^{2}S \\cot({\\alpha}_{1}) + 4S^{2} {\\csc({\\alpha}_{1})}^{2}}} {a_{3}}"
            self.side1 = value
            return (value, latex)
        elif self.surface is not None and self.side3 is not None and self.side2 is not None:
            value = np.sqrt(float(self.side2)**2 + float(self.side3)**2 - 2*np.sqrt(float(self.side2)**2*float(self.side3)**2 - 4*float(self.surface)**2))
            latex = "a_{1} = \\sqrt{{a_{2}}^{2} + {a_{3}}^{2} - 2 \\sqrt{{a_{2}}^{2}{a_{3}}^{2} - 4S^{2}}}"
            self.side1 = value
            return (value, latex)
        elif self.surface is not None and self.side2 is not None and self.angle2 is not None:
            b1 = np.sqrt((float(self.side2)**2 + 4*float(self.surface)/(np.tan(float(self.angle2)*np.pi/180)) + np.sqrt(float(self.side2)**4 + 8*float(self.side2)**2*float(self.surface)/(np.tan(float(self.angle2)*np.pi/180)) - 16*float(self.surface)**2))/2)
            b2 = np.sqrt((float(self.side2)**2 + 4*float(self.surface)/(np.tan(float(self.angle2)*np.pi/180)) - np.sqrt(float(self.side2)**4 + 8*float(self.side2)**2*float(self.surface)/(np.tan(float(self.angle2)*np.pi/180)) - 16*float(self.surface)**2))/2)
            if abs(complex(b1).imag) < 0.00000000000000001:
                value = b1
                latex = "a_{1} = \\sqrt {\\frac {{a_{2}}^{2} + 4S\\cot({\\alpha}_{2}) + \\sqrt {{a_{2}}^{4} + 8S{a_{2}}^{2}\\cot({\\alpha}_{2}) - 16S^{2}}} {2}}}"
                self.side1 = value
                return (value, latex)
            elif abs(complex(b2).imag) < 0.00000000000000001:
                value = b2
                latex = "a_{1} = \\sqrt {\\frac {{a_{2}}^{2} + 4S\\cot({\\alpha}_{2}) - \\sqrt {{a_{2}}^{4} + 8S{a_{2}}^{2}\\cot({\\alpha}_{2}) - 16S^{2}}} {2}}}"
                self.side1 = value
                return (value, latex)
            else:
                return("wft??!!", "{}")
        elif self.surface is not None and self.side3 is not None and self.angle3 is not None:
            b1 = np.sqrt((float(self.side3)**2 + 4*float(self.surface)/(np.tan(float(self.angle3)*np.pi/180)) + np.sqrt(float(self.side3)**4 + 8*float(self.side3)**2*float(self.surface)/(np.tan(float(self.angle3)*np.pi/180)) - 16*float(self.surface)**2))/2)
            b2 = np.sqrt((float(self.side3)**2 + 4*float(self.surface)/(np.tan(float(self.angle3)*np.pi/180)) - np.sqrt(float(self.side3)**4 + 8*float(self.side3)**2*float(self.surface)/(np.tan(float(self.angle3)*np.pi/180)) - 16*float(self.surface)**2))/2)
            if abs(complex(b1).imag) < 0.00000000000000001:
                value = b1
                latex = "a_{1} = \\sqrt {\\frac {{a_{3}}^{2} + 4S\\cot({\\alpha}_{3}) + \\sqrt {{a_{3}}^{4} + 8S{a_{3}}^{2}\\cot({\\alpha}_{3}) - 16S^{2}}} {2}}}"
                self.side1 = value
                return (value, latex)
            elif abs(complex(b2).imag) < 0.00000000000000001:
                value = b2
                latex = "a_{1} = \\sqrt {\\frac {{a_{3}}^{2} + 4S\\cot({\\alpha}_{3}) - \\sqrt {{a_{3}}^{4} + 8S{a_{3}}^{2}\\cot({\\alpha}_{3}) - 16S^{2}}} {2}}}"
                self.side1 = value
                return (value, latex)
            else:
                return("wft??!!", "{}")
        elif self.angle2 is not None and self.perimeter is not None and self.surface is not None:
            b1 = (np.sqrt((float(self.perimeter)**2*np.sin(float(self.angle2)*np.pi/180) + 4*float(self.surface)*(np.cos(float(self.angle2)*np.pi/180) + 1))**2 - 32*float(self.perimeter)**2*float(self.surface)*np.sin(float(self.angle2)*np.pi/180))/(np.sin(float(self.angle2)*np.pi/180)) + 4*float(self.surface)*(1/(np.tan(float(self.angle2)*np.pi/180))+1/(np.sin(float(self.angle2)*np.pi/180))) + float(self.perimeter)**2)/(4*float(self.perimeter))
            b2 = (np.sqrt((float(self.perimeter)**2*np.sin(float(self.angle2)*np.pi/180) + 4*float(self.surface)*(np.cos(float(self.angle2)*np.pi/180) + 1))**2 - 32*float(self.perimeter)**2*float(self.surface)*np.sin(float(self.angle2)*np.pi/180))/(np.sin(float(self.angle2)*np.pi/180)) - 4*float(self.surface)*(1/(np.tan(float(self.angle2)*np.pi/180))+1/(np.sin(float(self.angle2)*np.pi/180))) + float(self.perimeter)**2)/(4*float(self.perimeter))
            if b1>0:
                value = b1
                latex = "a_{1} = \\frac {1} {4P} (\\csc({\\alpha}_{2}) \\sqrt{{P^{2}\\sin({\\alpha}_{2}) + 4S(\\cos({\\alpha}_{2}) + 1)}^{2} - 32P^{2}S\\sin({\\alhpa}_{2})} + 4S(\\cot({\\alpha}_{2}) + \\csc({\\alpha}_{2}}) P^{2})"
                self.side1 = value
                return (value, latex)
            elif b2>0:
                value = b2
                latex = "a_{1} = \\frac {1} {4P} (\\csc({\\alpha}_{2}) \\sqrt{{P^{2}\\sin({\\alpha}_{2}) + 4S(\\cos({\\alpha}_{2}) + 1)}^{2} - 32P^{2}S\\sin({\\alhpa}_{2})} - 4S(\\cot({\\alpha}_{2}) + \\csc({\\alpha}_{2}}) P^{2})"
                self.side1 = value
                return (value, latex)
            else:
                return("wtf?!?!", "{}")
        elif self.angle3 is not None and self.perimeter is not None and self.surface is not None:
            b1 = (np.sqrt((float(self.perimeter)**2*np.sin(float(self.angle3)*np.pi/180) + 4*float(self.surface)*(np.cos(float(self.angle3)*np.pi/180) + 1))**2 - 32*float(self.perimeter)**2*float(self.surface)*np.sin(float(self.angle3)*np.pi/180))/(np.sin(float(self.angle3)*np.pi/180)) + 4*float(self.surface)*(1/(np.tan(float(self.angle3)*np.pi/180))+1/(np.sin(float(self.angle3)*np.pi/180))) + float(self.perimeter)**2)/(4*float(self.perimeter))
            b2 = (np.sqrt((float(self.perimeter)**2*np.sin(float(self.angle3)*np.pi/180) + 4*float(self.surface)*(np.cos(float(self.angle3)*np.pi/180) + 1))**2 - 32*float(self.perimeter)**2*float(self.surface)*np.sin(float(self.angle3)*np.pi/180))/(np.sin(float(self.angle3)*np.pi/180)) - 4*float(self.surface)*(1/(np.tan(float(self.angle3)*np.pi/180))+1/(np.sin(float(self.angle3)*np.pi/180))) + float(self.perimeter)**2)/(4*float(self.perimeter))
            if b1>0:
                value = b1
                latex = "a_{1} = \\frac {1} {4P} (\\csc({\\alpha}_{3}) \\sqrt{{P^{2}\\sin({\\alpha}_{3}) + 4S(\\cos({\\alpha}_{3}) + 1)}^{2} - 32P^{2}S\\sin({\\alhpa}_{3})} + 4S(\\cot({\\alpha}_{3}) + \\csc({\\alpha}_{3}}) P^{2})"
                self.side1 = value
                return (value, latex)
            elif b2>0:
                value = b2
                latex = "a_{1} = \\frac {1} {4P} (\\csc({\\alpha}_{3}) \\sqrt{{P^{2}\\sin({\\alpha}_{3}) + 4S(\\cos({\\alpha}_{3}) + 1)}^{2} - 32P^{2}S\\sin({\\alhpa}_{3})} - 4S(\\cot({\\alpha}_{3}) + \\csc({\\alpha}_{3}}) P^{2})"
                self.side1 = value
                return (value, latex)
            else:
                return("wtf?!?!", "{}")
        elif self.side2 is not None and self.perimeter is not None and self.surface is not None:
            b1 = (3*float(self.side2)*float(self.perimeter) - float(self.perimeter)**2 -2*float(self.side2)**2 + np.sqrt((2*float(self.side2) - float(self.perimeter))*(2*float(self.side2)**3*float(self.perimeter) - float(self.perimeter)**2*float(self.side2)**2 + 16*float(self.surface)**2)/float(self.perimeter)))/(2*(2*float(self.side2) - float(self.perimeter)))
            b2 = (3*float(self.side2)*float(self.perimeter) - float(self.perimeter)**2 -2*float(self.side2)**2 - np.sqrt((2*float(self.side2) - float(self.perimeter))*(2*float(self.side2)**3*float(self.perimeter) - float(self.perimeter)**2*float(self.side2)**2 + 16*float(self.surface)**2)/float(self.perimeter)))/(2*(2*float(self.side2) - float(self.perimeter)))
            if b1>0:
                value = b1
                latex = "a_{1} = \\frac {3a_{2}P - P^{2} - 2{a_{2}}^{2} + \\sqrt {\\frac {(2a_{2} - P)(2{a_{2}}^{3}P - {a_{2}}^{2}P^{2} + 16S^{2})} {P}}} {2(2a_{2} - P)}"
                self.side1 = value
                return (value, latex)
            elif b2>0:
                value = b2
                latex = "a_{1} = \\frac {3a_{2}P - P^{2} - 2{a_{2}}^{2} - \\sqrt {\\frac {(2a_{2} - P)(2{a_{2}}^{3}P - {a_{2}}^{2}P^{2} + 16S^{2})} {P}}} {2(2a_{2} - P)}"
                self.side1 = value
                return (value, latex)
            else:
                return("wtf?!?!", "{}")
        elif self.side3 is not None and self.perimeter is not None and self.surface is not None:
            b1 = (3*float(self.side3)*float(self.perimeter) - float(self.perimeter)**2 -2*float(self.side3)**2 + np.sqrt((2*float(self.side3) - float(self.perimeter))*(2*float(self.side3)**3*float(self.perimeter) - float(self.perimeter)**2*float(self.side3)**2 + 16*float(self.surface)**2)/float(self.perimeter)))/(2*(2*float(self.side3) - float(self.perimeter)))
            b2 = (3*float(self.side3)*float(self.perimeter) - float(self.perimeter)**2 -2*float(self.side3)**2 - np.sqrt((2*float(self.side3) - float(self.perimeter))*(2*float(self.side3)**3*float(self.perimeter) - float(self.perimeter)**2*float(self.side3)**2 + 16*float(self.surface)**2)/float(self.perimeter)))/(2*(2*float(self.side3) - float(self.perimeter)))
            if b1>0:
                value = b1
                latex = "a_{1} = \\frac {3a_{3}P - P^{2} - 2{a_{3}}^{2} + \\sqrt {\\frac {(2a_{3} - P)(2{a_{3}}^{3}P - {a_{3}}^{2}P^{2} + 16S^{2})} {P}}} {2(2a_{3} - P)}"
                self.side1 = value
                return (value, latex)
            elif b2>0:
                value = b2
                latex = "a_{1} = \\frac {3a_{3}P - P^{2} - 2{a_{3}}^{2} - \\sqrt {\\frac {(2a_{3} - P)(2{a_{3}}^{3}P - {a_{3}}^{2}P^{2} + 16S^{2})} {P}}} {2(2a_{3} - P)}"
                self.side1 = value
                return (value, latex)
            else:
                return("wtf?!?!", "{}")
        elif self.surface is not None and self.perimeter is not None and self.angle1 is not None:
            value = float(self.perimeter)/2 - 4*float(self.surface)/(float(self.perimeter)*np.tan(float(self.angle1)*np.pi/360))
            latex = "a_{1} = \\frac {P} {2} - \\frac {2S\\cot(\\frac {{\\alpha}_{1}} {2}}} {P}"
            self.side1 = value
            return (value, latex)
        else:
            return ("Not enough information about the polygon!", "{}")

    def get_side2(self):
        if self.side2 is not None:
            return(self.side2, "{}")
        elif self.side1 is not None and self.side3 is not None and self.angle2 is not None:
            value = np.sqrt(float(self.side3)**2 + float(self.side1)**2 - 2*float(self.side3) * float(self.side1) * np.cos(float(self.angle2)*np.pi/180))
            latex = "a_{2} = \\sqrt {{a_{3}}^{2} + {a_{1}}^{2} - 2{a}_{3}{a}_{1} \\cos({\\alpha}_{2})}"
            self.side2 = value
            return (value, latex)
        elif self.side1 is not None and self.side3 is not None and self.angle1 is not None:
            angle3 = float(np.arcsin(float(self.side3)*np.sin(float(self.angle1)*np.pi/180)/float(self.side1))*180/np.pi)
            self.angle3 = angle3
            angle2 = float(180 - float(self.angle1) - angle3)
            self.angle2 = angle2
            value = np.sqrt(float(self.side3)**2 + float(self.side1)**2 - 2*float(self.side3)*float(self.side1) * (np.cos(angle2*np.pi/180)))
            latex = "{\\alpha}_{3} = \\arcsin(\\frac {a_{3} \\sin({\\alpha}_{1})} {a_{1}}) \\to {\\alpha}_{2} = 180 - {\\alpha}_{1} - {\\alpha}_{3} \\to a_{2} = \\sqrt{{a_{3}}^{2} + {a_{1}}^{2} - 2{a}_{3}{a}_{1} \\cos({\\alpha}_{2})}"
            self.side2 = value
            return (value, latex)
        elif self.side1 is not None and self.side3 is not None and self.angle3 is not None:
            angle1 = float(np.arcsin(float(self.side1)*np.sin(float(self.angle3)*np.pi/180)/float(self.side3))*180/np.pi)
            self.angle1 = angle1
            angle2 = float(180 - float(self.angle3) - angle1)
            self.angle2 = angle2
            value = np.sqrt(float(self.side3)**2 + float(self.side1)**2 - 2*float(self.side3)*float(self.side1) * (np.cos(angle2*np.pi/180)))
            latex = "{\\alpha}_{1} = \\arcsin(\\frac {a_{1} \\sin({\\alpha}_{3})} {a_{3}}) \\to {\\alpha}_{2} = 180 - {\\alpha}_{1} - {\\alpha}_{3} \\to a_{2} = \\sqrt{{a_{3}}^{2} + {a_{1}}^{2} - 2{a}_{3}{a}_{1} \\cos({\\alpha}_{2})}"
            self.side2 = value
            return (value, latex)
        elif self.angle2 is not None and self.angle3 is not None and self.side1 is not None:
            angle1 = float(180 - float(self.angle2) - float(self.angle3))
            self.angle1 = angle1
            value = float(self.side1)*np.sin(angle2*np.pi/180)/np.sin(float(self.angle1)*np.pi/180) # type: ignore
            latex = "{\\alpha}_{1} = 180 - {\\alpha}_{3} - {\\alpha}_{2} \\to a_{2} = \\frac {a_{1} \\sin({\\alpha}_{2})} {\\sin({\\alpha}_{1})}"
            self.side2 = value
            return (value, latex)
        elif self.angle1 is not None and self.angle3 is not None and self.side1 is not None:
            angle2 = float(180 - float(self.angle1) - float(self.angle3))
            self.angle2 = angle2
            value = float(self.side1)*np.sin(angle2*np.pi/180)/np.sin(float(self.angle1)*np.pi/180)
            latex = "{\\alpha}_{2} = 180 - {\\alpha}_{1} - {\\alpha}_{3} \\to a_{2} = \\frac {a_{1} \\sin({\\alpha}_{2})} {\\sin({\\alpha}_{1})}"
            self.side2 = value
            return (value, latex)
        elif self.angle1 is not None and self.angle2 is not None and self.side1 is not None:
            value = float(self.side1)*np.sin(angle2*np.pi/180)/np.sin(float(self.angle1)*np.pi/180) # type: ignore
            latex = "a_{2} = \\frac {a_{1} \\sin({\\alpha}_{2})} {\\sin({\\alpha}_{1})}"
            self.side2 = value
            return (value, latex)
        elif self.side3 is not None and self.perimeter is not None and self.side1 is not None:
            value = float(self.perimeter) - float(self.side1) - float(self.side3)
            latex = "a_{2} = P - a_{1} - a_{3}"
            self.side2 = value
            return (value, latex)
        elif self.angle3 is not None and self.surface is not None and self.side1 is not None:
            value = 2*float(self.surface)/(float(self.side1)*np.sin(float(self.angle3)*np.pi/180))
            latex = "a_{2} = \\frac {2S} {a_{1}\\sin({\\alpha}_{3})}"
            self.side2 = value
            return (value, latex)
        elif self.surface is not None and self.side1 is not None and self.angle1 is not None:
            b1 = np.sqrt((float(self.side1)**2 + 4*float(self.surface)/(np.tan(float(self.angle1)*np.pi/180)) + np.sqrt(float(self.side1)**4 + 8*float(self.side1)**2*float(self.surface)/(np.tan(float(self.angle1)*np.pi/180)) - 16*float(self.surface)**2))/2)
            b2 = np.sqrt((float(self.side1)**2 + 4*float(self.surface)/(np.tan(float(self.angle1)*np.pi/180)) - np.sqrt(float(self.side1)**4 + 8*float(self.side1)**2*float(self.surface)/(np.tan(float(self.angle1)*np.pi/180)) - 16*float(self.surface)**2))/2)
            if abs(complex(b1).imag) < 0.00000000000000001:
                value = b1
                latex = "a_{2} = \\sqrt {\\frac {{a_{1}}^{2} + 4S\\cot({\\alpha}_{1}) + \\sqrt {{a_{1}}^{4} + 8S{a_{1}}^{2}\\cot({\\alpha}_{1}) - 16S^{2}}} {2}}}"
                self.side2 = value
                return (value, latex)
            elif abs(complex(b2).imag) < 0.00000000000000001:
                value = b2
                latex = "a_{2} = \\sqrt {\\frac {{a_{1}}^{2} + 4S\\cot({\\alpha}_{1}) - \\sqrt {{a_{1}}^{4} + 8S{a_{1}}^{2}\\cot({\\alpha}_{1}) - 16S^{2}}} {2}}}"
                self.side2 = value
                return (value, latex)
            else:
                return("wft??!!", "{}")
        elif self.perimeter is not None and self.side1 is not None and self.angle1 is not None:
            angle2 = float(np.arcsin(np.sin(float(self.angle1)*np.pi/180)*(float(self.perimeter)/float(self.side1) - 1)/(2 * np.cos(float(self.angle1)*np.pi/360)))*180/np.pi - float(self.angle1)/2)
            self.angle2 = angle2
            value = float(self.side1) * np.sin(angle2*np.pi/180)/np.sin(float(self.angle1)*np.pi/180)
            latex = "{\\alpha}_{2} = \\arcsin(\\frac {\\sin({\\alpha}_{1})} {2\\cos(\\frac {{\\alpha}_{1}} {2})} (\\frac {P} {a_{1}} - 1)) - \\frac {{\\alpha}_{1}} {2} \\to a_{2} = \\frac {a_{1} \\sin({\\alpha}_{2}})} {\\sin({\\alpha}_{1})}"
            self.side2 = value
            return (value, latex)
        elif self.side1 is not None and self.surface is not None and self.side3 is not None:
            angle2 = float(np.arcsin(2*float(self.surface)/(float(self.side1)*float(self.side3)))*180/np.pi)
            self.angle2 = angle2
            value = np.sqrt(float(self.side3)**2 + float(self.side1)**2 - 2*float(self.side3) * float(self.side1) * np.cos(angle2*np.pi/180))
            latex = "{\\alpha}_{2} = \\arcsin(\\frac {2S} {a_{1}a_{3}}) \\to a_{2} = \\sqrt {{a_{3}}^{2} + {a_{1}}^{2} - 2{a}_{3}{a}_{1} \\cos({\\alpha}_{2})}"
            self.side2 = value
            return (value, latex)
        elif self.side1 is not None and self.surface is not None and self.side3 is not None:
            side3 = 2*float(self.surface)/(float(self.side1)*np.sin(float(self.angle2)*np.pi/180)) # type: ignore
            self.side3 = side3
            value = np.sqrt(side3**2 + float(self.side1)**2 - 2*side3 * float(self.side1) * np.cos(float(self.angle2)*np.pi/180)) # type: ignore
            latex = "a_{3} = \\arcsin(\\frac {2S} {a_{1}\\sin({\\alpha}_{2})}}) \\to a_{2} = \\sqrt {{a_{3}}^{2} + {a_{1}}^{2} - 2{a}_{3}{a}_{1} \\cos({\\alpha}_{2})}"
            self.side2 = value
            return (value, latex)
        elif self.perimeter is not None and self.side1 is not None and self.angle2 is not None:
            value = -(2*float(self.side1)*(float(self.side1) + (float(self.side1) - float(self.perimeter))*np.cos(float(self.angle2)*np.pi/180) - float(self.perimeter)) + float(self.perimeter)**2)/(2*(float(self.side1)*np.cos(float(self.angle2)*np.pi/180) + float(self.side1) - float(self.perimeter)))
            latex = "a_{2} = \\frac {2a_{1}(a_{1} + (a_{1} - P)\\cos({\\alpha}_{2}) - P) + {P}^{2}} {2(a_{1}\\cos({\\alpha}_{2}) + a_{1} - P)}"
            self.side2 = value
            return (value, latex)
        elif self.perimeter is not None and self.side1 is not None and self.angle3 is not None:
            value = (float(self.perimeter)*(2*float(self.side1) - float(self.perimeter)))/(2*(float(self.side1)*np.cos(float(self.angle3)*np.pi/180) + float(self.side1) - float(self.perimeter)))
            latex = "a_{2} = \\frac {P(2a_{1} - P)} {2(a_{1}\\cos({\\alpha}_{3}) + a_{1} - P)}}"
            self.side2 = value
            return (value, latex)
        elif self.side1 is not None and self.perimeter is not None and self.surface is not None:
            b1 = (3*float(self.side1)*float(self.perimeter) - float(self.perimeter)**2 -2*float(self.side1)**2 + np.sqrt((2*float(self.side1) - float(self.perimeter))*(2*float(self.side1)**3*float(self.perimeter) - float(self.perimeter)**2*float(self.side1)**2 + 16*float(self.surface)**2)/float(self.perimeter)))/(2*(2*float(self.side1) - float(self.perimeter)))
            b2 = (3*float(self.side1)*float(self.perimeter) - float(self.perimeter)**2 -2*float(self.side1)**2 - np.sqrt((2*float(self.side1) - float(self.perimeter))*(2*float(self.side1)**3*float(self.perimeter) - float(self.perimeter)**2*float(self.side1)**2 + 16*float(self.surface)**2)/float(self.perimeter)))/(2*(2*float(self.side1) - float(self.perimeter)))
            if b1>0:
                value = b1
                latex = "a_{2} = \\frac {3a_{1}P - P^{2} - 2{a_{1}}^{2} + \\sqrt {\\frac {(2a_{1} - P)(2{a_{1}}^{3}P - {a_{1}}^{2}P^{2} + 16S^{2})} {P}}} {2(2a_{1} - P)}"
                self.side2 = value
                return (value, latex)
            elif b2>0:
                value = b2
                latex = "a_{2} = \\frac {3a_{1}P - P^{2} - 2{a_{1}}^{2} - \\sqrt {\\frac {(2a_{1} - P)(2{a_{1}}^{3}P - {a_{1}}^{2}P^{2} + 16S^{2})} {P}}} {2(2a_{1} - P)}"
                self.side2 = value
                return (value, latex)
            else:
                return("wtf?!?!", "{}")
        else:
            return ("Not enough information about the polygon!", "{}") 

    def get_angle3(self):
        if self.angle3 is not None:
            return (self.angle3, "{}")
        elif self.side1 is not None and self.side2 is not None and self.side3 is not None:
            value = float(np.arccos((float(self.side1)**2 + float(self.side2)**2 - float(self.side3)**2)/(2*float(self.side1)*float(self.side2)))*180/np.pi)
            latex = "{\\alpha}_{3} = \\arccos(\\frac {{a_{1}}^{2} + {a_{2}}^{2} - {a_{3}}^{2}} {2a_{1}a_{2}})"
            self.angle3 = value
            return (value, latex)
        elif self.side1 is not None and self.side2 is not None and self.angle1 is not None:
            angle2 = float(np.arcsin(float(self.side2)*np.sin(float(self.angle1)*np.pi/180)/float(self.side1))*180/np.pi)
            self.angle2 = angle2
            value = 180 - float(self.angle1) - angle2
            latex = "{\\alpha}_{2} = \\arcsin(\\frac {a_{2}\\sin({\\alpha}_{1})} {a_{1}}) \\to {\\alpha}_{3} = 180 - {\\alpha}_{1} - {\\alpha}_{2}"
            self.angle3 = value
            return (value, latex)
        elif self.side1 is not None and self.side2 is not None and self.angle2 is not None:
            angle1 = float(np.arcsin(float(self.side1)*np.sin(float(self.angle2)*np.pi/180)/float(self.side2))*180/np.pi)
            self.angle1 = angle1
            value = 180 - float(self.angle2) - angle1
            latex = "{\\alpha}_{1} = \\arcsin(\\frac {a_{1}\\sin({\\alpha}_{2})} {a_{2}}) \\to {\\alpha}_{3} = 180 - {\\alpha}_{1} - {\\alpha}_{2}"
            self.angle3 = value
            return (value, latex)
        elif self.side1 is not None and self.surface is not None and self.side2 is not None:
            value = float(np.arcsin(2*float(self.surface)/(float(self.side1)*float(self.side2)))*180/np.pi)
            latex = "{\\alpha}_{3} = \\arcsin(\\frac {2S} {a_{1}a_{2}})"
            self.angle3 = value
            return (value, latex)
        elif self.side1 is not None and self.side2 is not None and self.perimeter is not None:
            side3 = float(self.perimeter) - float(self.side1) - float(self.side2)
            self.side3 = side3
            value = float(np.arccos((float(self.side1)**2 + float(self.side2)**2 - float(self.side3)**2)/(2*float(self.side1)*float(self.side2)))*180/np.pi)
            latex = "a_{3} = P - a_{1} - a_{2} \\to {\\alpha}_{3} = \\arccos(\\frac {{a_{1}}^{2} + {a_{2}}^{2} - {a_{3}}^{2}} {2a_{1}a_{2}})"
            self.angle3 = value
            return (value, latex)
        else:
            return ("Not enough information about the polygon!", "{}") 

    def get_side3(self):
        if self.side3 is not None:
            return (self.side3, "{}")
        else:
            try:
                side1, latex_s1 = self.get_side1()
                side2, latex_s2 = self.get_side2()
                angle3, latex_a3 = self.get_angle3()
                value = np.sqrt(side1**2 + side2**2 - 2*side1*side2*np.cos(angle3*np.pi/180))
                latex = latex_s1 + "\\to " + latex_s2 + "\\to " + latex_a3 + " \\to a_{3} = \\sqrt {{a_{1}}^{2} + {a_{2}}^{2} - 2a_{1}a_{2}\\cos({\\alpha}_{3})}"
                self.side3 = value
                return (value, latex)
            except TypeError:
                return ("Impossible polygon or not enough information!", "{}")

    def get_angle1(self):
        if self.angle1 is not None:
            return (self.angle1, "{}")
        else:
            try:
                side1, latex_s1 = self.get_side1()
                angle3, latex_a3 = self.get_angle3()
                side3, latex_s3 = self.get_side3()
                value = float(np.arcsin(side1*np.sin(angle3*np.pi/180)/side3)*180/np.pi)
                latex = latex_s1 + "\\to " + latex_a3 + "\\to " + latex_s3 + " \\to {\\alpha}_{1} = \\arcsin(\\frac{a_{1}\\sin({\\alpha}_{3})} {a_{3}})"
                self.angle1 = value
                return (value, latex)
            except TypeError:
                return ("Impossible polygon or not enough information!", "{}")

    def get_angle2(self):
        if self.angle2 is not None:
            return (self.angle2, "{}")
        else:
            try:
                side2, latex_s2 = self.get_side2()
                angle3, latex_a3 = self.get_angle3()
                side3, latex_s3 = self.get_side3()
                value = float(np.arcsin(side2*np.sin(angle3*np.pi/180)/side3)*180/np.pi)
                latex = latex_s2 + "\\to " + latex_a3 + "\\to " + latex_s3 + " \\to {\\alpha}_{2} = \\arcsin(\\frac{a_{2}\\sin({\\alpha}_{3})} {a_{3}})"
                self.angle2 = value
                return (value, latex)
            except TypeError:
                return ("Impossible polygon or not enough information!", "{}")

    def get_perimeter(self):
        if self.perimeter is not None:
            return (self.perimeter, "{}")
        else:
            try:
                side1, latex_s1 = self.get_side1()
                side2, latex_s2 = self.get_side2()
                side3, latex_s3 = self.get_side3()
                value = float(side1 + side2 + side3) # type: ignore
                latex = latex_s1 + "\\to " + latex_s2 + "\\to " + latex_s3 + " \\to P = a_{1} + a_{2} + a_{3}"
                self.perimeter = value
                return (value, latex)
            except TypeError:
                return ("Impossible polygon or not enough information!", "{}")

    def get_surface(self):
        if self.surface is not None:
            return (self.surface, "{}")
        else:
            try:
                side1, latex_s1 = self.get_side1()
                side2, latex_s2 = self.get_side2()
                angle3, latex_a3 = self.get_angle3()
                value = side1*side2*np.sin(angle3*np.pi/180)/2 # type: ignore
                latex = latex_s1 + "\\to " + latex_s2 + "\\to " + latex_a3 + " \\to S = \\frac {a_{1}a_{2}\\sin({\\alpha}_{3})} {2}"
                self.side3 = value
                return (value, latex)
            except TypeError:
                return ("Impossible polygon or not enough information!", "{}")

    def get_parameters(self):
        triangle_value = []
        triangle_latex = []
        try:
            triangle_info = [self.get_angle1(), self.get_angle2(), self.get_angle3(), self.get_side1(), self.get_side2(), self.get_side3(), self.get_perimeter(), self.get_surface()]
            triangle_info = [(float(i[0]), i[1]) for i in triangle_info]
            for i in triangle_info:    
                if type(i[0]) == type(0.1):
                    triangle_value.append(round(i[0], self.n))
                    triangle_latex.append(i[1])
                    continue
                else:
                    return ("Not enough information about the polygon!", "{}")    
            return (triangle_value, triangle_latex)
        except TypeError:
            return ("Not enough information about the polygon!", "{}")

class irregular_polygon:
    def __init__(self, points, perimeter=None, surface=None, n=2):
        self.name = "Irregular Polygon"
        self.size = len(points)
        self.points = points
        self.perimeter = perimeter
        self.surface = surface
        self.n = n

    def get_perimeter(self):
        for i, point in enumerate(self.points):
            x0, y0 = point
            x1, y1 = self.points[(i+1)%self.size]
            x_1, y_1 = self.points[(i-1)%self.size]
