#include <iostream>
#include <math.h>
#include <cmath>
using namespace std;
double f(double n) 
{
    if (n == 0) return 1;
    else if (n == 1) return 1;
    else return f(n - 1) + f(n - 2);
}
double fib(double x)
{
    return 2 * x * x - 2 * x + 2.5;
}
int main()
{
    setlocale(LC_ALL, "rus");
    double a = -1, b = 9;
    double delta = 0.5;
    double eps = 0.2;
    int iter = 0;
    double n = abs(b - a) / (2*delta);
    double y = a + f(n - 1) / f(n) * (b - a);
    double x = a + f(n - 2) / f(n) * (b - a);
    while(iter!=n-3)
    {
        
        
        if (fib(x) <= fib(y))
        {
            b = y;
            y = x;
            x = a + f(n - iter - 3) / f(n - iter - 1) * (b - a);
        }
        else
        {
            a = x;
            x = y;
            y = a + f(n - iter - 2) / f(n - iter - 1) * (b - a);
        }
        iter += 1;
    }
    x = (a + b) / 2;
    y = x + eps;
    if (fib(x) <= fib(y)) b = y;
    else a = x;
    double x_min = (a + b) / 2;
    double sh = 1 / f(n);
    cout << "Искомая точка минимума: " << x_min << endl;
    cout << "На промежутке: [" << a << "; " << b << "]" << endl;
    cout << "Значение функции в точке минимума: " << fib(x_min) << endl;
    cout << "Количество итераций: " << iter << endl;
    cout << "Сходимость: " << sh << endl;
    system("pause");
}