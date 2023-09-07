import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.util.ArrayDeque;
import java.util.ArrayList;

public class Interpreter {
    private final OutputStream outputStream;
    private final BufferedReader inputReader;
    private ArrayList<Command> programm;
    private int programmPos = -1;

    // Stack which elements are positions in programm where while block starts,
    // innerBlockPosStack.pop() returns position of most recent opened block
    private ArrayDeque<Integer> innerBlockPosStack = new ArrayDeque<>();

    public Interpreter(
        InputStream inputStream, 
        OutputStream outputStream, 
        ArrayList<Command> programm
    ) {
        this.inputReader = new BufferedReader(new InputStreamReader(inputStream));
        this.outputStream = outputStream;
        this.programm = programm;
    }

    public Interpreter(InputStream inputStream, OutputStream outputStream) {
        this(inputStream, outputStream, new ArrayList<Command>());
    }

    public void accept(Command cmd) {
        programm.add(cmd);
    }

    public void accept(ArrayList<Command> concatProgramm) {
        programm.addAll(concatProgramm);
    }
}
