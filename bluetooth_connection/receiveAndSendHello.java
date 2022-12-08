//Working file to replicate receiveAndSendHello.py but for java
//currently uses jSerialComm jar file from https://fazecast.github.io/jSerialComm/
//after putting the jar file in the directory with this file:
//compile with javac -cp ".;jSerialComm-2.7.0.jar" receiveAndSendHello.java
//run with     java -cp ".;jSerialComm-2.7.0.jar" receiveAndSendHello
import com.fazecast.jSerialComm.*;
import java.util.Arrays;
import java.io.InputStream;

public class receiveAndSendHello{
    /**
    This method reads a given amount of bytes from a port and stores it in a given bytes array.
    @param port the SerialPort port to read from
    @param bytes byte array to store encoded bytes message
    @exception throws a UnsupportedEncodingException when incoming message is not encoded in utf-8
    */
    public static void readByBytes(SerialPort port, byte[] bytes){
        System.out.println("\nWaiting for message...");
        port.readBytes(bytes, 7);
        try{
            System.out.println("Message from " + port.getSystemPortName() + " :\n" + new String(bytes, "UTF8"));
        }
        catch (Exception e) {
            System.out.println(e.toString());
        }
    }
    /**
    This method reads from a SerialPort port using an InputStream associated with the SerialPort object.
    @param port the SerialPort to read from and create an InputStream object from
    @param bytes byte array to store encoded bytes message
    */
    public static String readWithInputStream(SerialPort port, byte[] bytes){
        InputStream istream;
        int numberOfBytes = 0;
        String msgFromSpike;
        istream = port.getInputStream();
        msgFromSpike = "";
        //Loops to receive data from buffer
        while(numberOfBytes == 0) {
            try{
                numberOfBytes = istream.read(bytes);
                
                //Outputs message from buffer and outputs terminal message
                msgFromSpike = new String(bytes, "UTF8");
                istream.close();
            }
            catch(Exception e){
                System.out.println(e.toString());
                break;
            }
        }
        return msgFromSpike;
        //commented out to repurpose as a clear buffer for now
        //System.out.println("Message from Lego Hub: " + msgFromSpike);
        //Haven't sent a message, but definitely tried to read
        //System.out.println("Received and sent message...");
    }
    /**
    This method writes a message to a given port.
    @param port the SerialPort port to write to
    @param msg message to write
    */
    public static void sendMsg(SerialPort port, String msg){
        System.out.println("Sending message '" + msg + "'...");
        try{
            byte[] msgBytes = msg.getBytes("UTF8");
            port.writeBytes(msgBytes, msgBytes.length);
        }
        catch (Exception e) {
            System.out.println(e.toString());
        }
    }
    public static void closeIfOpen(SerialPort port){
        String closeMsg;

        if(port.isOpen()){
            System.out.println("Closing " + port.getSystemPortName() + "  port...");
            closeMsg = (port.closePort() == true) ? "Successfully closed." : "It's still open somehow???";
            System.out.println(closeMsg);
        }
    }

    public static void main(String args[]){
        SerialPort[] sPorts;
        SerialPort lego;
        boolean legoIsOpen;
        String msg;
        byte[] byteBuffer = new byte[1000];
        byte[] byteBuffer2 = new byte[100];

        //Get available ports and print out their descriptions and port status
        sPorts = SerialPort.getCommPorts();
        System.out.printf("Length of sPorts (array of all communication ports): %d\n", sPorts.length);
        for(int i = 0; i<sPorts.length; i++){
            System.out.printf("Description of port %d :\n %s \n", i, sPorts[i].getPortDescription());
            System.out.printf("Is this port open? : %b\n", sPorts[i].isOpen());

        }
        //Okay, now try opening the bluetooth ports for the lego hub
        //Can not have 2 ports open at the same time, seems to have closed first port when second is opened.
        lego = SerialPort.getCommPort("COM4");

        //set read to block
        lego.setComPortTimeouts(SerialPort.TIMEOUT_READ_SEMI_BLOCKING, 10000, 0);

        //Test to see if it grabbed the right thing
        System.out.println("Lego port description: " + lego.getPortDescription() + " "+ lego.getSystemPortName());
        legoIsOpen = lego.openPort();
        System.out.printf("Tried to open COM4... Success? : %b\n", legoIsOpen);
        
        /*try to read with inputstream
        currently does not work as intended, outputs hub REPL for some reason
        EDIT 10/29/21: so it might work, but the first however many bytes read are the REPL no 
        matter what, so maybe just use this to clear the read buffer for now?
        */
        readWithInputStream(lego, byteBuffer);
        System.out.println("Message from Lego: " + readWithInputStream(lego, byteBuffer2));

        //try to read/write w/o inputstream, straight through readBytes/writeBytes in SerialPort
        //test to read and send a hello message
        //readByBytes(lego, byteBuffer2);
        //sendMsg(lego, "Hey!");

        //test sending a JSON string
        sendMsg(lego,"[\"Button\", \"Left\", \"WaitUntilPressed\"]" );

        //Close port if open
        closeIfOpen(lego);

        //Opening port seems to work... now, does reading/writing?

        //Current Output
        /**
        Length of sPorts (array of all communication ports): 3
        Description of port 0 :
        BthModem1
        Is this port open? : false
        Description of port 1 :
        BthModem0
        Is this port open? : false
        Description of port 2 :
        LEGO Technic Large Hub in FS Mode
        Is this port open? : false
        Lego port description: User-Specified Port COM4
        Tried to open COM4... Success? : true

        Waiting for message...
        Message from COM4 :
        Hello!
        Sending message 'Hey!'...
        Closing COM4  port...
        Successfully closed.
        */
    }
}
