#include <stdio.h>
#include <math.h>

int main() {
    // Point on line P(1,-1,0)
    double x1 = 1, y1 = -1, z1 = 0;

    // Plane coefficients: x - y + 4z = 5
    double A = 1, B = -1, C = 4, D = 5;

    // Distance formula
    double numerator = fabs(A*x1 + B*y1 + C*z1 - D);
    double denominator = sqrt(A*A + B*B + C*C);
    double distance = numerator / denominator;

    printf("Distance of line from plane = %lf\n", distance);

    return 0;
}