package project;

import java.io.File;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Responsible for finding SQLDeveloper installs
 */
public class SDInstalls {
    private static List<String> installs;

    public static void findInstalls() {
        installs = new ArrayList<>();

        // Get the correct platform path
        String mainPath = System.getProperty("user.home") + "/.sqldeveloper";
        if (System.getProperty("os.name").contains("Windows")) {
            mainPath = System.getenv("APPDATA") + "\\SQL Developer";
        }

        // Get all the folders that have <version>/o.ide/dtcache.xml
        File[] directories = new File(mainPath).listFiles((File f) -> {
//            String path = mainPath;
            if (f.isDirectory()) {

                // Check for <version>/o.ide
                Pattern folderPattern = Pattern.compile("^o\\.ide\\.[0-9]");
                f.listFiles((File f2) -> {
                    Matcher m = folderPattern.matcher(f2.getName());
                    if (m.find()) {
                        // Find if it contains dtcache.xml
                        File[] found = f2.listFiles((File f3) -> {
                            return f3.getName().equals("dtcache.xml");
                        });

                        // Add the folder to installs
                        if (found.length == 1) {
                            installs.add(found[0].getAbsolutePath());
                        }

                        return false;
                    }

                    return false;
                });
            }
            return false;
        });
    }

    public static List<String> getInstalls() {
        return installs;
    }
}
