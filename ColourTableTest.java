import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class ColourTableTest {

    @Test
    void fourDividedByTwoReturnsTrue() {
        int validNum = 4;
        ColourTable division = new ColourTable(validNum);
        assertTrue(ColourTable.thePowerOfTwo(validNum));
    }

    @Test
    void sevenDividedByTwoReturnsFalse() {
        int invalidNum = 7;
        assertFalse(ColourTable.thePowerOfTwo(invalidNum));
    }

    @Test
    void validPaletteSize() {
        int validNumColours = 16;
        ColourTable valid = new ColourTable(validNumColours);
        assertEquals(validNumColours, valid.getNumColours() );
    }

    @Test
    void paletteSizeTooBigReturnsException() {
        int invalidNumColours = 1050;
        assertThrows(IllegalArgumentException.class, () ->new ColourTable(invalidNumColours));
    }

    @Test
    void paletteSizeTooSmallReturnsException() {
        int invalidNumColours = 1;
        assertThrows(IllegalArgumentException.class, () ->new ColourTable(invalidNumColours));
    }

    @Test
    void invalidRgbValue() {
        int validSize = 8;
        int red = 256, green = 256, blue = 256;
        assertThrows(IllegalArgumentException.class, () -> new ColourTable(validSize).add(red, green, blue));
    }

    @Test
    void validRgbValue() {
        int validSize = 8;
        int red = 255, green = 0, blue = 0;
        ColourTable validRgb = new ColourTable(validSize);
        int initialSize = validRgb.getColoursList().size();

        validRgb.add(red, green, blue);

        int newSize = validRgb.getColoursList().size();
        assertNotEquals(initialSize, newSize);
    }

    @Test
    void paletteIsFull() {
        int fullPalette = 1025;
        int red = 255, green = 0, blue = 0;
        assertThrows(IllegalArgumentException.class, () -> new ColourTable(fullPalette).add(red, green, blue));
    }

    @Test
    void doesColourExist() {
        int validSize = 4;
        int red = 255, green = 0, blue = 0;
        ColourTable existing = new ColourTable(validSize);
        existing.add(red, green, blue);
        assertThrows(IllegalArgumentException.class, () -> existing.add(red, green, blue));
    }
}
