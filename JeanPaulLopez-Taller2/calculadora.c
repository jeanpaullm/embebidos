#include <stdio.h>
#include <biblioteca.h>

int main() {

	double a,b,c;
        
        a = 10; 
        b = 16;
        c = suma(a,b);
        
	printf("Suma: %.0f + %.0f = %.0f\n", a, b, c);

	a = 54; 
        b = 67;
        c = resta(a,b);
        
	printf("Resta: %.0f + %.0f = %.0f\n", a, b, c);

	a = 134; 
        b = 32;
        c = division(a,b);
        
	printf("Division: %.0f + %.0f = %.0f\n", a, b, c);

	a = 11; 
        b = 17;
        c = multiplicacion(a,b);
        
	printf("Multiplicacion: %.0f + %.0f = %.0f\n", a, b, c);

	a = 110;
        c = raizCuadrada(a);
        
	printf("Raiz cuadrada: sqrt(%.0f) = %.2f\n", a, c);


	return 0;

}
