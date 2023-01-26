public class Complex {
    int real;
    int imaginary;
    Complex(int real, int imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    static String toString(Complex c) {
        boolean hasRealPart = c.real != 0;
        boolean hasImaginaryPart = c.imaginary != 0;
        String divider = "";
        if (hasRealPart && hasImaginaryPart && c.imaginary > 0) {
            divider = "+";
        }
        String realPart = hasRealPart ? c.real + "" : "";
        String imaginaryPart = hasImaginaryPart ? c.imaginary + "i" : "";
        if (c.imaginary == 1 || c.imaginary == -1) {
            imaginaryPart = imaginaryPart.replace("1", "");
        }
        return realPart + divider + imaginaryPart;
    }

    static Complex parseComplex(String complexString) {
        int[] complexNumber = new int[2];
        char[] complexChars = complexString.toCharArray();
        int part = 0, pow = 0;
        for (int i = complexString.length() - 1; i >= 0; i--) {
            char ch = complexChars[i];
            if (ch == 'i') {
                complexNumber[1] = 1;
                part = 1;
                continue;
            }
            if (ch == '+' || ch == '-') {
                if (ch == '-') {
                    complexNumber[part] *= (-1);
                }
                pow = 0;
                part = 0;
                continue;
            }
            complexNumber[part] += Integer.parseInt(ch + "") * Math.pow(10, pow);
            pow++;
        }
        if (complexNumber[1] > 1) {
            complexNumber[1] -= 1;
        } else if (complexNumber[1] < -1) {
            complexNumber[1] += 1;
        }
        return new Complex(complexNumber[0], complexNumber[1]);
    }

    Complex multiply(Complex c) {
        int real = (this.real * c.real) + (-1) * (this.imaginary * c.imaginary);
        int imaginary = (this.real * c.imaginary) + (this.imaginary * c.real);
        return new Complex(real, imaginary);
    }

    Complex add(Complex c) {
        return new Complex(this.real + c.real, this.imaginary + c.imaginary);
    }

    Complex divide(Complex c) {
        Complex conjugate = c.conjugate();
        Complex numerator = this.multiply(conjugate);
        Complex denominator = c.multiply(conjugate);
        int real = numerator.real / denominator.real;
        int imaginary = numerator.imaginary / denominator.real;
        return new Complex(real, imaginary);
    }

    Complex conjugate () {
        return new Complex(this.real, (-1) * this.imaginary);
    }

    public static void main(String[] args) {
        Complex c = new Complex(2, 3);
        Complex d = new Complex(4, -2);
        System.out.println(Complex.toString(c.multiply(d)));
    }
}
