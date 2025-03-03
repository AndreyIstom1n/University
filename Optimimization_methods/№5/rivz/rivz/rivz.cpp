#include <iostream>
#include <cmath>
#include <math.h>
double func(double x1, double x2) 
{
	return 8*pow(x1, 2) + pow(x2, 2) - x1 * x2 + x1;
}

double fx1(double x1, double x2) 
{
	return 16 * x1 - x2 + 1;
}

double fx2(double x1, double x2) 
{
	return 2 * x2-x1;
}

double norma(double x1, double x2) 
{
	double norma = pow(x1, 2) + pow(x2, 2);
	return sqrt(norma);
}

double gold(double x1, double x2, double t) 
{ 
	return func(x1 - t * fx1(x1, x2), x2 - t * fx2(x1, x2));
}

double gold_sech(double x1, double x2) 
{  
	double a = -1;
	double b = 1;
	double k = 0.38196;
	double delta = 0.05;
	double t1 = a + k * (b - a);
	double t2 = a + b - t1;
	do {
		if (gold(x1, x2, t1) <= gold(x1, x2, t2)) {
			b = t2;
			t2 = t1;
			t1 = a + b - t2;
		}
		else {
			a = t1;
			t1 = t2;
			t2 = a + b - t1;
		}
	} while (fabs(b - a) > delta);
	return (b + a) / 2;
}
using namespace std;
int main() 
{
	setlocale(LC_ALL, "rus");
	int m = 50, it = 1;
	double eps1 = 0.01, eps2 = 0.015;
	double x1, x2, x0, x20, t, x01, x202, x00, x200, d1, d2, d10, d20, beta;
	x00 = x01 = 2.0, x200 = x202 = 2.0;
	t = gold_sech(x00, x200);
	x0 = x00 - t * fx1(x00, x200);
	x20 = x200 - t * fx2(x00, x200);
	d10 = -fx1(x0, x20);
	d20 = -fx2(x0, x20);
	for (int i = 1; i < m; i++) 
	{
		cout << it << "Итерация" << endl;
		if (norma(fx1(x0, x20), fx2(x0, x20)) < eps1)
			break;
		beta = pow(norma(fx1(x0, x20), fx2(x0, x20)), 2) / pow(norma(fx1(x01, x202), fx2(x01, x202)), 2);
		d1 = -fx1(x0, x20) + beta * d10;
		d2 = -fx2(x0, x20) + beta * d20;
		t = gold_sech(x0, x20);
		x1 = x0 + t * d1;
		x2 = x20 + t * d2;
		if (norma(x1 - x0, x2 - x20) < eps2 && fabs(func(x1, x2) - func(x0, x20)) < eps2 && norma(x0 - x01, x20 - x202) < eps2 && fabs(func(x0, x20) - func(x01, x202)) < eps2) 
		{
			x0 = x1;
			x20 = x2;
			it++;
			break;
		}
		d10 = d1;
		d20 = d2;
		x01 = x0, x202 = x20;
		x0 = x1, x20 = x2;
		it++;
		cout << x0<< " " << x20 << endl;
	}

	double Gesse[2][2];
	Gesse[0][0] = 16.0, Gesse[0][1] = -1.0, Gesse[1][0] = -1.0, Gesse[1][1] = 2.0;
	double l1 = (Gesse[0][0] + Gesse[1][1] + sqrt(pow((Gesse[0][0] + Gesse[1][1]), 2) - 4 * (Gesse[0][0] * Gesse[1][1] - Gesse[0][1] * Gesse[1][0]))) / 2;
	double l2 = (Gesse[0][0] + Gesse[1][1] - sqrt(pow((Gesse[0][0] + Gesse[1][1]), 2) - 4 * (Gesse[0][0] * Gesse[1][1] - Gesse[0][1] * Gesse[1][0]))) / 2;
	if (l1 > l2) 
	{
		double c = l1;
		l1 = l2;
		l2 = c;
	}

	double shod = (pow((l1 / l2 - 1), 2)) / (pow((l1 / l2 + 1), 2));
	double skor = pow((norma(x0 - x01, x20 - x202) / norma(x01 - x00, x202 - x200)), it / 2);

	cout << "Количество итераций: " << it-1 << endl;
	cout << "Искомая точка минимума: (" << x0 << "; " << x20 << ")" << endl;
	cout << "Значение функции в точке минимума: " << func(x0, x20) << endl;
	cout << "Показатель величины бета: " << beta << endl;
	system("pause");
}