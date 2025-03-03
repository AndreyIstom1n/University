#include <iostream>
#include <cmath>
#include <math.h>
using namespace std;
double func(double x1, double x2)
{
	return 8 * x1 * x1 + x2 * x2 - x1 * x2 + x1;
}
double fx1(double x1, double x2)
{
	return 16 * x1 - x2 + 1;
}
double fx2(double x1, double x2)
{
	return 2 * x2 - x1;
}
double norma(double x1, double x2)
{
	double norma = x1 * x1 + x2 * x2;
	return sqrt(norma);
}
double ft(double x1, double x2,double t)
{
	return func(x1 - t * fx1(x1, x2), x2 - t * fx2(x1, x2));
}
double gold(double x1, double x2)
{
	double a = -1.0, b = 1.0;
	double o = 0.38196;
	double delta = 0.05;
	double t1 = a + o * (b - a);
	double t2 = a + b - t1;
	do
	{
		if (ft(x1, x2, t1) <= ft(x1, x2, t2))
		{
			b = t2;
			t2 = t1;
			t1 = a + b - t2;
		}
		else
		{
			a = t1;
			t1 = t2;
			t2 = a + b - t1;
		}
	} while (fabs(b - a) > delta);
	return (b + a) / 2;
}
int main()
{
	setlocale(LC_ALL, "rus");
	int k = 1, m = 50;
	double eps1 = 0.01, eps2 = 0.015, x1, x2, x10 = 2.0, x20 = 2.0, t;
	for (int i = 0; i < m; i++)
	{
		if (norma(fx1(x10, x20), fx2(x10, x20)) < eps1)
			break;
		t = gold(x10, x20);
		x1 = x10 - t * fx1(x10, x20);
		x2 = x20 - t * fx2(x10, x20);
		if (norma(x1 - x10, x2 - x20) < eps2 && fabs(func(x1, x2) - func(x10, x20)) < eps2)
			break;
		x10 = x1, 
		x20 = x2;
		cout << k << " - итерация, " << endl;
		cout<< x10 << " " << x20 << " - значения" << endl;
		k++;
	}
	cout << k << " - итерация, " << endl;
	cout << x10 << " " << x20 << " - значения" << endl;

	cout << "Искомая точка минимума: " << "(" << x10 << "; " << x20 << ")" << endl;
	cout << "Значение функции в точке минимума: " << func(x10, x20) << endl;
	cout << "Количество итераций: " << k << endl;
	system("pause");
}
