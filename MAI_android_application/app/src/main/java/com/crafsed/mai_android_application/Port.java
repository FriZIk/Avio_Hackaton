package com.crafsed.mai_android_application;

import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.drawable.Drawable;
import android.net.Uri;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.math.BigInteger;
import java.net.Socket;
import java.nio.ByteBuffer;

public class Port {
    static File img;
    static String info;
    static String text;
    static void send(Context context){
        SharedPreferences sharedPreferences = context.getSharedPreferences("SETTINGS",Context.MODE_PRIVATE);
        String ip = sharedPreferences.getString("IP","0.tcp.ngrok.io");
        int port = sharedPreferences.getInt("PORT",17748);
        try {
            Socket socket = new Socket(ip, port);
            InputStream inputStream = socket.getInputStream();
            OutputStream outputStream = socket.getOutputStream();

            byte[] splB = info.getBytes();
            BigInteger bigInteger1 = BigInteger.valueOf(splB.length);

            FileInputStream fileInputStream = new FileInputStream(img);
            byte[] imgB = new byte[(int)img.length()];
            fileInputStream.read(imgB);

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
            System.out.println(length);

            byte[] strBytes = new byte[length];
            inputStream.read(strBytes);
            String s = new String(strBytes);
            System.out.println(s);
            text = s;
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
