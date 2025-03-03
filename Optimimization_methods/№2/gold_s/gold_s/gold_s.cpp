#include <iostream>
#include <math.h>
#include <cmath>
using namespace std;

double gold(double x)
{
    return 2 * x * x - 2 * x + 2.5;
}
int main()
{
    setlocale(LC_ALL, "rus");
    const double o = 0.38196;
    const double delta = 0.25;
    int iter = 0;
    double a = -1, b = 9;
    double x = a + o * (b - a);
    double y = a + b - x;
    while (abs(a - b) > delta)
    {
        if (gold(x) <= gold(y))
        {
            b = y;
            y = x;
            x = a + b - x;
        }
        else 
        {
            a = x;
            x = y;
            y = a + b - y;
        }
        iter += 1;
    }
    double x_min = (a + b) / 2;
    double sh = pow(0.618, iter - 1);
    cout << "Искомая точка минимума: " << x_min << endl;
    cout << "На промежутке: [" << a << "; " << b << "]" << endl;
    cout << "Значении функции в точке минимума: " << gold(x_min) << endl;
    cout << "Сходимость: " << sh << endl;
    cout << "Количество итераций: " << iter << endl;
    system("pause");
}