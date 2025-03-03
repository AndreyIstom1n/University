#include <iostream>
#include <cmath>
#include <math.h>
using namespace std;
double func(double x1, double x2)
{
	return 8 * pow(x1, 2) + pow(x2, 2) - x1 * x2 + x1;
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
	double norma = pow(x1, 2) + pow(x2, 2);
	return sqrt(norma);
}

void obrmatr(double** A, double** B, int n) {
	for (int k = 0; k < n; ++k)
	{
		double div = A[k][k];

		for (int j = 0; j < n; ++j)
		{
			A[k][j] /= div;
			B[k][j] /= div;
		}

		for (int i = k + 1; i < n; ++i)
		{
			double multi = A[i][k];
			for (int j = 0; j < n; ++j)
			{
				A[i][j] -= multi * A[k][j];
				B[i][j] -= multi * B[k][j];
			}
		}
	}

	for (int k = n - 1; k > 0; --k)
	{
		for (int i = k - 1; i >= 0; --i)
		{
			double multi = A[i][k];
			for (int j = 0; j < n; ++j)
			{
				A[i][j] -= multi * A[k][j];
				B[i][j] -= multi * B[k][j];
			}
		}
	}
}

int main() {
	setlocale(LC_ALL, "rus");
	int m = 50, it = 0;
	double eps1 = 0.1, eps2 = 0.15, x, y, t, x01, y01, x00, y00, d1, d2;
	x00 = x01 = 2, y00 = y01 = 2;
	double** H = new double* [2];
	for (int i = 0; i < 2; i++) {
		H[i] = new double[2];
	}
	double** H1 = new double* [2];
	for (int j = 0; j < 2; j++) {
		H1[j] = new double[2];
	}
	H[0][0] = 16.0, H[0][1] = -1.0, H[1][0] = -1.0, H[1][1] = 2.0;
	H1[0][0] = 1.0, H1[0][1] = 0.0, H1[1][0] = 0.0, H1[1][1] = 1.0;
	obrmatr(H, H1, 2);
	for (int i = 0; i < m; i++) 
	{
		//double z = norma(fx1(x01, y01), fx2(x01, y01));
		//cout << z << endl;
		if (norma(fx1(x01, y01), fx2(x01, y01)) < eps1)
			break;
		d1 = -H1[0][0] * fx1(x01, y01) - H1[0][1] * fx2(x01, y01);
		d2 = -H1[1][0] * fx1(x01, y01) - H1[1][1] * fx2(x01, y01);
		x = x01 + d1;
		y = y01 + d2;

		if (norma(x - x01, y - y01) < eps2 && fabs(func(x, y) - func(x01, y01)) < eps2 &&
			norma(x01 - x00, y01 - y00) < eps2 && fabs(func(x01, y01) - func(x00, y00)) < eps2) {
			x01 = x;
			y01 = y;
			it++;
			break;
		}
		x00 = x01, y00 = y01;
		x01 = x, y01 = y;
		it++;
	}
	
	cout << "Количетсво итераций: " << it << endl;
	cout << "Искомая точка минимума = (" << x01 << "; " << y01<<")" << endl;
	cout << "Значение функции в точке минимума = " << func(x01, y01) << endl;
	system("pause");
}