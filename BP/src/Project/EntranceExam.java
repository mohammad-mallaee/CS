import java.text.DecimalFormat;
import java.util.Scanner;

public class EntranceExam {
    static Scanner reader = new Scanner(System.in);

    public static void main(String[] args) {
        int index = -1;
        int command;
        System.out.println("\n|--> This program is written by mohammad mallaee <--|");
        System.out.print("\nEnter the number of students: ");
        Student[] students = new Student[reader.nextInt()];
        while (true) {
            showMenu();
            System.out.print("\nchoose one of the options: ");
            command = reader.nextInt();
            switch (command) {
                case 1:
                    if (index == students.length - 1) {
                        System.out.println("\nyou reached the maximum number of users!");
                        break;
                    }
                    index++;
                    students[index] = new Student(index);
                    String name = students[index].first + " " + students[index].last;
                    System.out.println("The score of " + name + " is " + students[index].getFormattedScore());
                    break;
                case 2:
                    System.out.print("\nstudent's index: ");
                    int studentIndex = reader.nextInt();
                    if (students[studentIndex] == null || students[studentIndex].index == -1) {
                        System.out.println("couldn't find the student.");
                        break;
                    }
                    students[studentIndex].printInfo();
                    break;
                case 3:
                    editInfo(students);
                    break;
                case 4:
                    deleteStudent(students);
                    break;
                case 5:
                    displayWinners(students);
                    break;
                case 6:
                    return;
                default:
                    System.out.println("invalid option");
            }
        }
    }

    static void showMenu() {
        String options = "\n-- Main Menu --"
                + "\n1.add student"
                + "\n2.display information by index"
                + "\n3.edit information"
                + "\n4.delete"
                + "\n5.winners"
                + "\n6.exit";
        System.out.println(options);
    }

    static void editInfo(Student[] students) {
        System.out.print("student's index: ");
        int index = reader.nextInt();
        if (students[index] == null || students[index].index == -1) {
            System.out.println("couldn't find the student.");
            return;
        }
        Student student = students[index];
        while (true) {
            student.printEditOptions();
            System.out.print("\nwhich option do you want to edit: ");
            int option = reader.nextInt();
            student.editInfo(option);
            student.calculateScore();
            System.out.println("\nDone Successfully!");
            student.printInfo();
            System.out.print("\ndo you want to continue editing (y/n): ");
            String confirmString = reader.next();
            if (confirmString.equalsIgnoreCase("n")) {
                break;
            } else if (!confirmString.equalsIgnoreCase("y")) {
                System.out.println("invalid option!");
            }
        }
    }

    static void deleteStudent(Student[] students) {
        System.out.print("student's index: ");
        int index = reader.nextInt();
        Student student = students[index];
        if (student == null || student.index == -1) {
            System.out.println("couldn't find the student!");
            return;
        }
        System.out.print("do you want to delete the student index " + index + " (" + student.first + " " + student.last + ")? (y/n) ");
        String confirmString = reader.next();
        if (confirmString.equalsIgnoreCase("n")) {
            return;
        } else if (!confirmString.equalsIgnoreCase("y")) {
            System.out.println("invalid option!");
            return;
        }
        student.delete();
        System.out.println("deleted the student successfully.");
    }

    static void displayWinners(Student[] students) {
        Student[] winners = new Student[3];
        for (Student student : students) {
            if (student == null) break;
            for (int j = 0; j < winners.length; j++) {
                if (winners[j] == null) {
                    winners[j] = student;
                    break;
                }
                if (student.score > winners[j].score) {
                    winners[j] = student;
                    for (int k = j + 1; k < winners.length - 1; k++) {
                        winners[k + 1] = winners[k];
                    }
                }
            }
        }
        System.out.println("\n-- Winners:");
        for (int i = 0; i < winners.length; i++) {
            if (winners[i] != null && winners[i].index != -1) {
                String name = winners[i].first + " " + winners[i].last;
                System.out.println((i + 1) + ". " + name + ": " + winners[i].getFormattedScore());
            }
        }
    }
}

