package com.crafsed.mai_android_application;

import android.content.ContentResolver;
import android.net.Uri;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.math.BigInteger;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;
import java.util.zip.ZipInputStream;

public class Extra {
    String unZipper(File file){
        try {
            ZipFile zipFile = new ZipFile(file, ZipFile.OPEN_READ);
            ZipEntry entry = zipFile.getEntry("doc.kml");
            byte[] buff = new byte[(int)entry.getSize()];
            zipFile.getInputStream(entry).read(buff);
            String s = new String(buff);
            String splited = s.split("LatLonAltBox")[1];
            splited = splited.replaceAll(">","");
            splited = splited.replaceAll("<","");
            splited = splited.replaceAll(" ","");
            splited = splited.replaceAll("west","");
            splited = splited.replaceAll("east","");
            splited = splited.replaceAll("south","");
            splited = splited.replaceAll("north","");
            splited = splited.replaceAll("/","");
            return splited;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }
    static private Extra instance;

    public static Extra getInstance() {
        if (instance==null) instance = new Extra();
        return instance;
    }
    private Extra(){}
}
