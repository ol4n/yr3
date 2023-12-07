import java.util.ArrayList;
import java.util.List;

public class ColourTable {
    private int numColours;
    private List<Integer> coloursList;
    public static boolean thePowerOfTwo(int n) {
        if (n <= 0) {
            return false;
        }
        while (n > 1) {
            if (n%2 != 0)
                return false;
            n = n/2;
        }
        return true;
    }

    public ColourTable(int numColours) {
        if (numColours <= 1 || numColours > 1024) {
            throw new IllegalArgumentException("Colour palette size must be between 1 and 1025");
        } else if (!thePowerOfTwo(numColours)) {
            throw new IllegalArgumentException("Colour palette size must be a power of 2");
        }
        this.numColours = numColours;
        this.coloursList = new ArrayList<>();
    }

    public int getNumColours() {
        return numColours;
    }

    public List<Integer> getColoursList() {
        return coloursList;
    }

    public void add(int red, int green, int blue) {
        if (!(red >= 0 && red <= 255 || green >= 0 && green <= 255 || blue >= 0 && blue <= 255)) {
            throw new IllegalArgumentException("Invalid RGB value");
        }

        int rgbConvert = (red << 16) | (green << 8) | blue;
        if (coloursList.size() >= getNumColours()) {
            throw new IllegalStateException("The colour palette is already full");
        } else if (coloursList.contains(rgbConvert)) {
            throw new IllegalArgumentException("The colour already exists");
        } else {
            coloursList.add(rgbConvert);
        }
    }
}