class Student {
    String first, last, nationalCode, studentCode, sex;
    int index, mathScore, englishScore, bpScore, age;
    double gpa, score;
    DecimalFormat df = new DecimalFormat();

    Student(int index) {
        this.index = index;
        Scanner reader = new Scanner(System.in);
        System.out.println("\nPlease enter the information of student number " + index + ":");
        System.out.print("first name: ");
        first = reader.nextLine();
        System.out.print("last name: ");
        last = reader.nextLine();
        System.out.print("national code: ");
        nationalCode = reader.nextLine();
        System.out.print("student code: ");
        studentCode = reader.nextLine();
        System.out.print("sex: ");
        sex = reader.nextLine();
        System.out.print("math score: ");
        mathScore = reader.nextInt();
        System.out.print("english score: ");
        englishScore = reader.nextInt();
        System.out.print("basic programming score: ");
        bpScore = reader.nextInt();
        System.out.print("age: ");
        age = reader.nextInt();
        this.calculateScore();
    }

    void calculateScore() {
        this.gpa = (this.mathScore + this.englishScore + this.bpScore) / 3.0;
        double score = this.gpa - findVariant(this);
        score = score * 0.9 + this.gpa * 0.5;
        score -= Math.abs(19 - this.age);
        this.score = score;
    }

    String getFormattedScore() {
        df.setMaximumFractionDigits(2);
        return df.format(this.score);
    }

    static double findVariant(Student student) {
        double gpa = student.gpa;
        int mathScore = student.mathScore;
        int englishScore = student.englishScore;
        int bpScore = student.mathScore;
        double distance = Math.pow(mathScore - gpa, 2)
                + Math.pow(englishScore - gpa, 2)
                + Math.pow(bpScore - gpa, 2);
        return Math.sqrt(0.5 * distance);
    }

    void delete() {
        index = -1;
        mathScore = 0;
        englishScore = 0;
        bpScore = 0;
        age = 0;
        gpa = 0;
        score = 0;
        first = "";
        last = "";
        nationalCode = "";
        studentCode = "";
        sex = "";
    }

    void printInfo() {
        df.setMaximumFractionDigits(2);
        String out = "\nstudent " + index + " information :"
                + "\nfirst name: " + first
                + "\nlast name: " + last
                + "\nnational code: " + nationalCode
                + "\nstudent code: " + studentCode
                + "\nsex: " + sex
                + "\nmath score: " + mathScore
                + "\nenglish score: " + englishScore
                + "\nbasic programming score: " + bpScore
                + "\nage: " + age
                + "\ngrade point average: " + df.format(gpa)
                + "\nscore: " + this.getFormattedScore();
        System.out.println(out);
    }

    void printEditOptions() {
        String editOptions = "\nediting " + first + " " + last + "'s information: "
                + "\n1.first name        2.last name"
                + "\n3.national code     4.student code"
                + "\n5.sex               6.math score"
                + "\n7.english score     8.basic programming score"
                + "\n9.age               10.grade point average"
                + "\n11.score";
        System.out.println(editOptions);
    }

    void editInfo(int option) {
        Scanner reader = new Scanner(System.in);
        System.out.print("write the new value: ");
        switch (option) {
            case 1:
                this.first = reader.nextLine();
                break;
            case 2:
                this.last = reader.nextLine();
                break;
            case 3:
                this.nationalCode = reader.nextLine();
                break;
            case 4:
                this.studentCode = reader.nextLine();
                break;
            case 5:
                this.sex = reader.nextLine();
                break;
            case 6:
                this.mathScore = reader.nextInt();
                break;
            case 7:
                this.englishScore = reader.nextInt();
                break;
            case 8:
                this.bpScore = reader.nextInt();
                break;
            case 9:
                this.age = reader.nextInt();
                break;
            case 10:
                this.gpa = reader.nextDouble();
                break;
            case 11:
                this.score = reader.nextDouble();
                break;
            default:
                System.out.println("invalid option!");
        }
    }
}
