package project;

import java.util.ArrayList;
import java.util.Scanner;

public class NoGuiMain {
    private static int version = 0;

    public static void main(String[] args) {
        System.out.println("==========================================");
        System.out.println("Welcome to Pimp My SQLDeveloper!");
        System.out.println("==========================================");

        AvailableSchemes.findSchemes();
        SDInstalls.findInstalls();

        initialCheck();
        selectVersion();
        selectAction();
    }

    private static void initialCheck() {
        // if no installs of SQLDeveloper were found, warn and quit the application
        if (SDInstalls.getInstalls().isEmpty()) {
            System.out.println("No SQLDeveloper installs were found, quitting");
            System.exit(1);
        }

        // if no schemes were found, warn the user and quit the application
        if (AvailableSchemes.getSchemes().isEmpty()) {
            System.out.println("No color schemes were found, please make sure you have the folder ../schemes");
            System.exit(1);
        }
    }

    private static void selectVersion() {
        // If only one version exists, skip
        if (SDInstalls.getInstalls().size() == 1) {
            version = 0;
            return;
        }

        // Allow the user to choose the version
        System.out.println("\n\nPick the SQLDeveloper version:");
        int i = 0;
        for (String s: SDInstalls.getInstalls()) {
            System.out.printf("%d - %s%n", i++, s);
        }

        System.out.print("Write a valid number, anything else will quit the application: ");

        Scanner in = new Scanner(System.in);
        try {
            int answer = Integer.parseInt(in.nextLine());

            if (answer < SDInstalls.getInstalls().size()) {
                version = answer;
            } else {
                System.exit(1);
            }
        } catch (NumberFormatException e) {
            System.exit(1);
        }
    }

    private static void selectAction() {
        System.out.println("\n\nChoose which operation you want do:");
        System.out.println("1 - Patch the schemes in ../schemes");
        System.out.println("2 - Reset schemes in SQLDeveloper");

        System.out.print("Write a valid number, anything else will quit the application: ");

        Scanner in = new Scanner(System.in);
        try {
            int answer = Integer.parseInt(in.nextLine());

            if (answer == 1) {
                schemes();
            } else if (answer == 2) {
                reset();
            } else {
                System.exit(1);
            }
        } catch (NumberFormatException e) {
            System.exit(1);
        }
    }

    private static void schemes() {
        System.out.println("\n\nThe following color schemes where found:");
        ArrayList<Integer> all = new ArrayList<>();
        int i = 0;
        for (String s: AvailableSchemes.getSchemes()) {
            System.out.printf("- %s%n", s);
            all.add(i);
            i++;
        }

        System.out.println("Would you like to patch them?");
        System.out.print("Write Y for yes, anything wil quit the application: ");

        Scanner in = new Scanner(System.in);
        String answer = in.nextLine();

        if (answer.charAt(0) == 'Y' || answer.charAt(0) == 'y') {
            PatchThemes.patchSchemes(version, all);
        } else {
            System.exit(1);
        }

        System.out.println("The schemes have been patched successfully!");
    }

    private static void reset() {
        System.out.println("\n\nREAD THE INSTRUCTIONS BELOW:");
        System.out.println("You're about to reset your color schemes. Don't worry, this will only reset your color schemes. After writing 'OK' do the following steps:\n" +
                " - Open SQLDeveloper\n" +
                " - Close SQLDeveloper\n" +
                " - Open Pimp My SQLDeveloper again to patch the themes\n" +
                "This steps are required since SQLDeveloper will rebuild the default schemes file on close, ensuring it is formatted correctly.");

        System.out.print("Type OK to continue: ");

        Scanner in = new Scanner(System.in);
        String answer = in.nextLine();

        if (answer.trim().equalsIgnoreCase("ok")) {
            PatchThemes.deleteSchemes(version);
            System.out.println("The schemes have been reset successfully!");
        } else {
            System.exit(1);
        }
    }
}
