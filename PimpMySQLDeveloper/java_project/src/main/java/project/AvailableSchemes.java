package project;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class AvailableSchemes {
    private static List<String> schemes;

    /**
     * Gets the schemes available in the folder ../schemes
     */
    public static void findSchemes() {
        try (Stream<Path> walk = Files.walk(Paths.get("../schemes/"))) {

            schemes = walk.filter(Files::isRegularFile)
                    .map(x -> x.getFileName().toString()).collect(Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static List<String> getSchemes() {
        return schemes == null ? new ArrayList<>() : schemes;
    }
}
