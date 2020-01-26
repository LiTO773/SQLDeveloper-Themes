package fxfiles;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.ComboBox;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.VBox;
import org.controlsfx.control.CheckListView;
import project.AvailableSchemes;
import project.PatchThemes;
import project.SDInstalls;

public class Controller {

    public ImageView logoView;
    public CheckListView<String> schemesList;
    public VBox schemeVBox;
    public ComboBox locations;

    @FXML
    public void initialize() {
        // Set the logo
        logoView.setImage(new Image(Controller.class.getResourceAsStream("/logo.png")));

        // Set the schemes
        schemesList = new CheckListView<>(prepareSchemes());
        schemeVBox.getChildren().add(schemesList);

        // Set the installs available
        locations.getItems().addAll(SDInstalls.getInstalls());
        locations.setValue(SDInstalls.getInstalls().get(0));
    }

    private ObservableList<String> prepareSchemes() {
        ObservableList<String> result = FXCollections.observableArrayList();
        result.addAll(AvailableSchemes.getSchemes());
        return result;
    }

    public void patch(ActionEvent actionEvent) {
        boolean result = PatchThemes.patchSchemes(locations.getSelectionModel().getSelectedIndex(), schemesList.getCheckModel().getCheckedIndices());

        if (result) {
            Alerts.successSchemes();
        } else {
            Alerts.errorSchemes();
        }
    }

    public void reset(ActionEvent actionEvent) {
        if (Alerts.invalidateDtCache()) {
            if (PatchThemes.deleteSchemes(locations.getSelectionModel().getSelectedIndex())) {
                System.exit(0);
            } else {
                Alerts.errorSchemes();
            }
        }
    }
}
