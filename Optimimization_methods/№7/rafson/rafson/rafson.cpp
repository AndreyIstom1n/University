#include <iostream>
#include <cmath>
#include <math.h>

using namespace std;

double func(double x, double y) {
	return 8*pow(x, 2) +  pow(y, 2) - x * y + x;
}

double fx1(double x, double y) {
	return 16 * x - y + 1;
}

double fx2(double x, double y) {
	return 2 * y - x;
}

double norma(double x, double y) {
	double l = pow(x, 2) + pow(y, 2);
	return sqrt(l);
}

void obrat(double** A, double** B, int n) {
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

double get_t(double x, double y, double t) {  
	return func(x - t * fx1(x, y), y - t * fx2(x, y));
}

double gold(double x, double y) {  
	double a = -1;
	double b = 1;
	double k = 0.38196;
	double l = 0.01;
	double t1 = a + k * (b - a);
	double t2 = a + b - t1;
	do {
		if (get_t(x, y, t1) <= get_t(x, y, t2)) {
			b = t2;
			t2 = t1;
			t1 = a + b - t2;
		}
		else {
			a = t1;
			t1 = t2;
			t2 = a + b - t1;
		}
	} while (fabs(b - a) > l);
	return (b + a) / 2;
}


int main() {
	setlocale(LC_ALL, "rus");
	int m = 50, it = 0;
	double eps1 = 0.001, eps2 = 0.0015;
	double x, y, t, x01, y01, x00, y00, d1, d2, x0, y0, X0, Y0;

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
	obrat(H, H1, 2); 

	x00 = x01 = x0 = 2, y00 = y01 = y0 = 2;
	if (H1[0][0] > 0 && (H1[0][1] < 0)) {
		for (int i = 0; i < m; i++) {
			if (norma(fx1(x01, y01), fx2(x01, y01)) < eps1)
				break;
			d1 = -H1[0][0] * fx1(x01, y01) - H1[0][1] * fx2(x01, y01);
			d2 = -H1[1][0] * fx1(x01, y01) - H1[1][1] * fx2(x01, y01);
			t = gold(x01, y01);
			x = x01 + t * d1;
			y = y01 + t * d2;
			if (norma(x - x01, y - y01) < eps2 && fabs(func(x, y) - func(x01, y01)) < eps2 && 
				norma(x01 - x00, y01 - y00) < eps2 && fabs(func(x01, y01) - func(x00, y00)) < eps2) {
				x01 = x;
				y01 = y;
				it++;
				break;
			}
			x00 = x01, y00 = y01;
			x01 = x, y01 = y;
			if (i == 0) {
				X0 = x01;
				Y0 = y01;
			}
			//cout <<"it "<<it << " " << x01 << " " << y01 << endl;
			it++;
		}
	}

	else {
		for (int i = 0; i < m; i++) {
			if (norma(fx1(x01, y01), fx2(x01, y01)) < eps1)
				break;
			d1 = -fx1(x01, y01);
			d2 = -fx2(x01, y01);
			t = gold(x01, y01);
			x = x01 + t * d1;
			y = y01 + t * d2;
			if (norma(x - x01, y - y01) < eps2 && fabs(func(x, y) - func(x01, y01)) < eps2 && norma(x01 - x00, y01 - y00) < eps2 && fabs(func(x01, y01) - func(x00, y00)) < eps2) {
				x01 = x;
				y01 = y;
				it++;
				break;
			}
			x00 = x01, y00 = y01;
			x01 = x, y01 = y;
			if (i == 0) {
				X0 = x01;
				Y0 = y01;
			}
			//cout << "1it " << it <<" "<< x01 << " " << y01 << endl;
			it++;
		}
	}
	double m1;

	double l1 = (H[0][0] + H[1][1] + sqrt(pow((H[0][0] + H[1][1]), 2) - 4 * (H[0][0] * H[1][1] - H[0][1] * H[1][0]))) / 2;
	double l2 = (H[0][0] + H[1][1] - sqrt(pow((H[0][0] + H[1][1]), 2) - 4 * (H[0][0] * H[1][1] - H[0][1] * H[1][0]))) / 2;

	if (l1 >= l2)
		m1 = l2;
	else
		m1 = l1;

	bool flag = false;
	if (pow(norma(x01 - x0, y01 - y0), 2) / m1 >= norma(X0 - x0, Y0 - y0))
		flag = true;

	cout << "Количество итераций: " << it << endl;
	cout << "Искомая точка минимума x* : = (" << x01 << "; " << y01 << ")"<<endl;
	cout << "Значение функции в точке минимума: " << func(x01, y01) << endl;
	if (flag)
		cout << "Сходится к точке минимума с квадратичной скоростью." << endl;
	return 0;
}