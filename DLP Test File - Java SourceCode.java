// Confidential: Internal use only. Do not distribute.

public class ConfidentialCalculator {

    public static double calculateBonus(double baseSalary) {
        // Confidential formula: Base salary * 20% bonus
        return baseSalary * 0.20;
    }

    public static void main(String[] args) {
        double salary = 60000;
        double bonus = calculateBonus(salary);
        System.out.println("Confidential: The calculated bonus is $" + bonus);
    }
}
