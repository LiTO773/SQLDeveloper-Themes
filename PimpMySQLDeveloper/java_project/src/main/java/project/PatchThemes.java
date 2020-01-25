package project;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Stream;

public class PatchThemes {
    public static boolean deleteSchemes(int pathIndex) {
        String path = SDInstalls.getInstalls().get(pathIndex);
        return writeDtcache(path, "");
    }

    public static boolean patchSchemes(int pathIndex, List<Integer> schemesIndex) {
        String path = SDInstalls.getInstalls().get(pathIndex);
        StringBuilder newContent = new StringBuilder();
        boolean appended = false;

        try (Stream<String> stream = Files.lines(Paths.get(path))) {
            stream.forEach((String s) -> {
                newContent.append(s);

                // If it is <schemeMap>, start appending the new themes
                if (appended == false && s.contains("<schemeMap>")) {
                    for (int sIndex : schemesIndex) {
                        String sPath = "../schemes/" + AvailableSchemes.getSchemes().get(sIndex);

                        // Read the file's content
                        readSchemeFile(sPath, newContent);
                    }
                }
            });
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }

        // Write to dtcache.xml
        return writeDtcache(path, newContent.toString());
    }

    private static void readSchemeFile(String sPath, StringBuilder newContent) {
        try (Stream<String> stream = Files.lines(Paths.get(sPath))) {
            stream.forEach(newContent::append);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static boolean writeDtcache(String sPath, String content) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(sPath))) {
            writer.write(content);
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        return true;
    }
}
