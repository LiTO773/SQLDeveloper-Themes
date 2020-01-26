package project;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {
        AvailableSchemes.findSchemes();
        SDInstalls.findInstalls();

        // if no installs of SQLDeveloper were found, warn and quit the application
        if (SDInstalls.getInstalls().isEmpty()) Alerts.noInstallsFound();

        // if no schemes were found, warn the user
        if (AvailableSchemes.getSchemes().isEmpty()) Alerts.noSchemesFound();

        primaryStage.setResizable(false);
        Parent root = FXMLLoader.load(getClass().getResource("/mainScene.fxml"));
        primaryStage.setTitle("Pimp My SQLDeveloper");
        primaryStage.setScene(new Scene(root, 660, 580));
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
