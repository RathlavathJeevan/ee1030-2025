#include <stdio.h>
#include <math.h>

// Function to find perpendicular foot from point (x0,y0) to line ax+by+c=0
void perpendicularFoot(double a, double b, double c, double x0, double y0, double *x, double *y) {
    double d = (a*x0 + b*y0 + c) / (a*a + b*b);
    *x = x0 - a*d;
    *y = y0 - b*d;
}

int main() {
    // Coordinates of A, B, C
    double Ax = 6, Ay = 0;
    double Bx = 0, By = 0;
    double Cx = 0, Cy = 8;

    // Line AC: equation ax + by + c = 0
    double a = Cy - Ay;    // y2 - y1
    double b = Ax - Cx;    // x1 - x2
    double c = (Cx*Ay - Ax*Cy);

    // Find D (perpendicular foot from B onto AC)
    double Dx, Dy;
    perpendicularFoot(a, b, c, Bx, By, &Dx, &Dy);

    printf("Coordinates of A(%.2f, %.2f)\n", Ax, Ay);
    printf("Coordinates of B(%.2f, %.2f)\n", Bx, By);
    printf("Coordinates of C(%.2f, %.2f)\n", Cx, Cy);
    printf("Coordinates of D(%.2f, %.2f)\n", Dx, Dy);

    // Circle through B, C, D can be found by determinant method
    // Equation: x^2 + y^2 + gx + fy + c = 0
    // Solve system using B(0,0), C(0,8), D(xd,yd)

    double g, f, cc;
    // Substitute B(0,0) => 0 + 0 + 0 + 0 + c = 0 => c = 0
    cc = 0;

    // Using C(0,8): 0 + 64 + 0 + 8f + c = 0 => 64 + 8f = 0 => f = -8
    f = -8;

    // Using D(xd,yd)
    // xd^2 + yd^2 + g*xd + f*yd + c = 0
    g = -(Dx*Dx + Dy*Dy + f*Dy) / Dx;

    printf("Equation of circle: x^2 + y^2 + %.2fx + %.2fy = 0\n", g, f);

    // Equation of tangents from A(x1,y1) to circle:
    // xx1 + yy1 + (g/2)(x + x1) + (f/2)(y + y1) + c = 0
    // But we can print general form
    printf("Tangents from A(%.2f, %.2f) can be derived using substitution in circle equation.\n", Ax, Ay);

    return 0;
}