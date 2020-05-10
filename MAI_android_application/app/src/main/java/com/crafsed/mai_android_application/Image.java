package com.crafsed.mai_android_application;

public class Image {
    private String name;
    private String coordinates;
    private String size;
    private String extra;

    public String getName() {
        return name;
    }

    public String getCoordinates() {
        return coordinates;
    }

    public String getExtra() {
        return extra;
    }

    public String getSize() {
        return size;
    }

    public void setCoordinates(String coordinates) {
        this.coordinates = coordinates;
    }

    public void setExtra(String extra) {
        this.extra = extra;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setSize(String size) {
        this.size = size;
    }
}
