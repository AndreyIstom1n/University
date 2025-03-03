#include <iostream>
#include <math.h>
#include <cmath>
using namespace std;

double dych(double x)
{   
    return 2*x*x-2*x+2.5;
}

int main()
{
    setlocale(LC_ALL, "rus");
    double a = -1, b = 9;
    const double eps = 0.2;     
    const double delta = 0.5;
    int iter = 0;                       

    while (abs(b - a) > (delta*2))
    {
        iter += 1;
        double x = ((a + b) / 2) - (eps/2);
        double y = ((a + b) / 2) + (eps/2);
        
        if (dych(x) > dych(y))
            a = x;
        else b = y;
        
        //cout <<"a: "<< a << endl <<"b: "<< b << endl;
    }

    double s = 1 / (pow(2, iter / 2));
    double x_min = (a + b) / 2;
    cout << "Искомая точка минимума: " << x_min << endl;
    cout << "На промежутке: [" << a << "; " << b <<"]"<< endl;
    cout << "Значение функции в точке минимума: " << dych(x_min) << endl;
    cout << "Количество итераций: " << iter << endl;
    cout << "Сходимость: " << s << endl;
    system("pause");
}