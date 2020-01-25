package project;

import javafx.application.Application;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;

import java.util.Optional;

/**
 * Responsible for all possible alerts in the application
 */
public class Alerts {
    public static void noSchemesFound() {
        Alert alert = new Alert(Alert.AlertType.WARNING);
        alert.setTitle("No schemes found");
        alert.setHeaderText("Uh oh! No schemes were found");
        alert.setContentText("Make sure the .jar is placed on a location where ../schemes is accessible.");

        alert.showAndWait();
    }

    public static void noInstallsFound() {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle("No installs found");
        alert.setHeaderText("Uh oh! No SQLDeveloper installs were found");
        alert.setContentText("Make sure that SQLDeveloper was installed correctly, since neither ~/.sqldeveloper or %appdata%/SQL Developer were found!");

        alert.showAndWait();
        System.exit(1);
    }

    public static void successSchemes() {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Done!");
        alert.setHeaderText("And... it's done 🎉");
        alert.setContentText("The schemes have been patched, you can now apply them in your Preferences.");

        alert.showAndWait();
        System.exit(0);
    }

    public static void errorSchemes() {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle("Unable to write to file!");
        alert.setHeaderText("Unable to write to file!");
        alert.setContentText("There was an error writing to dtcache.xml. Please check the console for further information.");

        alert.showAndWait();
        System.exit(1);
    }

    public static boolean invalidateDtCache() {
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION);
        alert.setTitle("dtcache.xml reset");
        alert.setHeaderText("You are about the reset your SQLDeveloper schemes");
        alert.setContentText("Don't worry, this will only reset your color schemes. After clicking 'OK' do the following steps:\n" +
                " - Open SQLDeveloper\n" +
                " - Close SQLDeveloper\n" +
                " - Open Pimp My SQLDeveloper to patch other themes\n" +
                "This steps are required since SQLDeveloper will rebuild the default schemes file on close, ensuring it is formatted correctly.");

        Optional<ButtonType> result = alert.showAndWait();
        return result.get() == ButtonType.OK;
    }
}
