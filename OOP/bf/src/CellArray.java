public class CellArray {
    public static final int CAPACITY = 30_000;
    private char[] cells = new char[CAPACITY];
    private int currentPos = 0;

    public char getValue() {
        return cells[currentPos];
    }

    public int getPos() {
        return currentPos;
    }

    public void move(boolean isToLeft) {
        currentPos += isToLeft ? -1 : 1;
        if (currentPos < 0)
            currentPos = 0;
        else if (currentPos >= CAPACITY) 
            currentPos = (CAPACITY - 1);
    }

    public void setValue(char val) {
        cells[currentPos] = val;
    }

    public void changeValue(boolean isMinus) {
        cells[currentPos] += isMinus ? -1 : 1;
    }
}
