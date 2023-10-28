import java.io.*;
import java.util.*;

public class CheckKeyword {
    public static void main(String[] args) throws IOException {
        String[] keywords = {
                "abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class", "const", "continue",
                "default", "do", "double", "else", "enum", "extends", "final", "finally", "float", "for", "goto", "if",
                "implements", "import", "instanceof", "int", "interface", "long", "native", "new", "package", "private",
                "protected", "public", "return", "short", "static", "strictfp", "super", "switch", "synchronized",
                "this", "throw", "throws", "transient", "try", "void", "volatile", "while"
        };
        String[] operators = {
                "=", "+", "-", "*", "/", "%", "++", "--", "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "&", "|",
                "^", "~", "<<", ">>", ">>>", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", ">>>=", "?:",
                "instanceof"
        };

        File myObj = new File(
                "C:\\Users\\harsh\\OneDrive - pdpu.ac.in\\HARSH\\_STUDY MATERIAL\\SEM 5\\Compiler Design\\Compiler Design Lab\\LAB 1\\input.txt");
        Scanner myReader = new Scanner(myObj);
        String data = "";
        String[] text = new String[50];
        while (myReader.hasNextLine()) {
            data = data + " " + myReader.nextLine();
            text = data.split(" ");
        }

        // Result arrays
        ArrayList<String> keywords_found = new ArrayList<String>();
        ArrayList<String> operators_found = new ArrayList<String>();

        // Keywords
        System.out.print("Keywords: ");
        for (String word : text) {
            for (String key : keywords) {
                if (key.equals(word) & !keywords_found.contains(word)) {
                    keywords_found.add(word);
                    System.out.print(word + " ");
                }
            }
        }
        // Operator
        System.out.print("\nOperators: ");
        for (String word : text) {
            for (String key : operators) {
                if (key.equals(word) & !operators_found.contains(word)) {
                    operators_found.add(word);
                    System.out.print(word + " ");
                }
            }
            myReader.close();
        }
    }
}