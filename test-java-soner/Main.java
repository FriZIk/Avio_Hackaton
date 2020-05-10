import java.io.*;
import java.math.BigInteger;
import java.net.Socket;
import java.nio.ByteBuffer;
import java.util.Arrays;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

public class Main {
    static String IP = "0.tcp.ngrok.io";
    static int PORT = 17748;

    public static void main(String[] args) {
        try {
            Socket socket = new Socket(IP, PORT);
            InputStream inputStream = socket.getInputStream();
            OutputStream outputStream = socket.getOutputStream();

            ZipFile zipFile = new ZipFile(new File("./v1.kmz"), ZipFile.OPEN_READ);
            ZipEntry entry = zipFile.getEntry("doc.kml");

            String str = new String(zipFile.getInputStream(entry).readAllBytes());
            String splited = str.split("LatLonAltBox")[1];

            byte[] splB = splited.getBytes();
            BigInteger bigInteger1 = BigInteger.valueOf(splB.length);

            File testImg = new File("./test.jpg");
            FileInputStream fileInputStream = new FileInputStream(testImg);
            byte[] imgB = fileInputStream.readAllBytes();
            BigInteger bigInteger2 = BigInteger.valueOf(imgB.length);

            byte[] bar1 = new byte[4];
            byte[] bar11 = bigInteger1.toByteArray();

            byte[] bar2 = new byte[4];
            byte[] bar22 = bigInteger2.toByteArray();

            for (int i = 3, k = bar11.length-1, j = bar22.length-1; i>0; i--){
                if (k>=0){
                    bar1[i] = bar11[k--];
                }  else {
                    bar1[i] = 0;
                }
                if (j>=0){
                    bar2[i] = bar22[j--];
                }  else {
                    bar2[i] = 0;
                }
            }

            outputStream.write(bar1);
            outputStream.write(bar2);

            outputStream.write(splB);
            outputStream.write(imgB);

            byte[] fourBytes = new byte[4];
            inputStream.read(fourBytes);
            int length = ByteBuffer.wrap(fourBytes).getInt();

            byte[] strBytes = new byte[length];
            inputStream.read(strBytes);
            String s = new String(strBytes);
            System.out.println(s);
	     
	    //byte[] fourBytes2 = new byte[40];
            //inputStream.read(fourBytes2);
            //length = inputStream.readInt();
	    //ByteBuffer bb = ByteBuffer.wrap(fourBytes2);
//	    length = bb.getInt();
	  //  for(byte b:fourBytes2) {
	//	char c = (char)b;
	//	System.out.print(b);
		//System.out.format("%d\n", (int)c);
	    //}
	    //System.out.format("output %d\n", length);
            //byte[] imgBytes = new byte[length];
            //inputStream.read(imgBytes);
            //File file = new File("IMAGE.png");
            //if (!file.exists()) file.createNewFile();
            //FileOutputStream fileOutputStream = new FileOutputStream(file);
            //fileOutputStream.write(imgBytes);
            //fileOutputStream.close();
            outputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
